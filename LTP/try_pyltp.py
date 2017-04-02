# -*- coding: utf-8 -*-
from pyltp import SentenceSplitter
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
from pyltp import Parser

# 功能1：分句
sents = SentenceSplitter.split('元芳你怎么看？我就趴窗口上看呗！')  # 分句
print '\n'.join(sents)

# 功能2：分词
segmentor = Segmentor()  # 初始化实例
segmentor.load('./ltp_data/cws.model')  # 加载模型
words = segmentor.segment('广州火车站是一个奇特的地方，王小明和李想正是因为这个原因爱上了它。')  # 分词
word2 = segmentor.segment('我们同学间有结婚的和尚结婚的人，不过这不影响我们间的感情。')  # 分词
print ' '.join(words)
print ' '.join(word2)
word2 = list(word2)
print ' '.join(word2)
print type(word2)
segmentor.release()  # 释放模型

# 功能3：词性标注
postagger = Postagger() # 初始化实例
postagger.load('./ltp_data/pos.model')  # 加载模型
postags = postagger.postag(words)  # 词性标注
print ' '.join(postags)
postagger.release()  # 释放模型

# 功能4：命名实体识别
recognizer = NamedEntityRecognizer() # 初始化实例
recognizer.load('./ltp_data/ner.model')  # 加载模型
netags = recognizer.recognize(words, postags)  # 命名实体识别
print ' '.join(netags)
recognizer.release()  # 释放模型

# 功能5：依存句法分析
parser = Parser() # 初始化实例
parser.load('./ltp_data/parser.model')  # 加载模型
arcs = parser.parse(words, postags)  # 句法分析
print " ".join("%d:%s" % (arc.head, arc.relation) for arc in arcs)
parser.release()  # 释放模型