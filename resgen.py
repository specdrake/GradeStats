import csv
resd = open('resdata.csv', 'r')
wrid = open('resgen.csv', 'w')
rd = csv.reader(resd)
fieldnames = ['no.', 'name', 'batch', 'fec', 'cgpa']
wd = csv.DictWriter(wrid, fieldnames=fieldnames)
flag = False

tot = 0
ograde = 0
apgrade = 0
agrade = 0
bpgrade = 0
bgrade = 0
cgrade = 0
othgrade = 0

fecname = input("Enter the full FEC code : ")
print(fecname + " : ")
for line in rd:
    if line[0] == "Sr.No":
        if line[8] == fecname:
            flag = True
        else:
            flag = False
    if line[0].isnumeric() and flag:
        field = {'no.' : line[0],'name' : line[1], 'batch' : line[2], 'fec' : line[8], 'cgpa' : line[10]}
        wd.writerow(field)
        tot += 1
        if line[8]=="O":
            ograde += 1
        elif line[8] =="A+":
            apgrade+=1
        elif line[8] == "A":
            agrade += 1
        elif line[8] == "B+":
            bpgrade += 1
        elif line[8] == "B":
            bgrade += 1
        elif line[8] == "C":
            cgrade += 1
        else:
            othgrade += 1
resd.close()
wrid.close()
print("O grade : " + str(ograde) + " -> " + str(round ((float(ograde) / tot * 100.0), 2)) + "%")
print("A+ grade : " + str(apgrade) + " -> " + str(round ((float(apgrade) / tot * 100.0), 2)) + "%")
print("A grade : " + str(agrade) + " -> " + str(round ((float(agrade) / tot * 100.0), 2)) + "%")
print("B+ grade : " + str(bpgrade) + " -> " + str(round ((float(bpgrade) / tot * 100.0), 2)) + "%")
print("B grade : " + str(bgrade) + " -> " + str(round ((float(bgrade) / tot * 100.0), 2)) + "%")
print("C grade : " + str(cgrade) + " -> " + str(round ((float(cgrade) / tot * 100.0), 2)) + "%")
print("F/P/I grades : " + str(othgrade) + " -> " + str(round ((float(othgrade) / tot * 100.0), 2)) + "%")
print("Total : " + str(tot))
