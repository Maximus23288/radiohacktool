import logging, argparse
from nrf24 import *

channels = []
args = None
parser = None
radio = None

# Initialize the argument parser
def init_args(description):

  global parser
  parser = argparse.ArgumentParser(description,
    formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=50,width=120))
  parser.add_argument('-c', '--channels', type=int, nargs='+', help='RF channels', default=range(2, 84), metavar='N')
  parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output', default=False)
  parser.add_argument('-l', '--lna', action='store_true', help='Enable the LNA (for CrazyRadio PA dongles)', default=False)

# Parse and process common comand line arguments 
def parse_and_init():

  global parser
  global args
  global channels
  global radio

  # Parse the command line arguments 
  args = parser.parse_args()

  # Setup logging
  level = logging.DEBUG if args.verbose else logging.INFO
  logging.basicConfig(level=level, format='[%(asctime)s.%(msecs)03d]  %(message)s', datefmt="%Y-%m-%d %H:%M:%S")

  # Set the channels 
  channels = args.channels
  logging.debug('Using channels {0}'.format(', '.join(str(c) for c in channels)))

  # Initialize the radio 
  radio = nrf24()
  if args.lna: radio.enable_lna()

