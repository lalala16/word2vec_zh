# -*- coding:utf-8 -*-
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

import os
origin_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
def w(model, target):
	try:
		tup = model.similar_by_word(target)
	except:
		raise
	for i in tup:
		print(i[0], ' ', i[1])

def train_embedding():
    print('Load Sentences...')
    cut_dir = origin_path+'/word2vec_zh/cut_data/'
    sentences = LineSentence(cut_dir+'data_small.csv')

    print('Initial Model...')
    model = Word2Vec(sentences, min_count=30, size=200, workers=4)

    model.save('my.model')

def test_embedding(target):
    cut_dir = origin_path + '/word2vec_zh/'
    model = Word2Vec.load(cut_dir+'my.model')
    w(model, target)


if __name__ == '__main__':
    test_embedding(u'爱情')
