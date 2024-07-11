import json
import time
from confluent_kafka import Producer
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapeme.spiders.spyme import SpymeSpider

from scrapy import signals
from scrapy.signalmanager import dispatcher

p = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

process = CrawlerProcess(get_project_settings())

def run_spider():
    items = []

    def crawler_results(signal, sender, item, response, spider):
        items.append(item)

    
    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    process.crawl(SpymeSpider)
    process.start()

    return items

items = run_spider()

for item in items:
    p.produce('topic1', json.dumps(item).encode('utf-8'), callback=delivery_report)
    p.flush()
    time.sleep(1)
