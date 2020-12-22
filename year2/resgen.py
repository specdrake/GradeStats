import csv
import json
resd = open('resdata.csv', 'r')
rd = csv.reader(resd)

db = {}
db['fecs'] = {}

grades = ['O', 'A+', 'A', 'B+', 'B', 'C', 'P']
flag = False
ind = 0

subjectPrefix = 'FEC'

def findFecIndex(line):
    for i in range(len(line)):
        if line[i][:len(subjectPrefix)] == subjectPrefix:
            return i, line[i], True
    return -1, '', False

for line in rd:
    if line[0] == "Sr.No":
        ind, fecname, flag = findFecIndex(line)
    if line[0].isnumeric() and flag:
        if not fecname in db['fecs']:
            db['fecs'][fecname] = {
                'O'  : 0,
                'A+' : 0,
                'A'  : 0,
                'B+' : 0,
                'B'  : 0,
                'C'  : 0,
                'P'  : 0,
                'N'  : 0, 
            }
        if line[ind] in grades: 
            db['fecs'][fecname][line[ind]] += 1
        else:
            db['fecs'][fecname]['N'] += 1
resd.close()

db['fecs'] = {key: val for key, val in sorted(db['fecs'].items(), key = lambda ele: int(ele[0][len(subjectPrefix):]))} 

with open('fecs2k18.json', 'w') as outfile:
    json.dump(db, outfile)