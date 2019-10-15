from collections import Counter

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    automakers = [item['automaker'] for item in data if item['year'] == year]
    print(automakers)
    automakers_counter = Counter(automakers)
    print (automakers_counter.most_common(1)[0][0])
