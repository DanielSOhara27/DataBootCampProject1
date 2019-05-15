from ast import literal_eval

def countLines(filepath):
    with open(filepath, "r") as amz20kfile:
        filelines = amz20kfile.readlines()
        amz20kfile.close()
    return filelines

def jsonHeaders(filepath):
    with open(filepath, "r") as jsonfile:
        headers = jsonfile.readline()

    return literal_eval(headers)
