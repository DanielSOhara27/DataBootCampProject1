from pandas import DataFrame

# Formatting kindle_reviews Review Times from MM DD, YYYY
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

    reviewersid = list()
    asins = list()
    reviewtexts = list()
    overalls = list()
    summaries = list()
    reviewtimes = list()

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
            reviewerid = review["reviewerID"]
            asin = review["asin"]
            reviewtext = review["reviewText"]
            overall = review["overall"]
            summary = review["summary"]
            reviewtime = review["reviewTime"]

            print(f"Finished processing review | {counter} of {size}")

        except:
            print(f"Skipping review {counter} of {size}")

        reviewersid.append(reviewerid)
        asins.append(asin.strip())
        reviewtexts.append(reviewtext.strip())
        overalls.append(overall)
        summaries.append(summary.strip())
        reviewtimes.append(reviewtime.strip())

    # kindle_reviews.json dataset has the review time format MM DD, YYYY
    # This format is not recognized by MySQL 5.7, therefore I am
    # reformatting it to be YYYY-MM-DD
    reviewtimes = formatDate(reviewTime_list=reviewtimes)

    print(f"\n{'-' * 35}\nFinished processing dataset\n{'-' * 35}")

    outputList.append(reviewtimes)
    outputList.append(asins)
    outputList.append(overalls)
    outputList.append(summaries)
    outputList.append(reviewersid)
    outputList.append(reviewtexts)

    return outputList

def toDataFrame(cleanColumns):
    dataframe = DataFrame({
        "Review Time" : cleanColumns[0],
        "ASIN" : cleanColumns[1],
        "Overall" : cleanColumns[2],
        "Summary" : cleanColumns[3],
        "Reviewer ID" : cleanColumns[4],
        "Review Text" : cleanColumns[5]
    })

    print(f"\n{'-' * 35}\nFinished creating the Dataframe\n{'-' * 35}")

    return dataframe
