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
