from os import path
from Resources.scripts.amz200k.extract import data_handler
from Resources.scripts.amz200k.load import output_handler

# This script goes over the Amazon's raw 200K reviews from Kaggle - datasets not included in base code
filelocation = path.join("..","..", "..", "datasets", "unzipped", "200000-amazon-reviews")
filename = "amz200k.json"

# Getting raw data from Amazon 200K dataset Unzipped
filelines = data_handler.readFile(path.join(filelocation,filename))

# Splitting the data into
output_handler.splitDatasetJson(filelines, filename, filelocation, size=3000)
