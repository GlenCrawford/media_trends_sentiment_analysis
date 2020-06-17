from media_trends_sentiment_analysis import *

def main():
  ARGUMENTS = Arguments.parse_arguments()

  dataframe = Dataset.load_dataset(ARGUMENTS.dataset)

if __name__ == '__main__':
  main()
