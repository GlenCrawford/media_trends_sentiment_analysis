import pandas as pd

DATASET_DIRECTORY_PATH = 'data/' # Relative to the project root directory.

def load_dataset(dataset_name):
  dataset_load_methods = {
    'abc_news': load_abc_news_dataset
  }

  try:
    return dataset_load_methods[dataset_name]()
  except KeyError:
    raise ValueError('Unrecognized dataset name: ' + str(dataset_name))

def load_abc_news_dataset():
  return pd.read_csv(
    DATASET_DIRECTORY_PATH + 'abc_news.csv',
    header = 0,
    names = ['Date', 'Headline'],
    parse_dates = ['Date'],
    infer_datetime_format = True
  )
