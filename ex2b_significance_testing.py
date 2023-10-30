import pandas as pd
from scipy.stats import ttest_ind
import math
import matplotlib.pyplot as plt


df = pd.read_csv('heart.csv')
df['gender'] = df['sex'].replace({0: 'female', 1: 'male'})
df['hasHeartDisease'] = df['target'].replace({0: 'yes', 1: 'no'})

hasDiseaseCount = df[df['hasHeartDisease'] == 'yes'].groupby("gender").size()

totalCount = df.groupby("gender").size()

p = pd.concat([hasDiseaseCount, totalCount], axis=1)
p.columns = ["heartDiseaseCount", "totalCount"]

p['propHeartDisease'] = p["heartDiseaseCount"] / p["totalCount"]

print(p)

p_men = p.loc['male', 'propHeartDisease']
p_women = p.loc['female', 'propHeartDisease']

n_men = p.loc['male', 'totalCount']
n_women = p.loc['female', 'totalCount']
SE_men = math.sqrt(p_men * (1-p_men) / n_men)
SE_women = math.sqrt(p_women * (1-p_women) / n_women)

SE_diff = math.sqrt(SE_men**2 + SE_women**2)

z = 1.96  # For 95% CI
lower_bound = (p_men - p_women) - z * SE_diff
upper_bound = (p_men - p_women) + z * SE_diff

print(f"95% CI for difference in proportions: ({lower_bound:.4f}, {upper_bound:.4f})")
