from os import path

# importing my scripts
from Resources.scripts.amz200k.extract import data_handler
from Resources.scripts.amz200k.transform import transform_data

# This script goes over the Amazon's raw 200K reviews from Kaggle - datasets not included in base code
filepath = path.join("..", "..", "datasets", "unzipped", "200000-amazon-reviews", "amz200k.json")

# Getting raw data from Amazon 200K dataset Unzipped
filelines = data_handler.readFile(filepath)

# Getting set of unique and random indexes
indexSet = data_handler.randomSet(low=0, high=len(filelines), size=1500)

# Getting the set of random json reviews extracted from amz200k.json into a dictionary
amzReviews = data_handler.extractData(indexSet=indexSet, filelines=filelines)

# Preparing reviews to export as csv
outputList = transform_data.extractColumns(amzReviews)

# List of columns go in and a DataFrame comes out
reviewsDF = transform_data.toDataFrame(outputList)

print(reviewsDF.head(2))


