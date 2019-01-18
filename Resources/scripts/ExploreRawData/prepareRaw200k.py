import ast
import os

# importing my script that prepares a set of unique indexes
from Resources.scripts.ExploreRawData import ExploreRaw200k

#importing my script that parses and cleans dirty Amazon200K json strings

#This script goes over the Amazon's 200K reviews
filepath = os.path.join("..", "..", "datasets", "unzipped", "200000-amazon-reviews", "amz200k.json")

#Getting raw data from Amazon 200K dataset Unzipped
#             - - IMPORTANT - -
# You will need to download the dataset and unzip it yourself
# Github does not allow files with size >100MB uploaded through GIT
with open(filepath, "r") as amz20kfile:
    lines = amz20kfile.readlines()
    amz20kfile.close()

#Getting set of unique indexes
indexSet = ExploreRaw200k.randomSet()

#This is the final JSON object that will contain the reviews to be analyzed for this project
jsonOutput = {"reviews": list()}

print(f"\n{'-'*35}Starting to parse reviews\n{'-'*35}")
size = len(indexSet)
counter = 0
try:
    for index in indexSet:

        # @Deprecated code block Start
        # line = cleanLine(lines[index])
        # jsonLine = json.loads(line)
        # jsonOutput["reviews"].append(jsonLine)
        # @Deprecated code block End

        counter += 1
        jsonOutput["reviews"].append(ast.literal_eval(lines[index]))
        print(f"Finished processing json | {counter} of {size}")

except:
    print("There was an error!!!!")
    print(f"({counter})-> {lines[index]}")
    with open("error.txt", "w+") as fp:
        fp.write(lines[index])
        fp.close()
    raise

print(f"\n{'-'*35}Finished processing test dataset \n{'-'*35}")

