import numpy as np
import pandas as pd

#This function helps choose a substet of size ~=1500 rows from Amazon's 200K reviews file
#This function also returns a list of random indexes that will help prepare the data for
#reading
def randomSet():

    #Generating a list of random integers between 0 and 200K that is of size 1500
    index = np.random.randint(low=-0, high=199999, size=1500)

    #Turning the list into a DataFrame for easier manipulation
    indexPD = pd.DataFrame({"index": index})

    #Getting rid of duplicates in the subset
    indexPD.drop_duplicates(subset ="index", keep = False, inplace = True)

    #I arbitrarily chose to work with a subset that is a factor of 100
    #So here I get rid of the extra indexes.
    if(indexPD["index"].count()%100 !=0):
        low = indexPD["index"].count() - (indexPD["index"].count()%100)
        high = indexPD["index"].count()
        indexPD.drop(indexPD.index[low:high], inplace=True)

    #Sorting values of Dataframe into ascending order for easier use in later steps
    indexPD.sort_values(by=["index"], inplace=True)

    #Reseting the indexes in the Dataframe and NOT letting the original indexes become a column
    indexPD.reset_index(drop=True, inplace=True)

    #Returning a list of unique indexes sorted in ascending order that will be used in later steps
    return indexPD["index"].tolist()

