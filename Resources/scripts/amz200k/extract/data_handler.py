import numpy as np
import pandas as pd
import ast


def randomSet(low, high, size):
    # This function helps choose a subset of user defined size from Amazon's 200K reviews file
    # This function also returns a list of random indexes that will help prepare the data for
    # reading

    # Generating a list of random integers
    index = np.random.randint(low=low, high=high, size=size)

    # Turning the list into a DataFrame for easier manipulation
    indexPD = pd.DataFrame({"index": index})

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
    # container for set of reviews
    jsonOutput = {"reviews": list()}

    print(f"\n{'-' * 35}Starting to parse reviews\n{'-' * 35}")

    size = len(indexSet)  # Purely aesthetic
    counter = 0  # Purely aesthetic

    try:
        for index in indexSet:
            # @Deprecated code block Start
            # line = cleanLine(lines[index])
            # jsonLine = json.loads(line)
            # jsonOutput["reviews"].append(jsonLine)
            # @Deprecated code block End

            counter += 1
            jsonOutput["reviews"].append(ast.literal_eval(filelines[index]))
            print(f"Finished processing json | {counter} of {size}")

    except:
        print("There was an error!!!!")
        print(f"({counter})-> {filelines[index]}")
        with open("tmp/error.txt", "w+") as fp:
            fp.write(filelines[index])
            fp.close()
        raise

    print(f"\n{'-' * 35}Finished processing test dataset \n{'-' * 35}")

    return jsonOutput


def readFile(filepath):
    #             - - IMPORTANT - -
    # You will need to download the dataset and unzip it yourself
    # Github does not allow files with size >100MB uploaded through GIT
    # the url to the datasets can be found in the project proposal's readme
    with open(filepath, "r") as amz20kfile:
        filelines = amz20kfile.readlines()
        amz20kfile.close()
    return filelines
