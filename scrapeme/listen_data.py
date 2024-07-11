from confluent_kafka import Consumer, KafkaException, KafkaError

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)

consumer.subscribe(['topic1'])

with open('data.json', 'a') as file:
    file.write( '[' + '\n')
    first = True
    try:
        while True:
            msg = consumer.poll(1.0)
            
            if msg is None:
                print("Listening...")
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print('%% %s [%d] reached end at offset %d\n' %
                          (msg.topic(), msg.partition(), msg.offset()))
                else:
                    print(msg.error())
                    break
            else:
                print("Consumed and saved... ")
                
                if not first:
                    file.write(',\n')
    
                file.write(msg.value().decode('utf-8'))
                first = False
                file.flush()
                
    except KeyboardInterrupt:
        file.write(']')
    finally:
        consumer.close()
