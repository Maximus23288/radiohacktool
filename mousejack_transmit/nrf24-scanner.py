#!/usr/bin/env python

import time, logging
from lib import common

# Parse command line arguments and initialize the radio
common.init_args('./nrf24-scanner.py')
common.parser.add_argument('-p', '--prefix', type=str, help='Promiscuous mode address prefix', default='')
common.parser.add_argument('-d', '--dwell', type=float, help='Dwell time per channel, in milliseconds', default='100')
common.parse_and_init()

# Parse the prefix addresses
prefix_address = common.args.prefix.replace(':', '').decode('hex')
if len(prefix_address) > 5: 
  raise Exception('Invalid prefix address: {0}'.format(args.address))

# Put the radio in promiscuous mode
common.radio.enter_promiscuous_mode(prefix_address)

# Convert dwell time from milliseconds to seconds 
dwell_time = common.args.dwell / 1000 

# Set the initial channel 
common.radio.set_channel(common.channels[0])

# Sweep through the channels and decode ESB packets in pseudo-promiscuous mode
last_tune = time.time()
channel_index = 0
while True:

  # Increment the channel
  if len(common.channels) > 1 and time.time() - last_tune > dwell_time:
    channel_index = (channel_index + 1) % (len(common.channels))
    common.radio.set_channel(common.channels[channel_index])
    last_tune = time.time()

  # Receive payloads
  value = common.radio.receive_payload()
  if len(value) >= 5:

    # Split the address and payload
    address, payload = value[0:5], value[5:]

    # Log the packet
    logging.info('{0: >2}  {1: >2}  {2}  {3}'.format(
              common.channels[channel_index], 
              len(payload), 
              ':'.join('{:02X}'.format(b) for b in address), 
              ':'.join('{:02X}'.format(b) for b in payload)))

