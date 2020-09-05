# Easy Data Transformation

## Setup Instructions
- [x] Create centos 7/8 EC2 instance in AWS
- [x] ssh to EC2 instance
- [x] Preemptively address `containerd.io` dependency:
```
sudo yum install -y https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.6-3.3.el7.x86_64.rpm
```
- [x] Install docker in EC2 instance
```
curl https://get.docker.com/ | sudo sh
```
- [x] curl `db_setup.sh` into ec2 instance
```
curl -O https://raw.githubusercontent.com/linuxacademy/content-python-use-cases/master/helpers/db_setup.sh
```

- [x] Change permissions and run setup (script contains commands run as sudo)
```
chmod +x db_setup.sh
./db_setup.sh
```

- From terminal export DB_URL and verify:
```
export DB_URL="postgres://admin:password@PUBLIC_IP:80/reviews"
echo $DB_URL
```

- Open REPL:
```
PYTHONPATH=. python
```

## First Iteration Testing
- Create connection, __make sure port 80 is allowed to EC2 instance__
```
>>> from dbexport.config import engine, get_connection
>>> db = get_connection()
```

```
>>> result = db.execute("SELECT count(id) FROM reviews")
>>> row = result.first()
>>> row
(2997,)
>>> row[0]
2997
```

## Second Iteration Testing

```
>>> from dbexport.config import Session
>>> session
<sqlalchemy.orm.session.Session object at 0x7f2b954f3e80>
```

## Third Iteration Testing

```
>>> from dbexport.config import Session
>>> from dbexport.models import Review, Product
>>> session = Session()
>>> from sqlalchemy import func
>>> session.query(func.count(Product.id))
<sqlalchemy.orm.query.Query object at 0x7f7170b04190>
>>> session.query(func.count(Product.id)).all()
[(999,)]
>>> products = session.query(Product).limit(5).all()
>>> products
[<dbexport.models.Product object at 0x7f7170a37370>, <dbexport.models.Product object at 0x7f7170a37310>, <dbexport.models.Product object at 0x7f7170a37520>, <dbexport.models.Product object at 0x7f7170a37580>, <dbexport.models.Product object at 0x7f7170a375e0>]
```
```
>>> for product in products:
...     print(product.name)
... 
unactability
sporadically
actinostomal
unsaturation
exocrine
```

## Fourth Iteration Testing

```
>>> from dbexport.config import Session
>>> from dbexport.models import Review, Product
>>> session = Session()
>>> products = session.query(Product).limit(5).all()
>>> reviews = products[0].reviews 
>>> reviews
[<dbexport.models.Review object at 0x7f2ee6b7af70>, <dbexport.models.Review object at 0x7f2ee6b870d0>]
>>> reviews[0].rating
1
```

## Fifth Iteration Testing
```
python product_csv.py
```

## Notes:
- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- You will need to set up an [Engine](https://docs.sqlalchemy.org/en/13/core/engines.html?highlight=engine) configuration.
- You will also need to create a [Session Class](https://docs.sqlalchemy.org/en/13/orm/session.html) to be use to start working with the models
- `@lru_cache` decorator from `functools`
- Declaring a [Mapping](https://docs.sqlalchemy.org/en/13/orm/tutorial.html?highlight=declare%20mapping#declare-a-mapping) map from a class to a table using the `declarative_base()` option inside of SQLAlchemy to create a base class and our models will be based off of that.
- ```
  cp product_{csv,json}.py
  ```