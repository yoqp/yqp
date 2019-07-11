# coding: utf-8
import codecs
import MeCab
import re, pprint
mecab = MeCab.Tagger()

with open('mecab.txt') as f:
    text = f.read()
    node = mecab.parseToNode(text)
    words = {}
    while node:
#        #if node.feature.split(',')[0] == '名詞':
        if node.surface in words:
            words[node.surface] += 1
        else:
            words[node.surface] = 1
        node = node.next
    for tpl in sorted(words.items(), key=lambda x: x[1], reverse=True)[0:5]:
        print(type(tpl))
        print(tpl)
