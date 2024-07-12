import time
from confluent_kafka import Consumer, KafkaException, KafkaError

conf = {
    'bootstrap.servers': 'kafka:9093',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
}

print("Waiting for consuming...")
time.sleep(3)

consumer = Consumer(conf)

consumer.subscribe(['topic1'])

with open('data.json', 'w') as file:
    file.write( '[' + '\n')
    timeout_counter = 0
    timeout_limit = 5
    first = True
    try:
        while True:
            msg = consumer.poll(1.0)
            
            if msg is None:
                if not(first):
                    timeout_counter += 1
                    if timeout_counter >= timeout_limit:
                        print("No new messages received for 5 seconds, stopping.")
                        break
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
                timeout_counter = 0
                if not first:
                    file.write(',\n')
    
                file.write(msg.value().decode('utf-8'))
                first = False
                file.flush()
                
    finally:
        file.write(']')
        consumer.close()
