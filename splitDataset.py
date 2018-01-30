import json
import random
import os


def splitData():

    file = open('1year_filtered.json')
    file1 = open("training.json","w+")
    file2 = open("testing.json", "w+")
    file3 = open("validation.json", "w+")
    count = 0
    for record in file:
        item = json.loads(record)
        r = random.random()
        # Value of r ranges from 0 to 1

        if r<=0.33:
            json.dump(item, file1)
            file1.write(os.linesep)

        elif r>0.33 and r<=0.66:
            json.dump(item,file2)
            file2.write(os.linesep)

        else:
            json.dump(item, file3)
            file3.write(os.linesep)

        count += 1

        if count % 100000 == 0:
            print "processed %d so far" % count
