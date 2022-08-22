# modules
from pandas import to_datetime, Grouper

def parse(data):
  data['date'] = to_datetime(data['date'], format='%Y-%m-%d')

  return data.set_index('date').groupby(Grouper(freq='MS')).sum()