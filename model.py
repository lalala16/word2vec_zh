# -*- coding:utf-8 -*-
#!/usr/bin/env python
# coding:utf-8
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
origin_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
def w(model, target):
	try:
		tup = model.similar_by_word(target)
	except:
		raise
	for i in tup:
		print i[0], ' ', i[1]

def train_embedding():
    print('Load Sentences...')
    cut_dir = origin_path+'/word2vec_zh/cut_data/'
    sentences = LineSentence(cut_dir+'data_chusai_fusai.csv')

    print('Initial Model...')
    model = Word2Vec(sentences, min_count=30, size=200, workers=4)

    model.save('my.model')

def testt_embedding(target):
    cut_dir = origin_path + '/word2vec_zh/'
    model = Word2Vec.load(cut_dir+'my.model')
    w(model, target)
    print model[target]


if __name__ == '__main__':
    train_embedding()
    testt_embedding(u'爱情')

