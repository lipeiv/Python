import csv
import pymongo
import redis

from redis import StrictRedis

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['1','lipeiv','18'])