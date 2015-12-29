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
sentence6 = "台灣大學獨立音樂"
listSentence.append(sentence1)
listSentence.append(sentence2)
listSentence.append(sentence3)
listSentence.append(sentence4)
listSentence.append(sentence5)
listSentence.append(sentence6)

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

sentences = [['first', 'sentence'], ['second', 'sentence']]
model = models.Word2Vec(sentences, min_count=1)

abc = [[u'台灣', u'大學', u'電機'], [u'獨立', u'音樂', u'需要', u'大家']]
model = models.Word2Vec(abc, min_count=1)
model.save('word2vec_model.model')

#print model[u'台灣']
sim = model.most_similar(positive=[u'台灣', u'大學'])
for s in sim:  
    print "word:%s,similar:%s " %(s[0],s[1])

for w in model.most_similar(u'台灣'):
    print w[0], w[1], 'hi'


'''
class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()
sentences = MySentences('/some/directory') # a memory-friendly iterator
model = gensim.models.Word2Vec(sentences)
'''