
f = open('a.txt', 'r')

def tryInt(x):
    try:
        return int(x)
    except:
        return str(x)

l = [[tryInt(y) for y in x.split()] for x in f.readlines()]
[D, I, S, V, F] = l[0] #[int(x) for x in l[0]]

for line in l[1:S+1]:
    [B, E, streetName, L] = line

for line in l[S+1:S+1+V]:
    P = line[0]
    path = line[1:]


print(D, I, S, V, F, l)