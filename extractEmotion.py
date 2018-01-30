import pickle
import json

def emotion():
    file1 = open('dictionaryOfScores.pckl', 'rb')
    diction1 = pickle.load(file1)
    counter = 0
    list_1 = []
    list_2 = []
    for item in diction1.values():
        counter+=1
        list_1.append(item["negemo"])
    sum1 = sum(list_1)
    # print sum1
    # print sum2
    avg = (sum1)/counter
    print avg

    list_negemo_below_avg = []
    list_negemo_abv_avg = []
    for item in diction1.items():
        if item[1]["negemo"] <= avg:
            # print type(item[0])
            list_negemo_below_avg.append(item[0])
        else:
            list_negemo_abv_avg.append(item[0])

    print(list_negemo_abv_avg)
    print(list_negemo_below_avg)

    file = open("graphs.json","r")
    scores = open("dictionaryOfScores2.pckl","r")
    dict_of_scores1 = pickle.load(scores)
    dictionary = {}
    for item in file:
        it = json.loads(item)
        for key,value in it.items():
            print key
            # print type(key)# print value
            if int(key) in list_negemo_below_avg or int(key) in list_negemo_abv_avg:
                print "here"
                if int(key) in dict_of_scores1:
                    dictionary[int(key)] = dict_of_scores1[int(key)]

                    # dictionary[int(key)] = dict_of_scores[key]
        else:
            continue
    f1 = open('dictionaryOfGraph.pckl', 'wb')
    pickle.dump(dictionary,f1)

