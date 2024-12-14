import re

example = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
with open('input.txt', 'r') as file:
	for line in file:
		txt = line
matches = re.findall("(?:mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", txt)

print(matches)
do = True
total = 0
for match in matches:
	if do:
		if match == "don't()":
			do = False
			continue
		elif match == "do()":
			continue
		else:
			nums = re.findall("\d+", match)
			total += int(nums[0]) * int(nums[1]) 
	else:
		if match == "do()":
			do = True

print(total)
