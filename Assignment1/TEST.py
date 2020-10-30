import csv

with open("D:\\assignment\python\\file\YuxiJi_RC11_Python\Assignment1\csvFiles\\artwork_data.csv", encoding = 'utf-8-sig') as dataFile:
    artReader = csv.DictReader(dataFile)
    line1=next(artReader)
    print(line1)
