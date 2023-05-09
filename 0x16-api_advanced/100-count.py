#!/usr/bin/python3

import operator
import requests


def count_w(word, title):
    l = title.split()
    n = 0
    for w in l:
        if (w.upper() == word.upper()):
            n = n + 1
    return n


def count_words(subreddit, word_list, nexT="", count={}):
    if (len(count.keys()) == 0):
        n = []
        for key in word_list:
            n.append(0)
        count = dict(zip(word_list, n))
    headers = {'User-agent': 'Alb4tr02'}
    url = "https://www.reddit.com/r/"+subreddit+"/hot/.json"+nexT
    req = requests.get(url, headers=headers)
    req1 = requests.get("https://www.reddit.com/r/"+subreddit, headers=headers)
    if (req1.status_code != 200):
        return
    json = req.json()
    if ('error' in json.keys()):
        return
    for post in json['data']['children']:
        title = post['data']['title']
        for word in word_list:
            count[word] = count[word] + count_w(word, title)
    if (json['data']['after'] is not None):
        return count_words(subreddit, word_list, "?after=" +
                           json['data']['after'], count)
    else:
        aux = sorted(count.items(), key=operator.itemgetter(0), reverse=False)
        aux1 = {}
        flag = True
        lk = []
        lv = []
        for element in aux:
            lk.append(element[0])
            lv.append(element[1])
        aux1 = dict(zip(lk, lv))
        aux = sorted(aux1.items(), key=operator.itemgetter(1), reverse=True)
        for element in aux:
            if (element[1] != 0):
                print("{}: {}".format(element[0], element[1]))
                flag = False
        if (flag):
            print("")
        return
