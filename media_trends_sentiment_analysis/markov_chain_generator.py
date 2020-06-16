import pandas as pd
import markovify

def generate(dataframe, year = None):
  # Optionally narrow to a specific year.
  if year is not None:
    dataframe = dataframe[dataframe['Date'].dt.year == year]

  markov_model = markovify.NewlineText(dataframe.Headline, state_size = 2)

  # Print 10.
  for i in range(10):
    print(markov_model.make_sentence())
