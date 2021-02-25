G = "green"
R = "red"

class Street:
    def __init__(self, leng, time_green):
        self.queue = []
        self.len = leng
        self.light = R
        self.timeLeft = 0
        self.time_green = time_green

class Car:
    def __init__(self, path):
        self.path = path

intersections = {}
streets = {}

def tryInt(x):
    try:
        return int(x)
    except:
        return str(x)

f = open('a.txt', 'r')
l = [[tryInt(y) for y in x.split()] for x in f.readlines()]
[D, I, S, V, F] = l[0]
for line in l[1:S+1]:
    [B, E, streetName, L] = line
    if(intersections.get(E) is None):
        intersections[E] = {}
    s = Street(L, 0)
    intersections[E][streetName] = s
    streets[streetName] = s
for line in l[S+1:S+1+V]:
    P = line[0]
    path = line[1:]
    streets[path[0]].queue.append(Car(path))

f = open('a.txt.out', 'r')
l = [[tryInt(y) for y in x.split()] for x in f.readlines()]
numIntersections = l.pop(0)[0]
for i in range(numIntersections):
    intersectionId = l.pop(0)[0]
    numStreets = l.pop(0)[0]
    for j in range(numStreets):
        [streetName, timeGreen] = l.pop(0)
        streets[streetName].time_green = timeGreen

print(streets)