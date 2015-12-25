# -*- coding: utf-8 -*-

import jieba
import jieba.posseg as pseg  
import extraDict
from gensim import corpora, models, similarities  
import re

jieba.load_userdict("gossipingDict.txt")
'''
sentence = "台中你是一個三寶三寶飯！"
print "Input：", sentence
words = jieba.cut(sentence, cut_all=False)
print "Output Full Mode："
for word in words:
    print word
'''
listSentence = []
sentence1 = "台中你是一個三寶三寶飯！"
sentence2 = "馬總統蔡英文"
sentence3 = "台灣大學電機系"
sentence4 = "獨立音樂需要大家一起來推廣，歡迎加入我們的行列！"
sentence5 = "我沒有心我沒有真實的自我我只有消瘦的臉孔所謂軟弱所謂的順從一向是我的座右銘"
listSentence.append(sentence1)
listSentence.append(sentence2)
listSentence.append(sentence3)
listSentence.append(sentence4)
listSentence.append(sentence5)


nWordAll = []
for sentence in listSentence:
    words = pseg.cut(sentence)
    nWord = ['']
    for word, flag in words:
        #print word
        if((flag == 'n'or flag == 'v' or flag == 'a' or flag == 'nz' or flag == 'ns' or flag == 'nt' or flag == 'nz') and len(word)>1):
                print word
                nWord.append(word)
    nWordAll.append(nWord)

dictionary = corpora.Dictionary(nWordAll)
corpus = [dictionary.doc2bow(text) for text in nWordAll]

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
lda = models.ldamodel.LdaModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=3)

for i in range(0, 3):
    for j in lda.print_topics(i)[0]:
        print j

corpus_lda = lda[corpus_tfidf]
for doc in corpus_lda:
    print doc

query = u"台灣 大學"
x = query.split( )
query_bow = dictionary.doc2bow(x)
print query_bow

query_lda = lda[query_bow]
print query_lda

a = list(sorted(lda[query_bow], key = lambda x : x[1]))
print a[0]
print a[-1]
#least related
print lda.print_topic(a[0][0])
#most related
print lda.print_topic(a[-1][0])