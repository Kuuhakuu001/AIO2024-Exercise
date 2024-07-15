import pandas as pd

df = pd.read_csv('advertising.csv')
data = df.to_numpy()

max_sales = df['Sales'].max()
max_sales_index = df['Sales'].idxmax()
print(max_sales, max_sales_index)
# Q15: Answer C

mean_tv = df['TV'].mean()
print(mean_tv)
# Q16: Answer B

sales_ge_20 = df[df['Sales'] >= 20].shape[0]
print(sales_ge_20)

mean_radio_sales_ge_15 = df[df['Sales'] >= 15]['Radio'].mean()
print(mean_radio_sales_ge_15)
# Q18: Answer B

mean_newspaper = df['Newspaper'].mean()
sum_sales_newspaper_gt_mean = df[df['Newspaper'] > mean_newspaper]['Sales'].sum()
print(sum_sales_newspaper_gt_mean)
# Q19: Answer C

mean_sales = df['Sales'].mean()
scores = ['Good' if x > mean_sales else 'Bad' if x < mean_sales else 'Average' for x in df['Sales']]
print(scores[7:10])
# Q20: Answer C

mean_sales = df['Sales'].mean()
closest_to_mean_sales = df.iloc[(df['Sales'] - mean_sales).abs().argsort()[:1]]['Sales'].values[0]
scores_closest = ['Good' if x > closest_to_mean_sales else 'Bad' if x < closest_to_mean_sales else 'Average' for x in df['Sales']]
scores_closest[7:10]
