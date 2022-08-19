def parseA(data):
  data.user_percent = data.user_percent / 100
  data['label'] = data.aggregated_label.fillna('fL')
  
  return data.drop('aggregated_label', axis=1).sort_values(['month','year'])

def parseB(data):
  data.percentage_duration = data.percentage_duration / 100
  data.label = data.aggregated_label
  
  return data.drop('aggregated_label', axis=1).sort_values(['month','year'])
