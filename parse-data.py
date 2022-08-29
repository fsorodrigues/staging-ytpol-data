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
  {'url': 'updated plots/all_1K/fig1_pnas_mean.csv', 'out_name': 'fig1_pnas_mean.csv'},
  {'url': 'updated plots/all_7K/fig2A_ledwich.csv', 'out_name': 'fig2a_ledwich.csv'},
  {'url': 'updated plots/all_7K/fig2B_ledwich.csv', 'out_name': 'fig2b_ledwich.csv'},
  {'url': 'updated plots/all_7K/fig3A_ledwich.csv', 'out_name': 'fig3a_smoothed.csv'},
  {'url': 'updated plots/all_7K/fig3B_ledwich.csv', 'out_name': 'fig3b_smoothed.csv'},
  {'url': 'outdated plots/Fig4_transition_matrix.txt', 'sep': '\s+', 'out_name': 'fig4.csv'},
  {'url': 'outdated plots/Fig5.txt', 'sep': '\s+', 'out_name': 'fig5.csv'},
  {'url': 'outdated plots/Fig6_heatmap_matrix.txt', 'sep': '\s+', 'out_name': 'fig6.csv'},
  {'url': 'outdated plots/Fig7A_one_sessiontype_60_10.txt', 'sep': '\s+', 'headers': range(0, 15), 'out_name': 'fig7a.csv'},
  {'url': 'outdated plots/Fig7B_meanr.txt', 'headers': range(0, 26), 'out_name': 'fig7b.csv'},
  {'url': 'updated plots/all_7K/table2_ledwich.csv', 'out_name': 'table2.csv'},
  # {'url': 'daily_collections/video_count.csv', 'out_name': 'video_count.csv'},
]
# credentials
creds = {
  "key": AWS_ACCESS_KEY_ID,
  "secret": AWS_SECRET_ACCESS_KEY
}

# iterate over files that need parsing 
for file in datasets:
  # a couple files lack headers, so we have to manually introduce them
  keys = file.keys()
  if ('headers' in keys):
    data = pd.read_csv(
      f's3://{bucket}/youtube-paper/{file["url"]}',
      sep=(file['sep'] if ('sep' in keys) else ','), # handles different separators
      names=[x for x in file['headers']],
      storage_options=creds
    )
  # the majority of files can be loaded more easily
  else:
    data = pd.read_csv(
      f's3://{bucket}/youtube-paper/{file["url"]}',
      sep=(file['sep'] if ('sep' in keys) else ','), # handles different separators
      storage_options=creds
    )

  # find the appropriate parse defined in a different file
  parser = parsers.steps[file["url"]]

  # parse data
  out_data = parser(data)

  # save data to different location
  out_data.to_csv(f's3://{bucket}/youtube-paper/processed/{file["out_name"]}', index=False)