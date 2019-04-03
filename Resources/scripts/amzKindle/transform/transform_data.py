from pandas import DataFrame


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
