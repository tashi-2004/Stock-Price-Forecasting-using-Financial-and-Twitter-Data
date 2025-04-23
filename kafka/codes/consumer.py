from kafka import KafkaConsumer
from textblob import TextBlob
import json

consumer = KafkaConsumer('tweets_topic',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

for message in consumer:
    tweet = message.value['tweet']
    sentiment = analyze_sentiment(tweet)
    print(f"Tweets: {tweet} -> Sentiment: {sentiment}")
