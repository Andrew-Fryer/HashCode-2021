# FILE = 'f.txt'

import random

def getStreet(line):
    data = line.split('\n')[0].split(' ')
    return {'from': int(data[0]), 'to': int(data[1]), 'name': data[2], 'L': int(data[3])}

def getPath(line):
    data = line.split('\n')[0].split(' ')
    return {'P': int(data[0]), 'streets': data[1:]}

def writeln(f, data):
    f.write(str(data))
    f.write('\n')

def getOutput(FILE):
    f = open(FILE, 'r')
    
    D = 0
    I = 0
    S = 0
    V = 0
    F = 0
    data = f.readline()
    data = [int(i) for i in data.split('\n')[0].split(' ')]
    
    D = data[0]
    I = data[1]
    S = data[2]
    V = data[3]
    F = data[4]
    
    streets = []
    paths = []
    for i in range(S):
        streets.append(getStreet(f.readline()))
    for i in range(V):
        paths.append(getPath(f.readline()))
        
    f.close()
    f = open(FILE+'.out', 'w')
    
    writeln(f, I)
    for i in range(I):
        writeln(f, i)
        s = []
        for j in streets:
            if (j['to'] == i):
                s.append(j)
        writeln(f, len(s))
        for j in s:
            writeln(f, "{} {}".format(j['name'], random.randint(1, max(1, int(V/I)))))
    f.close()
    
files = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']
for i in files:
    getOutput(i)