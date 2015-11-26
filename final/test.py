#encoding=utf-8
import jieba
import extradict

jieba.load_userdict("gossipingdict.txt")

sentence = "台中你是一個三寶三寶飯！"
print "Input：", sentence
words = jieba.cut(sentence, cut_all=False)
print "Output Full Mode："
for word in words:
    print word