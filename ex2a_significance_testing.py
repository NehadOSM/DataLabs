import pandas as pd
from scipy.stats import ttest_ind
import math
import matplotlib.pyplot as plt

df = pd.read_csv('heart.csv')

df['gender'] = df['sex'].replace({0: 'female', 1: 'male'})
df['hasHeartDisease'] = df['target'].replace({0: 'yes', 1: 'no'})
grouped = df.groupby('hasHeartDisease')['trestbps'].agg(['mean', 'std'])
print(grouped)


group1 = df[df['hasHeartDisease'] == 'yes']['trestbps']
group2 = df[df['hasHeartDisease'] == 'no']['trestbps']

t_stat, p_value = ttest_ind(group1, group2)
print(f"t-statistic: {t_stat}, p-value: {p_value}")


n1, n2 = len(group1), len(group2)
s1, s2 = group1.std(), group2.std()
pooled_std = math.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))
cohens_d = (group1.mean() - group2.mean()) / pooled_std
print(f"Cohen's d: {cohens_d}")


fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 8), sharey=True)

# Boxplot
df.boxplot(column='trestbps', by='hasHeartDisease', ax=ax[0, 0])
ax[0, 0].set_title('Boxplot of trestbps by Heart Disease Status')
ax[0, 0].set_xlabel('Has Heart Disease')
ax[0, 0].set_ylabel('trestbps')

# Histogram
df[df['hasHeartDisease'] == 'yes']['trestbps'].hist(ax=ax[0, 1], label='Yes', alpha=0.7)
df[df['hasHeartDisease'] == 'no']['trestbps'].hist(ax=ax[0, 1], label='No', alpha=0.7)
ax[0, 1].set_title('Histogram of trestbps by Heart Disease Status')
ax[0, 1].legend()

plt.tight_layout()
plt.show()

