from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen('http://doohaproject.tistory.com/attachment/cfile4.uf@259065335977804F2E3809.csv').read().decode()
dataFile = StringIO(data)
dataFile2 = StringIO(data)
csvReader = csv.reader(dataFile)
csvDictReader = csv.DictReader(dataFile2)

for row in csvReader:
    print(row)

#csvDictReader 사용시 fieldname을 분리할 수 있음.
print(csvDictReader.fieldnames)
for row in csvDictReader:
    print(row)