# name, level, published, created_on, review_count, avg_rating
# Product 1,1,True,2019-07-10,10,4.3

from dbexport.config import Session
from dbexport.models import Review, Product

from sqlalchemy.sql import func

import csv

csv_file = open("product_ratings.csv", mode="w")
fields = ["name", "level", "published", "created_on", "review_count", "avg_rating"]
csv_writer = csv.DictWriter(csv_file, fieldnames=fields)
csv_writer.writeheader()

session = Session()

reviews_statement = ( # Make a select query
    session.query(
        Review.product_id,
        func.count("*").label("review_count"),
        func.avg(Review.rating).label("avg_rating")
    )
    .group_by(Review.product_id) # Make a group by
    .subquery()  # Make a subquery
)

for product, review_count, avg_rating in (  
    session.query(  # Merge into this query
        Product, reviews_statement.c.review_count, reviews_statement.c.avg_rating
        ).outerjoin(reviews_statement, Product.id == reviews_statement.c.product_id)
    # Each row will return as a 3-tuple
):
    csv_writer.writerow(
        {
            "name": product.name,
            "level": product.level,
            "published": product.published,
            "created_on": product.created_on.date(),
            "review_count": review_count or 0,
            "avg_rating": round(float(avg_rating), 4) if avg_rating else 0,
        }
    )

csv_file.close()