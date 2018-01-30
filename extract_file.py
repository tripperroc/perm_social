import json
import os
import youtube.liwc.categories
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

labels = ["first_person", "second_person", "third_person", "posemo", "negemo", "cognitive", "sensory", "time", "past", "present", "future", "work", "leisure", "swear", "social", "family", "friend", "humans", "anx", "anger",
          "sad", "body", "health", "sexual", "space", "time", "achieve", "home", "money", "relig", "Affect", "cause", "Quant", "Numb", "inhib", "ingest", "motion", "nonfl", "filler", "number_classified_words", "number_words"]

dict_with_jsonData = dict()
dict_with_scores = dict()
dict_for_hist = dict()

def readText():
    f = open('1year_temp.json')
    file = open('myfile_temp.txt', 'w')
    count = 0
    for i in f:
        item = json.loads(i)
        dict_with_jsonData["text"] = item.get("text")
        dict_with_jsonData["user_ID"] = item.get("user")

        #print dict_with_jsonData["user_ID"]["id"]

        #Obtain Categories with specific values of the LIWC scores for each LIWC ITem
        values = getLIWCDictForText(dict_with_jsonData["text"].encode('utf-8'))
        # print values

        # current_user_id = dict_with_jsonData["user_ID"]["id"]
        # tweet_count = dict_with_jsonData["user_ID"]["statuses_count"]
        # dict_for_hist[current_user_id]=tweet_count
        # if dict_with_scores.has_key(current_user_id):
        #     temporary = dict_with_scores[current_user_id]
        #     for val in temporary.keys():
        #         temporary[val] = temporary[val] + values[val]
        #     dict_with_scores[current_user_id] = temporary
        # else:
        #     dict_with_scores[current_user_id]= values
        #
        # count +=1
        # if (count%1000 == 0):
        #     print "processed %d so far" % count

    # PASS the values to the dictionary and directly append the values to the dictionary.
    # file.write(my_dict["text"].encode('utf-8'))
    # file.write(os.linesep)
    # print dict1
    # file.write(str(dict_with_scores))
    # file.close()
    return dict_with_scores

def getLIWCDictForText(text):
    global labels
    d = dict()
    vals = youtube.liwc.categories.classify(text)
    for i in range(0, len(vals)):
        d[labels[i]] = 100 * vals[i] / float(vals[40])
    return d

def findAvg(dict_with_scores):
    '''
    :param dict_with_scores:
    :return:
    '''
    count = 0
    first_person = second_person = third_person = posemo = negemo = 0
    cognitive = sensory = time = past = present = future = work = 0
    leisure = swear = social = family = friend = humans = anx = 0
    anger = sad = body = health = sexual = space = time = achieve = 0
    home = money = relig = affect = cause = quant = numb = inhib = ingest = motion = nonfl = filler = 0
    number_classified_words = number_words = 0
    result = 0
    for item in dict_with_scores.items():
        if (count%1000 == 0):
            print "processed %d so far" % count
        first_person += item[1]["first_person"]
        second_person += item[1]["second_person"]
        third_person += item[1]["third_person"]
        posemo += item[1]["posemo"]
        negemo += item[1]["negemo"]
        cognitive += item[1]["cognitive"]
        sensory += item[1]["sensory"]
        time += item[1]["time"]
        past += item[1]["past"]
        present += item[1]["present"]
        future += item[1]["future"]
        work += item[1]["work"]
        leisure += item[1]["leisure"]
        swear += item[1]["swear"]
        social += item[1]["social"]
        family += item[1]["family"]
        friend += item[1]["friend"]
        humans += item[1]["humans"]
        anx += item[1]["anx"]
        anger += item[1]["anger"]
        sad += item[1]["sad"]
        body += item[1]["body"]
        health += item[1]["health"]
        sexual += item[1]["sexual"]
        space += item[1]["space"]
        time += item[1]["time"]
        achieve += item[1]["achieve"]
        home += item[1]["home"]
        money += item[1]["money"]
        relig += item[1]["relig"]
        affect += item[1]["Affect"]
        cause += item[1]["cause"]
        quant += item[1]["Quant"]
        numb += item[1]["Numb"]
        inhib += item[1]["inhib"]
        ingest += item[1]["ingest"]
        motion += item[1]["motion"]
        nonfl += item[1]["nonfl"]
        filler += item[1]["filler"]
        number_classified_words += item[1]["number_classified_words"]
        number_words += item[1]["number_words"]
        count += 1

    # Finds users with LIWC scores whose "negemo" is below average negemo or above average negemo
    negemo_result = negemo/len(dict_with_scores)

    greater_than_equalnegemo = dict()
    lesser_negemo = dict()

    for item in dict_with_scores.items():
        if item[1]["negemo"] < negemo_result:
            lesser_negemo[item[0]] = item[1]
        else:
            greater_than_equalnegemo[item[0]] = item[1]

    print lesser_negemo
    print "********Break*********"
    print greater_than_equalnegemo

    # print len(lesser_negemo)
    # print len(greater_than_equalnegemo)

def histogram():

    '''
    This method displays the histogram of the tweets of users.
    :return:
    '''


    plt.hist(dict_for_hist.values(),range=[0,100000],bins=100, color='g')
    plt.xlabel("Number of total tweets by an individual user")
    plt.ylabel("Number of users")
    plt.title("Users v/s Tweets Count")
    plt.show()


def main():
    dict_with_scores = readText()
    findAvg(dict_with_scores)
    histogram()

if __name__ == '__main__':
    main()