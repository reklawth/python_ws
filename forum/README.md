# Forum

Our organization has a forum that has been running for quite some time, and we've recently added some logic to mark comments on forum posts as positive or negative. With this new information, some people without database access would like to be able to have the information exported so that they can view reports. To facilitate this, we've decided to create a library for interacting with the database and models that we can easily utilize in scripts to export information in a digestable form for whomever asks us. Our library will only provide models for the database tables; the end user will be required to know how to set up a SQLAlchemy engine and session.

The forum database has two tables that we'd like to interact with:

    The posts table, which contains forum posts.
    The comments table, which contains comments that are associated with posts.


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