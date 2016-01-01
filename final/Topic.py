import operator
import time
from datetime import date
from datetime import datetime
from datetime import timedelta

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

        topicFreq(list3600Topic)
        topicFreq(list21600Topic)
        topicFreq(list86400Topic)

def sumArticle(filename):
    day = []
    with open(filename, 'r') as datafile:
        now = datetime.today()
        article = []
        flag = 2
        for i, line in enumerate(datafile):
            if i > 0:              
                data = line.split(',')
                articleTime = datetime.strptime(data[0], '%Y-%m-%d %H:%M:%S')
                deltaTime = now - articleTime
                print str(deltaTime.days) + ' delta'
                if int(deltaTime.days) == flag:
                    print 'hi'
                    article.append(data)
                    print str(article) + 'w'
                else:
                    print 'yo'
                    print topicFreq(article)
                    day.append(topicFreq(article))
                    flag = flag - 1
                    print str(flag) + 'flag'
                    article = []
    print day[0]

def topicFreq(listTopic):
    dictFreq = {}
    for topic in listTopic:
        if topic[2] in dictFreq:
            dictFreq[topic[2]] += 1
        else:
            dictFreq[topic[2]] = 1

    sorted_topic = sorted(dictFreq.items(), key = operator.itemgetter(1), reverse=True)
    return sorted_topic

def main():
    hotArticle('article.csv')
    sumArticle('article.csv')

if __name__ == '__main__':
    main()