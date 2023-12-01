import sys
import re

total = 0

# Yes I can put the numbers in an array, but whatever
def token_to_num(token):
	match token:
		case "one":
			return 1
		case "two":
			return 2
		case "three":
			return 3
		case "four":
			return 4
		case "five":
			return 5
		case "six":
			return 6
		case "seven":
			return 7
		case "eight":
			return 8
		case "nine":
			return 9
		case _:
			return int(token)

for line in sys.stdin:
	tokens = re.findall(r'(\d|one|two|three|four|five|six|seven|eight|nine)', line)
	value = (token_to_num(tokens[0]) * 10) + token_to_num(tokens[-1])
	#print("{}:{}{}:{}{}:{}".format(value, token_to_num(tokens[0]), token_to_num(tokens[-1]), tokens[0], tokens[-1], line))
	total += value

print("total: {:d}".format(total))

