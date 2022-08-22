# modules
from pandas import Categorical

# local modules
import enforce_order

def parse(data):
  data.columns = data.columns.str.replace('IDW', 'AW')
  data.label = data.label.str.replace('IDW', 'AW')

  data = data.rename(
    columns={ 
      f'monthly_cat_duration{x}': x 
      for x in enforce_order.preferred_order 
    }
  )

  data['cluster'] = Categorical(data['label'], enforce_order.preferred_order)

  return data.drop('label', axis=1).sort_values("cluster")