import pandas as pd

ad_clicks = pd.read_csv ('ad_clicks.csv')

# print(ad_clicks.groupby('utm_source').user_id.count().reset_index())

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
# print(ad_clicks.head())

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
clicks_pivot = clicks_by_source.pivot(columns = 'is_click', index = 'utm_source', values = 'user_id').reset_index()

clicks_pivot['percent_clicked'] = clicks_pivot[True] /  (clicks_pivot[True] + clicks_pivot[False])

print(ad_clicks.groupby('experimental_group').user_id.count())

A_B = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

A_B_pivot = A_B.pivot(columns ='is_click', index= 'experimental_group', values = 'user_id').reset_index()

# print(A_B_pivot)
A_B_pivot['percent_click'] = A_B_pivot[True] /  (A_B_pivot[True] + A_B_pivot[False])
# print(A_B_pivot)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

# print(a_clicks.head())

a_per_day_click = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
a_per_day_click_pivot = a_per_day_click.pivot(columns = 'is_click', index = 'day', values = 'user_id').reset_index()


a_per_day_click_pivot['percent_click'] = a_per_day_click_pivot[True] / (a_per_day_click_pivot[True] + a_per_day_click_pivot[False])

print(a_per_day_click_pivot)

b_per_day_click = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
b_per_day_click_pivot = b_per_day_click.pivot(columns = 'is_click', index = 'day', values = 'user_id').reset_index()


b_per_day_click_pivot['percent_click'] = b_per_day_click_pivot[True] / (b_per_day_click_pivot[True] + b_per_day_click_pivot[False])

print(b_per_day_click_pivot)
