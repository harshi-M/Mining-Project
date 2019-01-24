def readFile(fileName):
    data = []
    with open(fileName, 'rb') as fileContents:
        lines = [x.decode('utf8').strip() for x in fileContents.readlines()]
    dataAttributes = lines[0].strip().split(",")
    print(len(dataAttributes))
    print("------------")
    for ipLine in lines[1:]:
        data.append(ipLine.strip().split(","))
    print(dataAttributes)
    return [data, dataAttributes]

[data, dataAttributes] = readFile("sampleData.csv")
