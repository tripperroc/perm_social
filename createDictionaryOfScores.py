import json
import pickle
import youtube.liwc.categories

labels = ["first_person", "second_person", "third_person", "posemo", "negemo", "cognitive", "sensory", "time", "past", "present", "future", "work", "leisure", "swear", "social", "family", "friend", "humans", "anx", "anger",
          "sad", "body", "health", "sexual", "space", "time", "achieve", "home", "money", "relig", "Affect", "cause", "Quant", "Numb", "inhib", "ingest", "motion", "nonfl", "filler", "number_classified_words", "number_words"]


def createDict():
    file = open('training.json')
    #f = open('dict_with_jsonData.pckl', 'rb')
    #set_of_ids = pickle.load(f)
    count = 0
    liwc_by_user = dict()

    for i in file:
        item = json.loads(i)
        count += 1
        user_id = item["user"]["id"]
        try:
            #if user_id in set_of_ids:
            value = getLIWCDictForText(item["text"].encode("utf-8"))
            if user_id in liwc_by_user:
                for keys in liwc_by_user[user_id]:
                    liwc_by_user[user_id][keys] += value[keys]
            else:
                liwc_by_user[user_id] = dict()
                for label in labels:
                    liwc_by_user[user_id][label] = value[label]


        except:
            continue
        if count%10000==0:
            print "processed %d so far" %count

    for user_id in liwc_by_user:
        for value in labels:
            if value != "number_words" or value != "number_classified_words":
                liwc_by_user[user_id][value] = float(liwc_by_user[user_id][value]) / liwc_by_user[user_id]["number_words"]

    f1 = open('dictionaryOfScores.pckl', 'wb')
    pickle.dump(liwc_by_user,f1)

    f1.close()


def getLIWCDictForText(text):
    global labels
    d = dict()
    vals = youtube.liwc.categories.classify(text)
    for i in range(0, len(vals)):
        d[labels[i]] =  vals[i]
    return d


