import csv




with open("csvFiles\ artwork_data.csv", encoding = 'utf-8-sig') as dataFile:
    artReader = csv.DictReader(dataFile)
    line1=next(artReader)
    print(line1) 
