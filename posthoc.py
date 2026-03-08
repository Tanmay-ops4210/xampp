from statsmodels.stats.multicomp import pairwise_tukeyhsd

group1 = [23, 25, 29, 34, 30]
group2 = [19, 20, 22, 25, 24]
group3 = [15, 18, 20, 21, 17]
group4 = [28, 24, 26, 30, 29]

all_data = group1 + group2 + group3 + group4

group_labels = (
    ['Group1'] * len(group1) +
    ['Group2'] * len(group2) +
    ['Group3'] * len(group3) +
    ['Group4'] * len(group4)
)

tukey_results = pairwise_tukeyhsd(all_data, group_labels)

print("Tukey-Kramer Post-Hoc Test Results:")
print(tukey_results)
