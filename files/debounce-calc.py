#!/usr/bin/env python3
#
#

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--freq", help="fpga clock freq in hz", type=int, default=27000000)
parser.add_argument("-v", "--value", help="debounce value", type=int, default=16)
args = parser.parse_args()

print(f"debounce value : {args.value:9d}")
print(f"     fpga freq : {args.freq:9d} Hz")
print("---------------------------------") 
print(f"          delay: {1000 / (args.freq / (1 << args.value) - 1):9.2f} ms") 


