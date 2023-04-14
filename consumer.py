#!/usr/bin/env python
# Copyright 2023 Julien Peloton
# Author: Julien Peloton
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" A simple Kafka Consumer running on a Kafka Cluster """
from confluent_kafka import Consumer, KafkaError

import argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    '-ip', type=str, default='127.0.0.0',
    help="Server IP"
)
parser.add_argument(
    '-port', type=int, default=9092,
    help="Port"
)
parser.add_argument(
    '-topic', type=str, default='test_topic',
    help="Name of the topic where we want to publish data"
)
parser.add_argument(
    '-groupid', type=str, default='test',
    help="Group ID name"
)


args = parser.parse_args(None)


c = Consumer({
    'bootstrap.servers': '{}:{}'.format(args.ip, args.port),
    'group.id': args.groupid,
    'auto.offset.reset': 'earliest'
})

c.subscribe([args.topic])

while True:
    msg = c.poll(1.0)

    if msg is None:
        print('No message...')
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))

c.close()
