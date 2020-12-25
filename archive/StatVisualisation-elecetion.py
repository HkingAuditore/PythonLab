from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
analyzer = SentimentIntensityAnalyzer()


def get_vader_score(sent):
    # Polarity score returns dictionary
    sentiment = analyzer.polarity_scores(sent)
    return sentiment


def get_textblob_score(sent):
    sentiment = TextBlob(sent)
    return sentiment

from textblob import TextBlob
import pandas as pd

chunkSize = 5000
df_chunks = pd.read_csv('hashtag_joebiden.csv', header=0, encoding="utf-8", chunksize=chunkSize,
                        iterator=True)

chunks = []
j = 0

while True:
    try:
        chunk = df_chunks.get_chunk(chunkSize)
        if j % 10 == 0 :
            chunks.append(chunk)
            print(j)
        j += 1
    except StopIteration:
        break
df = pd.concat(chunks, ignore_index=True)

for i in df.index:
    try:
        tweet = df.loc[i, 'tweet']
        textBlob = get_textblob_score(tweet)
        vader = get_vader_score(tweet)
        df.loc[i, 'polarity'] = textBlob.polarity
        df.loc[i, 'subjectivity'] = textBlob.subjectivity
        df.loc[i, 'sentiment'] = vader['compound']
    except:
        continue

print(df)
df.to_csv('hashtag_joebiden.csv', encoding="utf-8", index=False)
