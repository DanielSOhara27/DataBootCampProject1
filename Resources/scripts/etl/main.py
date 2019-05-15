from os import path
from pprint import pprint
from pyspark import sql as sparksql
from pyspark import SparkFiles

import Resources.scripts.etl.data_reader as data_handler

# This script goes over the Amazon's raw 200K reviews from Kaggle - datasets not included in base code
filepath = path.join("..", "..", "datasets", "unzipped", "200000-amazon-reviews", "amz200k.json")

spark = sparksql.SparkSession.builder.appName("Python Spark SQL Amazon 200k").getOrCreate()
df = spark.read.json(filepath)
df.show()
#pandaDF = df.toPandas()
#pandaDF.columns.values

# print(df.columns)
# df.createOrReplaceTempView("reviews")
# res = spark.sql("Select _corrupt_record, itemID from reviews where _corrupt_record is not null limit 10")
# res.show()





