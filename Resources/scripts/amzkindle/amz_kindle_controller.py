from os import path

# Importing my scripts for Kindle
from Resources.scripts.amzKindle.extract import data_handler
from Resources.scripts.amzKindle.transform import transform_data
from Resources.scripts.amzKindle.load import output_handler


# This script goes over the Amazon's raw Kindle reviews from Kaggle - datasets not included in base code
filepath = path.join("..", "..", "datasets", "unzipped", "kindle-reviews", "kindle_reviews.json")

# Getting raw data from Amazon kindle dataset Unzipped
filelines = data_handler.readFile(filepath)

# Getting set of unique and random indexes
indexSet = data_handler.randomSet(low=0, high=len(filelines), size=1500)

# Getting the set of random json reviews extracted from kindle_reviews.json into a dictionary
amzReviews = data_handler.extractData(indexSet=indexSet, filelines=filelines)

# Preparing reviews to export as csv
outputList = transform_data.extractColumns(amzReviews)

# List of columns go in and a DataFrame comes out
reviewsDF = transform_data.toDataFrame(outputList)

output_handler.exportCSV(reviewsDF)

print(f"Finished ETL processes for Amazon kindle review dataset. We worked with a subset of {reviewsDF['Review Time'].count()} randomly chosen reviews")
