# modules
from os import getenv
import pandas as pd
  
# local modules
# import enforce_order
import parsers

# global vars
AWS_ACCESS_KEY_ID = getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = getenv('AWS_SECRET_ACCESS_KEY')
bucket = getenv('bucket')

# datasets
datasets = [
  # {'url': 'youtube-paper/updated plots/all_7K/fig2A_ledwich.csv'},
  # {'url': 'youtube-paper/updated plots/all_1K/fig1_pnas_mean.csv'},
  # {'url': 'youtube-paper/updated plots/all_7K/fig2B_ledwich.csv'},
  # {'url': 'youtube-paper/updated plots/all_7K/fig3A_ledwich.csv'},
  # {'url': 'youtube-paper/updated plots/all_7K/fig3B_ledwich.csv'},
  # {'url': 'youtube-paper/outdated plots/Fig4_transition_matrix.txt', 'sep': '\s+'},
  {'url': 'youtube-paper/outdated plots/Fig5.txt', 'sep': '\s+'},
]
creds = {
  "key": AWS_ACCESS_KEY_ID,
  "secret": AWS_SECRET_ACCESS_KEY
}

for file in datasets:
  data = pd.read_csv(
    f's3://{bucket}/{file["url"]}',
    sep=(file['sep'] if file['sep'] else ','),
    storage_options=creds
  )

  parser = parsers.steps[file["url"]]

  print(parser(data))
  