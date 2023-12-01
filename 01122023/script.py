import sys
import re

total = 0

for line in sys.stdin:
	tokens = re.findall(r'\d', line)
	value = (int(tokens[0]) * 10) + int(tokens[-1])
	total += value

print("total: {:d}".format(total))

