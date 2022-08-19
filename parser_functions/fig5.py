# modules
from functools import reduce

def parse(data):
  nulls = data[~data['LowerBound'].notnull()].to_dict(orient='list')['Mean']
  data = data[data['LowerBound'].notnull()].copy()

  nulls_list = []
  scenario_list = [4,3,2]
  
  for item in nulls:
    for i in scenario_list:
      nulls_list.append(item)

  data['cluster'] = nulls_list
  data['scenario'] = scenario_list * len(nulls)

  return data.rename(columns={
    'Mean': 'mean', 'LowerBound': 'lower-bound', 'UpperBound': 'upper-bound'
  })
  