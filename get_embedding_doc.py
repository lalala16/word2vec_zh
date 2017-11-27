#!/usr/bin/env python
# coding:utf-8

import numpy as np
import jieba
import jieba
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])

origin_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]


def serperate_text(text_contend='', text2sentence=False):
    text_list = jieba.lcut(text_contend)
    stop_sentence = {u'。', u'！', u'？', u';', u'：', u'（', u'）'}
    if not text2sentence:

        return text_list
    else:
        result = []
        line = []
        for count, word in enumerate(text_list):
            if word in stop_sentence:
                if len(line) > 0:
                    result.append(line)
                line = []
            else:
                is_alpha = True
                for ww in word:
                    if ww < u'\u4e00' or ww > u'\u9fa5':
                        is_alpha = False
                        break
                if not is_alpha:
                    continue
                line.append(word)
        return result


def get_corpus(all_file=[], out_filename='', have_sentence=True):
    out_file = open(out_filename, 'a+')
    for in_filename in all_file:
        in_file = open(in_filename, 'r')

        sentence=[]
        linecount =0

        while(True):
            line = in_file.readline()
            if not line:
                break

            data_line = line.split('\t')
            # assert len(data_line) == 4
            if len(data_line) != 4:
                print 'innormal line:', linecount
                continue
            if data_line[3].strip() == 'POSITIVE':
                linecount += 1
                contend = serperate_text(data_line[1] + '。' + data_line[2], text2sentence=have_sentence)
                if len(contend) == 0:
                    continue
                sentence.extend(contend)
                if len(sentence) > 20000:
                    print len(sentence)
                    for sens in sentence:
                        new_line = ' '.join(sens) + '\n'
                        out_file.write(new_line)
                    sentence = []
        if len(sentence) > 0:
            print len(sentence)
            for sens in sentence:
                new_line = ' '.join(sens) + '\n'
                # print new_line
                out_file.write(new_line)
        in_file.close()
        print '********************************************'
    out_file.close()

if __name__ == '__main__':
    print origin_path
    get_corpus([origin_path + '/chusai_data/train.tsv', origin_path + '/fusai_data/train.tsv'],
               origin_path+'/word2vec_zh/cut_data/data.csv')


