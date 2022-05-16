import numpy as np

#sequence
sequence="ATTCTTA"
sequenceTwo="TTTCT"

#create matris
mainMatrix=np.zeros(len(sequence)+1,len(sequenceTwo)+1)
matchMatrix=np.zeros(len(sequence),len(sequenceTwo))
#match dismatch,gap

match=1
dismatch=-1
gap=-2

#fill matris

for i in range(len(sequence)):
    for j in range(len(sequenceTwo)):
        if sequence[i]==sequenceTwo[j]:
            matchMatrix[i][j]= match
        else:
            matchMatrix[i][j]=dismatch

for i in range(len(sequence)):
    mainMatrix[i][0]=i*gap
for i in range(len(sequenceTwo)):
    mainMatrix[0][i]=i*gap


for i in range(len(sequence)):
    for j in range(len(sequenceTwo)):
        mainMatrix[i][j]=max(mainMatrix[i-1][j-1]+matchMatrix[i-1][j-1],
                             mainMatrix[i-1][j]+gap,
                             mainMatrix[i][j-1]+gap)

alignment=""
alignmentTwo=""

sequenceLen=len(sequence)
sequenceTwoLen=len(sequenceTwo)


