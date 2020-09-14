# Forum

Our organization has a forum that has been running for quite some time, and we've recently added some logic to mark comments on forum posts as positive or negative. With this new information, some people without database access would like to be able to have the information exported so that they can view reports. To facilitate this, we've decided to create a library for interacting with the database and models that we can easily utilize in scripts to export information in a digestable form for whomever asks us. Our library will only provide models for the database tables; the end user will be required to know how to set up a SQLAlchemy engine and session.

The forum database has two tables that we'd like to interact with:

    The posts table, which contains forum posts.
    The comments table, which contains comments that are associated with posts.

![Screenshot](img/img01.png)

Databases are great for storing and allowing us to query information, but the default shape and SQL are not always the best options for people within our organization. If we know the schema of our database tables, we can create classes to model our data and then massage the data into other shapes that are more helpful for specific use cases. We will use an existing SQLAlchemy library to query our forum database and export data as both JSON and CSV for other employees in our organization.

## Set Up a Project and Virtualenv with pipenv
To set up our project, we're going to create a new directory with an internal directory of the same name (forum) to hold our Python package:
```
$ mkdir -p forum/forum
$ cd forum
```
We'll also need to add an __init__.py to the internal forum directory to mark it as a package:
```
$ touch forum/__init__.py
```
Next, let's make sure that pipenv is installed and use it to create our virtualenv, then install SQLAlchemy and psycopg2-binary so that we can interact with a PostgreSQL database:
```
$ pip3.7 install --user -U pipenv

$ pipenv --python python3.7 install SQLAlchemy psycopg2-binary
```

Once the virtualenv is created, we should activate it while working on this project:
```
$ pipenv shell
(forum) $
```
Lastly, we should create a setup.py so that our library can be installed. A quick and easy way to do this is to use the setup.py for Humans:
```
(forum) $ curl -O https://raw.githubusercontent.com/navdeep-G/setup.py/master/setup.py
```
Now that we have a setup.py, we'll need to change some of the metadata and add our dependencies to the REQUIRED list:

setup.py (partial)
```py
# Package meta-data.
NAME = 'forum'
DESCRIPTION = 'A model library for accessing an internal forum database'
URL = 'https://github.com/me/forum'
EMAIL = 'me@example.com'
AUTHOR = 'Awesome Soul'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.0'

# What packages are required for this module to be executed?
REQUIRED = ['SQLAlchemy', 'psycopg2-binary']
```

## Define the `Post` and `Comment` Classes in a `models` Module

Our library only needs to provide a few classes that we can then use with SQLAlchemy in ad-hoc scripts. To do this, we'll use the declarative_base from SQLAlchemy. Here's the schema for our posts and comments database tables:

```
create table posts (
    id SERIAL PRIMARY KEY,
    body TEXT NOT NULL,
    author_name VARCHAR(50) NOT NULL,
    created_on TIMESTAMP NOT NULL DEFAULT NOW()
);
create table comments (
    id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES posts(id),
    comment TEXT NOT NULL,
    sentiment VARCHAR(10) NOT NULL,
    commenter_name VARCHAR(50) NOT NULL,
    created_on TIMESTAMP NOT NULL DEFAULT NOW()
);
```

Now we can install our library on any machine that needs to interact with the database, and these classes will make working with the data easier. We're not going to add any configuration logic to our helper; the user will be expected to know how to generate a SQLAlchemy engine and a session.

## Utilize the Library from REPL

Before we call this portion of the application completed, we're going to ensure that we can interact with the database the way that we think that we should be able to. Let's install our package using pip install -e . (with our virtualenv started):
```
(forum) $ pip install -e .
```
Now let's open up a REPL, create an engine and a session, and load in some Post and Comment objects to ensure that the library is working as expected. For the engine, you'll need to use the username of admin, a password of password, the public IP address of the database server, port 80, and a database name of forum.
```
(forum) $ python
>>> from sqlalchemy import create_engine
>>> from sqlalchemy.orm import sessionmaker
>>> from forum.models import Post, Comment
>>> engine = create_engine("postgres://admin:password@PUBLIC_IP:80/forum")
>>> Session = sessionmaker(bind=engine)
>>> session = Session()
>>> posts = session.query(Post).limit(10).all()
>>> posts
>>> post = posts[0]
>>> post.__dict__
>>> post.comments[0].__dict__
```

We were successfully able to query our database and populate Post and Comment objects.

## Write the Posts Query in the `export_csv.py` Script


![Screenshot](img/img02.png)


The foundation of both of our export scripts will be the same, so let's write that first. We need to do the following:

    Create a SQLAlchemy engine to connect to our database server.
    Create a Session class that is bound to our engine.
    Create an instance of our Session class to make queries to the database.

This is all done using SQLAlchemy itself instead of relying on code in the forum package. We're also going to pass the database connection in using a DB_URL environment variable when we run the script:

export_csv.py
```py
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = os.environ["DB_URL"]
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()
```
With the SQLAlchemy boilerplate out of the way, we're now ready to use our models. Because we need some information about the comments table but want to receive a row for each post, we'll need to create a few different subqueries to calculate the various comment counts. Let's write these subqueries now:

export_csv.py
```py
# SQLAlchemy configuration omitted

from sqlalchemy.sql import func

from forum.models import Post, Comment

comments = (
    session.query(Comment.post_id, func.count("*").label("comments"))
    .group_by(Comment.post_id)
    .subquery()
)

negative_comments = (
    session.query(Comment.post_id, func.count("*").label("negative_comments"))
    .filter(Comment.sentiment == "negative")
    .group_by(Comment.post_id)
    .subquery()
)

positive_comments = (
    session.query(Comment.post_id, func.count("*").label("positive_comments"))
    .filter(Comment.sentiment == "positive")
    .group_by(Comment.post_id)
    .subquery()
)
```
We'll use these three subqueries as part of the main query that we'll be using to get the posts.

export_csv.py
```py
# Previous code omitted

final_query = (
    session.query(
        Post,
        comments.c.comments,
        negative_comments.c.negative_comments,
        positive_comments.c.positive_comments,
    )
    .outerjoin(comments, Post.id == comments.c.post_id)
    .outerjoin(negative_comments, Post.id == negative_comments.c.post_id)
    .outerjoin(positive_comments, Post.id == positive_comments.c.post_id)
)
```
This query is a bit complicated, but we're getting the information that we want out of the database, making only 4 queries regardless of how many posts and comments there are.

This code will act as the foundation for both of our scripts.

## Add the CSV Export to `export_csv.py`
Now that we have our final query, we need to build a csv.DictWriter and iterate through the rows that are returned from our query. Let's set up the writer first:

export_csv.py
```py
# Other imports omitted
import csv

# Query code omitted

csv_file = open("forum_export.csv", mode="w")
fields = ["id", "body", "author_name", "created_on","comments", "positive_comments", "negative_comments"]
csv_writer = csv.DictWriter(csv_file, fieldnames=fields)
csv_writer.writeheader()
```
Now we have an open file, a CSV writer, and we've written the field names to a header row. The last thing that we need to do is iterate through the final_query and write a CSV row for each row returned from the query using csv_writer.writerow.

export_csv.py
```py
# Previous code omitted

for post, comments, negative_comments, positive_comments in final_query:
    csv_writer.writerow({
        "id": post.id,
        "body": post.body,
        "author_name": post.author_name,
        "created_on": post.created_on.date(),
        "comments": comments or 0,
        "positive_comments": positive_comments or 0,
        "negative_comments": negative_comments or 0
    })

csv_file.close()
```
There are a few modifications that we need to make to the data returned from our query so that it can be written to CSV:

    The timestamp for created_on needs to be turned into a date.
    For each comment value, we need to add a default 0 if there were none returned for the particular post.

The last thing that we need to do is run this:
```
(forum) $ DB_URL=postgres://admin:password@PUBLIC_IP:80/forum python export_csv.py
```
Now we should have properly formatted rows within forum_export.csv.

## Create the `export_json.py` Script
For the JSON export, we'll use much of the same code as export_csv.py, except that we'll rely on the json module instead of the csv module to write out our results.

Let's create export_json.py. We can do this by making a copy of export_csv.py and removing the CSV-related logic:
```
(forum) $ cp export_csv.py export_json.py
```
export_json.py
```py
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = os.environ["DB_URL"]
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy.sql import func

from forum.models import Post, Comment

comments = (
    session.query(Comment.post_id, func.count("*").label("comments"))
    .group_by(Comment.post_id)
    .subquery()
)

negative_comments = (
    session.query(Comment.post_id, func.count("*").label("negative_comments"))
    .filter(Comment.sentiment == "negative")
    .group_by(Comment.post_id)
    .subquery()
)

positive_comments = (
    session.query(Comment.post_id, func.count("*").label("positive_comments"))
    .filter(Comment.sentiment == "positive")
    .group_by(Comment.post_id)
    .subquery()
)

final_query = (
    session.query(
        Post,
        comments.c.comments,
        negative_comments.c.negative_comments,
        positive_comments.c.positive_comments,
    )
    .outerjoin(comments, Post.id == comments.c.post_id)
    .outerjoin(negative_comments, Post.id == negative_comments.c.post_id)
    .outerjoin(positive_comments, Post.id == positive_comments.c.post_id)
)

for post, comments, negative_comments, positive_comments in final_query:
    {
        "id": post.id,
        "body": post.body,
        "author_name": post.author_name,
        "created_on": post.created_on.date(),
        "comments": comments or 0,
        "positive_comments": positive_comments or 0,
        "negative_comments": negative_comments or 0,
    }
```
Since we want the JSON objects to have the same information as the rows in CSV, we've kept the dictionary within our loop.

To finish this script we need to:

    Create an empty list to hold the items.
    Add the dictionary to the items list.
    Dump the items list as JSON to forum_export.json using the json.dump function.

Let's add this now:

export_json.py
```py
# previous code omitted
import json

items = []

for post, comments, negative_comments, positive_comments in final_query:
    items.append(
        {
            "id": post.id,
            "body": post.body,
            "author_name": post.author_name,
            "created_on": str(post.created_on.date()),
            "comments": comments or 0,
            "positive_comments": positive_comments or 0,
            "negative_comments": negative_comments or 0,
        }
    )

with open("forum_export.json", mode="w") as f:
    json.dump(items, f)
```
Now we can export the JSON using a command similar to the one we used for the CSV export:
```
(forum) $ DB_URL=postgres://admin:password@PUBLIC_IP:80/forum python export_json.py
```
We've successfully written scripts for all of the exporting that was requested of us.