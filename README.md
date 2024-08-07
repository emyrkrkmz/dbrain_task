﻿# dbrain_task

## Task 1

* docker-compose.yaml created

```shell
  docker-compose up --build -d
```

* Create topic, "topic1"

```
docker exec -it <docker id> kafka-topics.sh --create --topic topic1 --bootstrap-server localhost:9092 --partitions 5 --replication-factor 1

```


* To list topics, ensured topic was created

```
docker exec -it <docker id> kafka-topics.sh --list --bootstrap-server localhost:9092
```

* To send message

```
docker exec -it <docker id> kafka-console-producer.sh --topic topic1 --bootstrap-server localhost:9092
```

* To listen message

```
docker exec -it <docker id> kafka-console-consumer.sh --topic topic1 --bootstrap-server localhost:9092
```


## Task 2

- Scrapy is used for scrape https://scrapeme.live/shop/ (only page 1)

* Scrapy project started and spider generated

```
cd scrape

Terminal1: python send_data.py
Terminal2: python listen_data.py
```

* Data saved as data.json 

* Api was written with FastAPI


```
cd api

uvicorn main:app --reload
```

* Send a get request to host_url/data

## Task 3

* Dockerfiles created, docker-compose.yaml configured

```
docker-compose build

docker-compose up
```

* For stopping 

```
docker-compose down
```

- Scraped data published from http://localhost:8000/data
