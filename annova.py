import scipy.stats as stats

group1 = [23, 25, 29, 34, 30]
group2 = [19, 20, 22, 25, 24]
group3 = [15, 18, 20, 21, 17]
group4 = [28, 24, 26, 30, 29]

f_statistic, p_value = stats.f_oneway(group1, group2, group3, group4)

print("One-way ANOVA Results:")
print("F-statistic:", f_statistic)
print("P-value:", p_value)
