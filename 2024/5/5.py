def read_input(input):
	with open(input, "r") as file:
		rules = {}
		updates = []
		section = 1
		for line in file:
			if line == '\n':
				section = 2
				continue
			elif section == 1:
				nums = line.split('|')
				if int(nums[0]) not in rules:
					rules[int(nums[0])] = []
				rules[int(nums[0])].append(int(nums[1].strip()))
			else:
				nums = line.split(',')
				nums[-1] = nums[-1].strip()
				for i in range(len(nums)):
					nums[i] = int(nums[i])
				updates.append(nums)
	return (rules, updates)

def get_middle_num(nums):
	return nums[(len(nums)//2)]

def part1(rules, updates):
	total = 0
	for line in updates:
		correct = True
		for num in line:
			if num in rules:
				for after in rules[num]:
					if after in line and line.index(num) > line.index(after):
						correct = False
						break
			if not correct:
				break
		else:
			total += get_middle_num(line)
	return total

def order_line(line, rules):
	for num in line:
		if num in rules:
			for after in rules[num]:
				if after in line and line.index(num) > line.index(after):
					num_index = line.index(num)
					after_index = line.index(after)
					line[num_index] = after
					line[after_index] = num
	unordered = False
	for num in line:
		if num in rules:
			for after in rules[num]:
				if after in line and line.index(num) > line.index(after):
					line = order_line(line, rules)
					unordered = True
					break
			if unordered:
				break
	print(line)
	return line

def part2(rules, updates):
	total = 0
	for line in updates:
		correct = True
		for num in line:
			if num in rules:
				for after in rules[num]:
					if after in line and line.index(num) > line.index(after):
						total += get_middle_num(order_line(line, rules))
						break
			if not correct:
				break
	return total

if __name__ == "__main__":
	rules, updates = read_input("input.txt")
	print(part1(rules, updates))
	print(part2(rules, updates))

