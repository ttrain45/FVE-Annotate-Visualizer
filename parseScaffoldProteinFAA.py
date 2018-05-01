import pandas as pd

def parseFile(path):
    f = open(path, 'r')
    protein = ''
    data = []
    count = 0
    info = []
    secondInfo = []
    for line in f:
        if (line[0] is '>'):
            if count > 0:
                data.append([secondInfo[0][3:],info[0], info[1], info[2], info[3], protein])
            info = line.split(' # ')
            secondInfo = info[4].split(';')
            count += 1
        else:
            protein = protein + line
    data.append([secondInfo[0][3:],info[0], info[1], info[2], info[3], protein])
    df = pd.DataFrame(data=data,columns=['ID','FASTA_ID','START','FINISH','DIRECTION','PROTEIN'])
    return df

