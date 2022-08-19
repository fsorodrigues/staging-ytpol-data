# modules
from pandas import Categorical

# local modules
import enforce_order

def parse(data):
  data = data.reset_index()
  data['from'] = Categorical(data['index'], enforce_order.preferred_order)

  return data.drop('index', axis=1).sort_values("from")