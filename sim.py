class Street:
    def __init__(self, leng, time_green):
        self.queue = []
        self.len = leng
        self.timeLeft = 0
        self.time_green = time_green

class Car:
    def __init__(self, path):
        self.path = path
        self.distanceLeft = 0

intersections = {}
streets = {}

def tryInt(x):
    try:
        return int(x)
    except:
        return str(x)

f = open('input_files/a.txt', 'r')
l = [[tryInt(y) for y in x.split()] for x in f.readlines()]
[D, I, S, V, F] = l[0]
for line in l[1:S+1]:
    [B, E, streetName, L] = line
    if(intersections.get(E) is None):
        intersections[E] = []
    s = Street(L, 0)
    intersections[E].append(s)
    streets[streetName] = s
for line in l[S+1:S+1+V]:
    P = line[0]
    path = line[1:]
    streets[path[0]].queue.append(Car(path))

f = open('output_files/a.txt.out', 'r')
l = [[tryInt(y) for y in x.split()] for x in f.readlines()]
numIntersections = l.pop(0)[0]
for i in range(numIntersections):
    intersectionId = l.pop(0)[0]
    numStreets = l.pop(0)[0]
    for j in range(numStreets):
        [streetName, timeGreen] = l.pop(0)
        streets[streetName].time_green = timeGreen
        if(j == 0):
            # first street in schedule at intersection
            streets[streetName].timeLeft = timeGreen

score = 0
for timeStep in range(D): # for each time step
    # configure lights (timeLeft)
    for i in intersections.values():
        for sInd in range(len(i)):
            s = i[sInd]
            if(s.timeLeft > 1):
                s.timeLeft -= 1
            elif(s.timeLeft == 1):
                s.timeLeft = 0
                nextStreet = i[(sInd+1) % len(i)]
                nextStreet.timeLeft = nextStreet.time_green

    for streetName in streets.keys():
        s = streets[streetName]
        queueCopy = [x for x in s.queue]
        for cInd in range(len(queueCopy)):
            c = queueCopy[cInd]
            if(s.timeLeft > 0 and s.queue[0].distanceLeft == 0):
                if(len(c.path) > 1):
                    # move car to next street
                    s.queue.remove(c)
                    nextStreet = streets[c.path[0]]
                    nextStreet.queue.append(c)
                    c.path.pop(0)
                    c.distanceLeft = nextStreet.len
                else:
                    # remove car (it's done)
                    s.queue.remove(c) # todo: should remove at start of last street
                    score += F + (D - timeStep)
            if(c.distanceLeft > 0):
                # move car along
                c.distanceLeft -= 1

print(score)