import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('censusCrimeClean.csv')

medIncome = df['medIncome']
ViolentCrimesPerPop = df['ViolentCrimesPerPop']
correlation_value = medIncome.corr(ViolentCrimesPerPop)
print(correlation_value)
spearman_correlation_value = medIncome.corr(ViolentCrimesPerPop, method='spearman')
print(spearman_correlation_value)

#  In a scatterplot visualization,
#  the Pearson correlation focuses on linear relationships,
#  whereas the Spearman correlation is about monotonic relationships.
#  If the scatterplot shows a straight-line relationship, 
#  Pearson correlation will be closer to +1 or -1.
#  If the relationship is monotonic but not linear,
#  Spearman correlation will capture this, but Pearson may not.
#  Differences in these correlation values can provide insights into the nature of the relationship between "medIncome" and "ViolentCrimesPerPop".

columns_to_compare = ['population', 'householdsize',  'racepctblack','racePctWhite', 'racePctAsian', 'racePctHisp']

fig, axs = plt.subplots(3, 2, figsize=(15, 15)) 
axs = axs.ravel() 

for i, column in enumerate(columns_to_compare):
    current_column = df[column]
    
    pearson_corr = current_column.corr(ViolentCrimesPerPop)
    spearman_corr = current_column.corr(ViolentCrimesPerPop, method='spearman')
    
    print(f'Correlation between {column} and ViolentCrimesPerPop:')
    print(f'Pearson correlation: {pearson_corr}')
    print(f'Spearman correlation: {spearman_corr}')
    
    axs[i].scatter(df[column], ViolentCrimesPerPop, alpha=0.5)
    axs[i].set_title(f'Scatterplot of {column} and ViolentCrimesPerPop')
    axs[i].set_xlabel(column)
    axs[i].set_ylabel('ViolentCrimesPerPop')
    axs[i].grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()
