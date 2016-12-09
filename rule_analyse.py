# coding=utf-8
from __future__ import division
import numpy as np
from collections import defaultdict
from operator import itemgetter

dataset_filename = 'affinity_dataset.txt'
x = np.loadtxt(dataset_filename)
n_sample, n_features = x.shape
num_apple_purchase = 0
valid_rules = defaultdict(int)
invalid_rules = defaultdict(int)
num_occurances = defaultdict(int)
data_list = ['面包', '牛奶', '奶酪', '苹果', '香蕉']

for sample in x:
	for premise in range(5):
		if sample[premise] == 0: continue
		num_occurances[premise] += 1
		for conclusion in range(n_features):
			if premise == conclusion: continue
			if sample[conclusion] == 1:
				valid_rules[(premise, conclusion)] += 1
			else:
				invalid_rules[(premise, conclusion)] += 1

support = valid_rules
confidence = defaultdict(float)
for premise, conclusion in valid_rules.keys():
	rule = (premise, conclusion)
	confidence[rule] = valid_rules[rule] / num_occurances[premise]
# print('{0}+{1}={2}'.format(data_list[premise], data_list[conclusion], valid_rules[rule] / num_occurances[premise]))
sorted_confidence = sorted(confidence.items(), key=itemgetter(1), reverse=True)
for i in range(5):
	pr, con = sorted_confidence[i][0]
	print('买{}就会买{}：支持度{},可信度{},总数{}'.format(data_list[pr], data_list[con], support[(pr, con)], confidence[(pr, con)], num_occurances[pr]))
