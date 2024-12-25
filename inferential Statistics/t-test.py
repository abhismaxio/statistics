from scipy.stats import ttest_ind

group1= [23,21,25,30,28]
group2= [20,21,19,24,21]

t_stat, p_val = ttest_ind(group1,group2)

print(f"T-statistic: {t_stat}, P-value: {p_val}")