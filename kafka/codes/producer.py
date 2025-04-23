from kafka import KafkaProducer
import pymongo
import json
import time

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

client = pymongo.MongoClient("mongodb://localhost:27017/")  
db = client["stockdb"]
collection = db["tweets"]  
cursor = collection.find({})  
for document in cursor:
    tweet = document["tweet"]  
    producer.send('tweets_topic', {'tweets': tweet})
    print(f"Sent to Kafka: {tweet}")
    time.sleep(2)  
producer.close()
