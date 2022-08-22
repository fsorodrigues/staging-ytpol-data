# modules
from pandas import to_datetime, pivot_table

col_map = {
  'aggregated_label': 'cluster',
  1: 'HP', 
  2: 'Search', 
  3: 'User/Channel', 
  4: 'Video', 
  5: 'Ext URL', 
  6: 'Other', 
}

def parse(data):
  data['date'] = to_datetime(data.apply(lambda x: f'{x["year"]}-{x["month"]}', axis=1), yearfirst=True)

  data = data[(data['date'] == data['date'].max())]

  data['percentge'] = data['percentge'] / 100

  pivoted = pivot_table(
    data.fillna('fL'),
    values='percentge',
    index='aggregated_label',
    columns='cases',
    aggfunc=sum
  )\
  .reset_index()\
  .rename(col_map, axis=1)

  return pivoted