import pickle
import json
import os

def read():
    """
    Reads in the JSON file and extracts user IDs from the data to create a set of IDs(users) present in the dataset.

    :return:
    """
    set_of_ids = set()
    f = open('../../../Downloads/1year_filtered_sorted.json')
    file1 = open('dictionary_with_jsonData.txt', 'w')
    count = 0
    write_id = open('id.txt','w')
    f1 = open('dict_with_jsonData.pckl', 'wb')


    for i in f:
        dict_with_jsonData = json.loads(i)
        if "id" in dict_with_jsonData["user"]  :
            set_of_ids.add(dict_with_jsonData["user"]["id"])
        else:
            continue
        count +=1
        if (count%10000 == 0):
            print "processed %d so far" % count
        file1.write(str(dict_with_jsonData))
        file1.write(os.linesep)


    for val in set_of_ids:
        write_id.write(str(val))
        write_id.write(os.linesep)


    pickle.dump(set_of_ids, f1)

    f1.close()

    file1.close()
    write_id.close()
