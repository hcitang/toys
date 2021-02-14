import random
#import argparse

#parser = argparse.ArgumentParser(description='Process some integers.')
#parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                    help='an integer for the accumulator')
#parser.add_argument('--file', dest='file', action='store_const',
#                    const=sum, default=max,
#                    help='sum the integers (default: find the max)')

#args = parser.parse_args()
#print(args.accumulate(args.integers))

lines = open('items.txt', 'r').readlines()
items = random.sample(lines, 9)
for item in items:
	print item