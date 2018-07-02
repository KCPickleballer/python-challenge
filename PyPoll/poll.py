import csv
import os

csvpath = os.path.join('.', 'election_data.csv')

pollRec = []
pollDict = {}

voteCnt = 0

fout = open('pollout', 'wt')

#with open('election_data.csv', newline='') as csvfile:
with open(csvpath, newline='') as csvfile:
    linereader = csv.reader(csvfile, delimiter=',')
    for row in linereader:
        canidate = row[2]  
        if canidate != 'canidate':
            
            voteCnt = voteCnt + 1
            
    
            if canidate in pollDict:
                pollDict[canidate] = pollDict[canidate]  + 1
            else:
                pollDict[canidate] = 1
       # pollRec.append(row)

winCnt = 0
winCan = ''
print("Election Results")
print("----------------")
print("Total Votes:  {}".format(voteCnt))
print("----------------")

print("Election Results", file=fout)
print("----------------", file=fout)
print("Total Votes:  {}".format(voteCnt), file=fout)
print("----------------", file=fout)


for canidate in pollDict.keys():
    canVote = pollDict[canidate]
    canPct = (canVote / voteCnt) * 100
    if canVote > winCnt:
        winCnt = canVote
        winCan = canidate
    print("{:15}  {:6.2f}%  ({})".format(canidate+":", canPct, canVote))
    print("{:15}  {:6.2f}%  ({})".format(canidate+":", canPct, canVote), file=fout)

print("Winner: {}".format(winCan)) 
print("Winner: {}".format(winCan), file=fout) 
#print(pollDict)
fout.close()
csvfile.close()

