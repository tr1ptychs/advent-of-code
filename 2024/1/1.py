def read_file(file):
	left = []
	right = []
	with open(file, 'r') as file:
		for line in file:
			nums = line.split('   ')	
			left.append(int(nums[0]))
			right.append(int(nums[1].strip()))
	left = sorted(left)
	right = sorted(right)
	return left, right 

list


if __name__ == "__main__":
	left, right = read_file('day1input.txt')
	sum = 0
	for left_num in left:
		num_count = 0
		for right_num in right:
			if left_num == right_num:
				num_count += 1
		sum += left_num * num_count
	print(sum)
