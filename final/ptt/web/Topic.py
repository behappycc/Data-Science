#coding: utf-8 

import operator
import time
import argparse
import random
from datetime import date
from datetime import datetime
from datetime import timedelta

import pymongo
from pymongo import MongoClient
format = '%Y%m%d'

#summary report of topics in hours
def hotArticle(filename):
    flagSeconds = [3600,21600,86400] #flagHours =  [1, 6, 24]
    list3600Topic = []
    list21600Topic = []
    list86400Topic = []
    with open(filename, 'r') as datafile:
        for i, line in enumerate(datafile):
            if i > 0:
                #data[0]->date, data[1]->title, data[2]->topic
                data = line.split(',')
                now = datetime.today()
                articleTime = datetime.strptime(data[0], '%Y-%m-%d %H:%M:%S')
                deltaTime = now - articleTime
                print deltaTime
                print deltaTime.seconds
                if (deltaTime.seconds < flagSeconds[0]):
                    print data[1] + '3600'
                    list3600Topic.append(data)
                if (deltaTime.seconds < flagSeconds[1]):
                    print data[1] + '21600'
                    list21600Topic.append(data)
                if (deltaTime.seconds < flagSeconds[2]):
                    print data[1] + '86400'
                    list86400Topic.append(data)

        #topicFreq(list3600Topic)
        #topicFreq(list21600Topic)
        #topicFreq(list86400Topic)

def topicFreq(listTopic):
    dictFreq = {}
    for topic in listTopic:
        if topic[2] in dictFreq:
            dictFreq[topic[2]] += 1
        else:
            dictFreq[topic[2]] = 1

    sorted_topic = sorted(dictFreq.items(), key = operator.itemgetter(1), reverse=True)
    return sorted_topic

def topicFreqDB(listTopic):
    dictFreq = {}
    sorted_topic = []
    for topic in listTopic:
        if topic['topic_guess'] in dictFreq:
            dictFreq[topic['topic_guess']] += 1
        else:
            dictFreq[topic['topic_guess']] = 1

    sorted_topic = sorted(dictFreq.items(), key = operator.itemgetter(1), reverse=True)
    #print sorted_topic
    return sorted_topic

def statisticTopic(board):
    client = MongoClient('localhost', 27017)
    #collection = client['Ptt'][board]
    collection = client['Ptt']['Weekarticle' + board]

    flagSeconds = [3600,21600,86400] 
    flagHours =  [1, 7, 30]
    list1Topic = []
    list7Topic = []
    list30Topic = []

    articles = collection.find()
    #2006-01-21 03:32:26
    for article in articles:
        now = datetime.today()
        articleTime = article['date']
        deltaTime = now - articleTime
        #if (deltaTime.days < flagHours[0]):
        #    list1Topic.append(article)
        if (deltaTime.days < flagHours[1]):
            list7Topic.append(article)
        #if (deltaTime.days < flagHours[2]):
        #   list30Topic.append(article)
   
    #print topicFreqDB(list1Topic)

    return list7Topic

def statisticTopicFast(board):
    client = MongoClient('localhost', 27017)
    collection = client['Ptt']['Weekarticle' + board]

    list7Topic = []
    dest_time = datetime.now() - timedelta(days=7)
    articles = collection.find({'date':{'$gt':dest_time}})

    for article in articles:
        list7Topic.append(article)
        
    return list7Topic

#update week article
def updateWeekArticle(board, day):
    client = MongoClient('localhost', 27017)
    collection = client['Ptt'][board]    
    collectionWeek = client['Ptt']['Weekarticle' + board]

    result = collectionWeek.delete_many({})
    print 'delete: ' + str(result.deleted_count)

    dest_time = datetime.now() - timedelta(days=7)
    articles = collection.find({'date':{'$gt':dest_time}})

    for article in articles:
        collectionWeek.insert_one(article)

'''
"message_conut": { # 推文
        "all": 總數,
        "boo": 噓文數,
        "count": 推文數-噓文數,
        "neutral": → 數,
        "push": 推文數
    }
'''

def statisticSchoolTopic(board, place):
    client = MongoClient('localhost', 27017)
    #collectionWeek = client['Ptt'][board] 
    collectionWeek = client['Ptt']['Weekarticle' + board]

    placeArticle = []
    articles = collectionWeek.find()
    for article in articles:
        if article['place'] == place:
            placeArticle.append(article)
            #print article['place'], article['school']
    return placeArticle

def recommendArticle(articles, num):
    listRecommendArticle = []
    for article in articles:
        if article['message_conut']['all'] > num:
            listRecommendArticle.append(article)
    return listRecommendArticle

def randomChoice(articles, num):
    hotArticle = []
    for i in xrange(num):
        hotArticle.append(random.choice(articles))
    return hotArticle

def topicRanking(board):
    print "topic ranking......"
    client = MongoClient('localhost', 27017)
    collection = client['Ptt'][board]

    now_time = datetime.now()
    dest_time = now_time - timedelta(days=7)

    articles = collection.find({"date": {"$gt": dest_time}}).sort('date', pymongo.DESCENDING)
    
    dest_time = now_time - timedelta(days=1)
    data = {}
    data[dest_time] = [0]*50
    for article in articles:
        print article['article_title'], article['topicid']
        if article['date'] < dest_time:
            dest_time = dest_time - timedelta(days=1)
            data[dest_time] = [0]*50
        data[dest_time][article['topicid']] += 1

    topics = []
    with open("topic.txt", "r") as datafile:
        for line in datafile:
            topics.append(line.strip('\n'))

    with open('static/csv/'+board+'_topic_ranking.csv', 'w+') as datafile:
        datafile.write("date," + ",".join(topics) + "\n")
        for day in data:
            datafile.write(day.strftime(format) + "," + ",".join([str(x) for x in data[day]]) + "\n")

def main():
    parser = argparse.ArgumentParser(description='statistic topic')
    parser.add_argument('-b', metavar='BOARD_NAME', help='Board name', required=True)
    args = parser.parse_args()
    board = args.b

    #statisticTopic(board)
    #statisticSchoolTopic(board, u'台北')
    updateWeekArticle(board, 7)
    topicRanking(board)

if __name__ == '__main__':
    main()