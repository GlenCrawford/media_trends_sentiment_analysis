import argparse

def parse_arguments():
  parser = argparse.ArgumentParser(
    allow_abbrev = False,
    description = 'PyTorch sentiment analysis model of media trends.'
  )

  parser.add_argument(
    '--dataset',
    action = 'store',
    dest = 'dataset',
    default = 'abc_news',
    choices = ['abc_news'],
    help = 'Dataset to use (defaults to abc_news).',
  )

  return parser.parse_args()
