import random

filename = ["color.txt","mascot.txt"]
list = [[]]*2

for i in range(0,2):
    with open(filename[i]) as infile:
        list[i] = infile.readlines()
        list[i] = [x.strip() for x in list[i]]

numGen = input("Generate how many names? ")
print "Generating", numGen, "names."

for j in range(0,numGen):
    for i in range(0,2):
        listNum = random.randrange(0,len(list[i]))
        print list[i][listNum],
    print
