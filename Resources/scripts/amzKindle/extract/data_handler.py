from numpy import random
from pandas import DataFrame
from ast import literal_eval


def randomSet(low, high, size):
    # This function helps choose a subset of user defined size from Amazon's Kindle reviews file
    # This function also returns a list of random indexes that will help prepare the data for
    # reading

    # Generating a list of random integers
    index = random.randint(low=low, high=high, size=size)

    # Turning the list into a DataFrame for easier manipulation
    indexPD = DataFrame({"index": index})

    # Getting rid of duplicates in the subset
    indexPD.drop_duplicates(subset="index", keep=False, inplace=True)

    # I arbitrarily chose to work with a subset that is a factor of 100
    # So here I get rid of the extra indexes.
    if (indexPD["index"].count() % 100 != 0):
        low = indexPD["index"].count() - (indexPD["index"].count() % 100)
        high = indexPD["index"].count()
        indexPD.drop(indexPD.index[low:high], inplace=True)

    # Sorting values of Dataframe into ascending order for easier use in later steps
    indexPD.sort_values(by=["index"], inplace=True)

    # Reseting the indexes in the Dataframe and NOT letting the original indexes become a column
    indexPD.reset_index(drop=True, inplace=True)

    # Returning a list of unique indexes sorted in ascending order that will be used in later steps
    return indexPD["index"].tolist()

def extractData(indexSet, filelines):
    # This function reads each line of the variable fileline (This is a list with
    # with all the reviews read from amz200k.json we will now parse the lines from
    # raw text and turn it into a dictionary of dictionaries

    # container for set of reviews
    jsonOutput = {"reviews": list()}

    print(f"\n{'-' * 35}\nStarting to parse reviews\n{'-' * 35}")

    size = len(indexSet)  # Purely aesthetic counter for I/O feedback
    counter = 0  # Purely aesthetic counter for I/O feedback

    try:
        for index in indexSet:
            # @Deprecated code block Start
            # line = cleanLine(lines[index])
            # jsonLine = json.loads(line)
            # jsonOutput["reviews"].append(jsonLine)
            # @Deprecated code block End

            counter += 1
            jsonOutput["reviews"].append(literal_eval(filelines[index]))
            print(f"Finished processing json | {counter} of {size}")

    except:
        print("There was an error!!!!")
        print(f"({counter})-> {filelines[index]}")

        #BUG -> Error log will only contain one line.
        with open("tmp/error.txt", "w+") as fp:
            fp.write(filelines[index])
            fp.close()
        raise

    print(f"\n{'-' * 35}\nFinished processing test dataset\n{'-' * 35}")

    return jsonOutput

def readFile(filepath):
    #                    - - - - - - - - -
    #                    - - IMPORTANT - -
    #                    - - - - - - - - -
    # You will need to download the dataset and unzip it yourself
    # Github does not allow files with size >100MB uploaded through GIT
    # the url to the datasets can be found in the project proposal's readme
    #
    #
    with open(filepath, "r") as amzkindlefile:
        filelines = amzkindlefile.readlines()
        amzkindlefile.close()
    return filelines

def unzipData(fromPath, toPath):
    import zipfile

    try:
        zip_ref = zipfile.ZipFile(fromPath, 'r')
        zip_ref.extractall(path=toPath)
        zip_ref.close()

    except:
        print("There was an error unzipping the file")
        raise

