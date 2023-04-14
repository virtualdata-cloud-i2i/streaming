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
""" Kafka consumer to listen streams from somewhere """
import time
import os
from confluent_kafka import Producer

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

args = parser.parse_args(None)

p = Producer({
    'bootstrap.servers': '{}:{}'.format(args.ip, args.port),
})

username = os.environ['USERNAME']

for i in range(3):
    data = f"[{username}]: This is message {i+1}"
    p.produce(args.topic, data.encode('utf-8'))
    time.sleep(1)

p.flush()
