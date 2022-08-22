# # modules
from pandas import melt

# local modules
import enforce_order

def parseA(data):
  data['cluster'] = [x for x in enforce_order.preferred_order if x != 'fL']

  return melt(data, id_vars='cluster', var_name='index', value_name='fraction')

def parseB(data):
  data['cluster'] = enforce_order.preferred_order

  return melt(data, id_vars='cluster', var_name='length', value_name='mean')