# This file is now deprecated and no longer needed,
# but it will be left as reference of past trials and
# errors. Wrote a 4 line solution to this problem
#
#
#

import ast
import json
import re


def cleanLine(amzJsonLine):

    #Functions are defined below
    start = indexOfReviewText(amzJsonLine)
    end = indexOfHelpful(amzJsonLine)

    cleanJsonLine = fixReviewText(amzJsonLine=amzJsonLine, indexOfReview=start, indexOfHelpful=end)

    return createJson(cleanJsonLine)





def indexOfReviewText(amzJsonLine):
    reviewPattern = re.compile(",\s*['|\"]\s*reviewText\s*['|\"]\s*:")

    return re.search(reviewPattern, amzJsonLine).end()



def indexOfHelpful(amzJsonLine):
    regexPattern = re.compile(",\s*['|\"]\s*helpful\s*['|\"]\s*:")

    return re.search(regexPattern, amzJsonLine).start()



def indexOfSummaryText(amzJsonLine):
    summaryPattern = re.compile("['|\"]\s*summary\s*['|\"]\s*['|\"]")

    return re.search(summaryPattern, amzJsonLine).end()



def indexOfCategoryID(amzJsonLine):
    categoryIDPattern = re.compile("['|\"]\s*,\s*['|\"]categoryID\s*['|\"]")

    return re.search(categoryIDPattern, amzJsonLine).start()



def fixReviewText(amzJsonLine, indexOfReview, indexOfHelpful):

    #Step 1, Extract dirty substring causing trouble and delete trailing whitespaces
    dirtyStr = amzJsonLine[indexOfReview : indexOfHelpful]
    dirtyStr.strip()

    #Step 2, Check to see if the substring needs cleaning
    if(dirtyStr[0]!='"' and dirtyStr[-1]!='"'):
        dirtyStr = ' ' + json.dumps(dirtyStr[ 2 : len(dirtyStr)-1 ])

    #Step 3, Create new string with correct Json Syntax for reviewText value
    cleanStr = amzJsonLine[:indexOfReview] + str(dirtyStr) + amzJsonLine[indexOfHelpful:]

    return cleanStr

def fixSummaryText(amzJsonLine, indexOfSummary, indexOfCategoryID):

    #Step 1, Extract dirty substring causing trouble and delete trailing whitespaces
    dirtyStr = amzJsonLine[indexOfSummary : indexOfCategoryID]
    dirtyStr.strip()

    #Step 3, Create new string with correct Json Syntax for reviewText value
    cleanStr = amzJsonLine[:indexOfSummary] + str(dirtyStr) + amzJsonLine[indexOfCategoryID:]

    return cleanStr



def cleanCategoriesList(amzJsonList):
    # Finally, turn the list of lists called Category into a proper dictionary
    startList = re.search(re.compile("\[\s*\["), amzJsonList).end() - 2
    endList = re.search(re.compile("\]\s*\]"), amzJsonList).start() + 2
    categoryLists = ast.literal_eval(amzJsonList[startList:endList])
    categoryDict = {}
    for x in range(len(categoryLists)):
        categoryDict[str(x)] = categoryLists[x]

    return amzJsonList.replace(amzJsonList[startList:endList], json.dumps(categoryDict))




def createJson(cleanJsonLine):

    # auxJsonLine is defined with pattern1 and will contain a copy of string being parsed


    # Looking for {' with or without spaces and replacing for {"
    pattern1 = re.compile("\{\s*'")
    auxJsonLine = re.sub(pattern1, '{"', cleanJsonLine)

    # Looking for attributes (nHelpful, outOf, unixReviewTime, rating, categoryID)
    for att in ['nHelpful', 'outOf', 'unixReviewTime', 'rating', 'categoryID', 'summary', 'itemID', 'categories', 'price']:
        regex = f"['|\"]\s*{att}\s*['|\"]"
        pattern = re.compile(regex)
        auxJsonLine = re.sub(pattern, f"\"{att}\" ", auxJsonLine)

    # Looking for '} with or without spaces and replacing for "}
    pattern2 = re.compile("'\s*\}")
    auxJsonLine = re.sub(pattern2, '"}', auxJsonLine)

    # Looking for [' with or without spaces and replacing for ["
    pattern3 = re.compile("\[\s*'")
    auxJsonLine = re.sub(pattern3, '["', auxJsonLine)

    # Looking for '] with or without spaces and replacing for "]
    pattern4 = re.compile("'\s*]")
    auxJsonLine = re.sub(pattern4, '"]', auxJsonLine)

    # Looking for ',' with or without spaces and replacing for " , "
    pattern5 = re.compile("['|\"]\s*,\s*['|\"]")
    auxJsonLine = re.sub(pattern5, '" , "', auxJsonLine)

    # Looking for ':' with or without spaces and replacing for " : "
    pattern6 = re.compile("['|\"]\s*:\s*['|\"]")
    auxJsonLine = re.sub(pattern6, '" : "', auxJsonLine)

    # Looking for ':{ with or without spaces and replacing for " : {
    pattern7 = re.compile("'\s*:\s*{")
    auxJsonLine = re.sub(pattern7, '" : {', auxJsonLine)

    # Looking for }, ' with or without spaces and replacing for }, "
    pattern8 = re.compile("}\s*,\s*'")
    auxJsonLine = re.sub(pattern8, '}, "', auxJsonLine)

    # Cleaning the list of lists called categories
    auxJsonLine = cleanCategoriesList(auxJsonLine)



    return auxJsonLine
