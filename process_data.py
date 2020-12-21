import pandas as pd
import numpy as np
from sklearn import datasets

# dataset = pd.read_csv("癌症风险数据集.csv",usecols=['behavior_eating','behavior_personalHygine'])
dataset = datasets.load_breast_cancer()
