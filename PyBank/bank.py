import csv

bankRec = []

fout = open('bankout', 'wt')

with open('budget.csv', newline='') as csvfile:
    linereader = csv.reader(csvfile, delimiter=',')
    for row in linereader:
        print(row)
        bankRec.append(row)

mnthCnt = len(bankRec) 
#print(bankRec)
print("Total Months: {} ".format(mnthCnt-1))

totProf = 0
maxInc = -1000000
maxDec = 1000000
hiChng = -1000000
loChng = 1000000
hiMnth = ''
loMnth = '' 
hiMnthChng = ''
loMnthChng = '' 
totChng = 0
for i in range(1,mnthCnt):
    curRev = int(bankRec[i][1] )
    #print("curRev: {} ".format(curRev))
    totProf = totProf + curRev
    if curRev > maxInc:
        maxInc = curRev
        hiMnth = bankRec[i][0]
    if curRev < maxDec:
        maxDec = curRev
        loMnth = bankRec[i][0]

    if i > 1 :
        curChng = int(bankRec[i][1]) - int(bankRec[i-1][1])
        totChng = totChng + curChng
        print(" {} ${}".format(bankRec[i][0], curChng ))

        if curChng > hiChng:
            hiChng = curChng
            hiMnthChng = bankRec[i][0]
        if curChng < loChng:
            loChng = curChng
            loMnthChng = bankRec[i][0]
    
    

print("Total Profit/Loss: ${}".format(totProf))
#print("Average ")
#print("Greatest Revenue {} {}".format(hiMnth,maxInc))
print("Average Change ${}".format(totChng/(mnthCnt - 2)))
print("Greatest Increase in Profit {} $ {}".format(hiMnthChng,hiChng))
print("Greatest Decrease in Profit {} $ {}".format(loMnthChng,loChng))



print("Total Profit/Loss: ${}".format(totProf), file=fout)
print("Average Change ${}".format(totChng/(mnthCnt - 2)), file=fout)

print("Greatest Increase in Profit {} $ {}".format(hiMnthChng,hiChng), file=fout)
print("Greatest Decrease in Profit {} $ {}".format(loMnthChng,loChng), file=fout)
#print("Greatest Revenue {} ({})".format(hiMnth,maxInc), file=fout)
fout.close()
csvfile.close()
#