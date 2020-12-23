import json
import matplotlib.pyplot as plt

f1 = open('fecs2k19.json')
f2 = open('year2/fecs2k18.json')
db1 = json.load(f1)
db2 = json.load(f2)

db = {}
db['fecs'] = {}

for k in db1['fecs'].keys():
    db['fecs'][k] = {}
    for grade in db1['fecs'][k].keys():
        db['fecs'][k][grade] = db1['fecs'][k][grade]

for k in db2['fecs'].keys():  
    if k not in db['fecs']:
        db['fecs'][k] = {}
        for grade in db2['fecs'][k].keys():
            db['fecs'][k][grade] = db2['fecs'][k][grade]

    else:
        for grade in db2['fecs'][k].keys():
            db['fecs'][k][grade] += db2['fecs'][k][grade]

for fec in db['fecs'].keys():
    total = 0
    for grade in db['fecs'][fec].keys():
        total += db['fecs'][fec][grade]
    for grade in db['fecs'][fec].keys():
        db['fecs'][fec][grade] = round(db['fecs'][fec][grade] / total * 100.0, 2)

print(db)
colours = ['#f27979', '#ff2200', '#590c00', '#a64b29', '#734939', '#f2c6b6', '#ff8c40', '#663600', '#f2b63d', '#665533', '#c2f200', '#e6f2b6', '#2b331a', '#4b731d', '#60bf6c', '#00ff44', '#00593c', '#00ffee', '#59b3ad', '#003c40', '#00ccff', '#004d73', '#5989b3', '#002e73', '#4d5366', '#7989f2', '#2929a6', '#4400ff', '#180059', '#cc00ff', '#b68fbf','#6b0073', '#f780ff', '#644d66', '#330d2b', '#ff0088', '#731d3f', '#ff0044', '#bf8f9c', '#330d12']
ind = 0
for fec in db['fecs'].keys():
    D = db['fecs'][fec]
    xticks = list(D.keys())
    x = [10 * i for i in range(len(D.keys()))]
    y = D.values()
    plt.xticks(x, xticks)
    plt.scatter(x, y, s = 50, c = colours[ind], label = fec)
    ind += 1
plt.title('Distribution of Letter Grades in FECs')
plt.xlabel('Letter Grades')
plt.ylabel('Percentages')
plt.legend()
plt.show()