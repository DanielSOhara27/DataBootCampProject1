from pandas import DataFrame
from os import path

def exportCSV(amzDataframe):

    try:
        filepath = path.join("..", "..", "datasets", "data", "amz200k_processed.csv")

        amzDataframe.to_csv(filepath, encoding="UTF-8", header=True)

    except:
        print("Something went wrong! Could not export dataframe to CSV")
        raise

    print(f"\n{'-' * 35}\nThe CSV file was saved in Resources/datasets/data folder\nand is called amz200k_processed.csv\n{'-' * 35}")

def splitDatasetJson(filelines, filename, filelocation, size):
    filecounter = 0
    counter = 0
    file_output = list()

    try:
        for line in filelines:

            file_output.append(line)
            counter += 1

            if counter%size == 0:
                filecounter+=1
                counter = 0
                file_output = list()
                exportJson(filelocation=filelocation, filename=filename, filecounter=filecounter, filedata=file_output)
    except:
        print("There was an error splitting the dataset")
        raise

def exportJson(filelocation, filename, filecounter, filedata):
    oldName = filename.split(".")
    newName = oldName[0] + "_"+ str(filecounter) + "." + oldName[1]

    with open(path.join(filelocation, newName), "w+") as fileOutput:

        for line in filedata:
            fileOutput.write(line)
    print(f"Succesfully created file called  {newName}")
