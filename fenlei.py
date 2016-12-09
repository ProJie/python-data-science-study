# coding=utf-8
from __future__ import division
import numpy as np
from collections import defaultdict
from operator import itemgetter
from sklearn.metrics import classification_report
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split


class MachineLearning(object):
	def __init__(self):
		# 加载数据
		dataset = load_iris()
		x = dataset.data
		y = dataset.target
		n_samples, n_features = x.shape
		# 按列取平均值
		attribute_means = x.mean(axis=0)
		# 断言求列平均值之后的列数为feature,也就是shape为(n_feature,)
		assert attribute_means.shape == (n_features,)
		# 比较原始数据和平均值的大小关系,得到布尔数组
		x_d = np.array(x > attribute_means, dtype=int)
		# 随机数种子
		random_state = 14
		# 从样本中随机的按比例选取train data和test data
		self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x_d, y, random_state=random_state, test_size=0.4)
	
	# 训练
	def train(self, x, y_true, feature):
		# 获取样本数(行),特征数目(列)
		n_samples, n_features = x.shape
		# 断言传入的参数特征列的下标大于0小于特征列的数目
		assert 0 <= feature < n_features
		values = set(x[:, feature])
		predictors = dict()
		errors = []
		for current_value in values:
			most_frequent_class, error = self.train_feature_value(x, self.y_train, feature, current_value)
			predictors[current_value] = most_frequent_class
			errors.append(error)
		total_error = sum(errors)
		return predictors, total_error
	
	# 训练特征值
	# 传入训练数据,所属类别,特征列,特征值
	def train_feature_value(self, x, y_true, feature, value):
		class_counts = defaultdict(int)
		for sample, y in zip(x, y_true):
			if sample[feature] == value:
				class_counts[y] += 1
		sorted_class_counts = sorted(class_counts.items(), key=itemgetter(1), reverse=True)
		most_frequent_class = sorted_class_counts[0][0]
		n_samples = x.shape[1]
		error = sum([class_count for class_value, class_count in class_counts.items() if class_value != most_frequent_class])
		return most_frequent_class, error
	
	# 预测
	def predict(self, X_test, model):
		variable = model['variable']
		predictor = model['predictor']
		y_predicted = np.array([predictor[int(sample[variable])] for sample in X_test])
		return y_predicted


# 执行
# 实例化机器学习类
ml = MachineLearning()
# 字典推导式,循环数据点列(特征数目),对每列进行train训练,得到一个预报器
all_predictors = {variable: ml.train(ml.x_train, ml.y_train, variable) for variable in range(ml.x_train.shape[1])}
# 接收error
errors = {variable: error for variable, (mapping, error) in all_predictors.items()}
# 按照错误率进行特征(列)排序,错误最少的提取出来
best_variable, best_error = sorted(errors.items(), key=itemgetter(1))[0]
print("The best model is based on variable {0} and has error {1:.2f}".format(best_variable, best_error))
model = {'variable': best_variable, 'predictor': all_predictors[best_variable][0]}
print(model)
y_predicted = ml.predict(ml.x_test, model)
print(y_predicted)
accuracy = np.mean(y_predicted == ml.y_test) * 100
print("The test accuracy is {:.1f}%".format(accuracy))
print(classification_report(ml.y_test, y_predicted))
