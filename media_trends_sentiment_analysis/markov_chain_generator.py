import pandas as pd
import markovify

INPUT_FILE_PATH = 'data/abc_news.csv' # Relative to the project root directory.
COLUMN_NAMES = ['Date', 'Headline']

def generate(year = None):
  dataframe = load_dataframe()

  # Optionally narrow to a specific year.
  if year is not None:
    dataframe = dataframe[dataframe['Date'].dt.year == year]

  markov_model = markovify.NewlineText(dataframe.Headline, state_size = 2)

  # Print 10.
  for i in range(10):
    print(markov_model.make_sentence())

def load_dataframe():
  return pd.read_csv(
    INPUT_FILE_PATH,
    header = 0,
    names = COLUMN_NAMES,
    parse_dates = ['Date'],
    infer_datetime_format = True
  )
