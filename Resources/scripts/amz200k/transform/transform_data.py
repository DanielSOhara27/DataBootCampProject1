from pandas import DataFrame

# Formatting Amz200k Review Times from MM DD, YYYY
# to MySQL 5.7 compatible version: YYYY-MM-DD
# i.e "06 27, 2014" -> "2014-27-01"
def formatDate(reviewTime_list):
    clean_times = list()

    for row in reviewTime_list:

        rowArray = row.split(" ")
        new_time = rowArray[2]+"-"+rowArray[0]+"-"

        if(len(rowArray[1]) > 2):
            new_time +=rowArray[1][:2]
        else:
            new_time +=rowArray[1][:1]

        clean_times.append(new_time)

    return clean_times

def extractColumns(reviewsDict):

    categories = list()
    itemID = list()
    reviewText = list()
    rating = list()
    summary = list()
    reviewTime = list()

    # The final list will be held here
    outputList = list()

    # This are purely aesthetic to keep track of progress
    counter = 0
    size = len(reviewsDict["reviews"])

    print(f"\n{'-' * 35}\nStarting to parse review\n{'-' * 35}")

    for review in reviewsDict["reviews"]:

        try:
            counter+=1 # counter for the aesthetic printing

            # Trying to extract the data we need
            category = review["categories"]
            item = review["itemID"]
            rText = review["reviewText"]
            rat = review["rating"]
            summ = review["summary"]
            rTime = review["reviewTime"]

            print(f"Finished processing review | {counter} of {size}")

        except:
            print(f"Skipping review {counter} of {size}")

        categories.append(category)
        itemID.append(item.strip())
        reviewText.append(rText.strip())
        rating.append(rat)
        summary.append(summ.strip())
        reviewTime.append(rTime.strip())



    # Amz200K.json dataset has the review time format MM DD, YYYY
    # This format is not recognized by MySQL 5.7, therefore I am
    # reformatting it to be YYYY-MM-DD
    reviewTime = formatDate(reviewTime_list=reviewTime)

    print(f"\n{'-' * 35}\nFinished processing dataset\n{'-' * 35}")

    outputList.append(reviewTime)
    outputList.append(itemID)
    outputList.append(rating)
    outputList.append(summary)
    outputList.append(categories)
    outputList.append(reviewText)

    return outputList

def toDataFrame(cleanColumns):
    dataframe = DataFrame({
        "Review Time" : cleanColumns[0],
        "Item ID" : cleanColumns[1],
        "Rating" : cleanColumns[2],
        "Summary" : cleanColumns[3],
        "Categories" : cleanColumns[4],
        "Review Text" : cleanColumns[5]
    })

    print(f"\n{'-' * 35}\nFinished creating the Dataframe\n{'-' * 35}")

    return dataframe
