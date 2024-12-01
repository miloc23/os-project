import sys

if len(sys.argv) < 2:
    print("Failed: need to provide input file")
    exit()

file = open(sys.argv[1], "r")

data = dict()


for line in file:
    words = line.split(",")
    if len(words) > 2:
        print("Error")
        exit()
    key = words[0]
    val = int(words[1].rstrip())
    if key not in data:
        data[key] = list()
    data[key].append(val)
    #print(key, val)

for k, v in data.items():
    print(k, v)
