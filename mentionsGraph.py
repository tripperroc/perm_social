import pickle
import os
import json


dict_of_users = dict()
def check():
    f = open('dict_with_jsonData.pckl', 'rb')
    set_of_ids = pickle.load(f)
    f.close()
    findSocialGraph(set_of_ids)

def findSocialGraph(set_of_ids):
    file = open("1year_filtered.json")
    count = 0
    for i in file:
        dict_with_jsonData = json.loads(i)

        if "id" in dict_with_jsonData["user"]:
            if "mention_ids" in dict_with_jsonData:
                list_of_ids = dict_with_jsonData["mention_ids"]
                for value in list_of_ids:
                    if value in set_of_ids:
                        if dict_of_users.has_key(dict_with_jsonData["user"]["id"]):
                            temporary = dict_of_users[dict_with_jsonData["user"]["id"]]
                            if value not in temporary:
                                temporary.append(value)
                            else:
                                continue
                            dict_of_users[dict_with_jsonData["user"]["id"]] = temporary
                        else:
                            dict_of_users[dict_with_jsonData["user"]["id"]]=[value]
        else:
            continue
        count += 1
        if (count % 10000 == 0):
            print "processed %d so far" % count

    with open('graphs.json', 'w') as f:
        json.dump(dict_of_users, f)
