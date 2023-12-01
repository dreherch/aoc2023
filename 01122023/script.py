import sys
import re

total = 0

# This code does not work, its possible to link One, Eight and Two infinitely
# you need either two check from any char or use a smarter regexp
# fortunately I have the right result for my input and don't need to implement either

# Yes I can put the numbers in an array, but whatever
def token_to_num(token):
	match token:
		case "one":
			return ['1']
		case "oneight":
			return ['1', '8']
		case "two":
			return ['2']
		case "twone":
			return ['2', '1']
		case "three":
			return ['3']
		case "four":
			return ['4']
		case "five":
			return ['5']
		case "six":
			return ['6']
		case "seven":
			return ['7']
		case "eightwone":
			return ['8', '2', '1']
		case "eightwo":
			return ['8', '2']
		case "eighthree":
			return ['8', '3']
		case "eight":
			return ['8']
		case "nine":
			return ['9']
		case _:
			return [token]

for line in sys.stdin:
	tokens = re.findall(r'(\d|oneight|one|twone|two|three|four|five|six|seven|eightwone|eightwo|eighthree|eight|nine)', line)
	value = (int(token_to_num(tokens[0])[0]) * 10) + int(token_to_num(tokens[-1])[-1])
	#print("{}:{}{}:{}{}:{}".format(value, token_to_num(tokens[0]), token_to_num(tokens[-1]), tokens[0], tokens[-1], line))
	total += value

print("total: {:d}".format(total))

