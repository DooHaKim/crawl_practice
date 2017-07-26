from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen('http://doohaproject.tistory.com/attachment/cfile4.uf@259065335977804F2E3809.csv').read().decode()
dataFile = StringIO(data)
#csvReader = csv.reader(dataFile)
csvDictReader = csv.DictReader(dataFile)

#for row in csvReader:
#    print(row)

print(csvDictReader.fieldnames)
print('----------------')
for row in csvDictReader:
    print(row)