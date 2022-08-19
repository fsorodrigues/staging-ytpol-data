def parseA(data):
  data['label'] = data.aggregated_label.fillna('fL')

  data['median_duration'] = data\
    .sort_values(['month','year'])\
    .groupby('label')\
    .rolling(3)\
    ['median_duration']\
    .mean()\
    .reset_index(drop=True)

  return data\
    .dropna(subset='median_duration')\
    .drop('aggregated_label', axis=1)\
    .sort_values(['month','year'])

def parseB(data):
  data['label'] = data.aggregated_label.fillna('fL')

  data['median_user_watchtime'] = data\
    .sort_values(['month','year'])\
    .groupby('label')\
    .rolling(3)\
    ['median_user_watchtime']\
    .mean()\
    .reset_index(drop=True)

  return data\
    .dropna(subset='median_user_watchtime')\
    .drop('aggregated_label', axis=1)\
    .sort_values(['month','year'])