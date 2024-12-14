def read_file(file):
	list = []
	with open(file, 'r') as file:
		for line in file:
			nums = line.split(' ')
			nums[-1] = nums[-1].strip()
			nums = [int(num) for num in nums]
			list.append(nums)
	return list  

if __name__ == "__main__":
	count = 0
	rows = read_file('input.txt')
	for line in rows: 
		increasing = None
		for i in range(len(line) - 1):
			j = i + 1
			diff = line[j] - line[i]
			if not (1 <= diff <= 3 or -1 >= diff >= -3):
				break
			if increasing == None:
				increasing = diff > 0
			elif increasing != (diff > 0):
				break
		else:
			count += 1
			rows.remove(line)
			break
	for line in rows: 
		for x in range(len(line)):
			increasing = None
			new_line = line.copy()
			new_line.pop(x)
			for i in range(len(new_line) - 1):
				j = i + 1
				diff = new_line[j] - new_line[i]
				if not (1 <= diff <= 3 or -1 >= diff >= -3):
					break
				if increasing == None:
					increasing = diff > 0
				elif increasing != (diff > 0):
					break
			else:
				count += 1
				break
	print(count)
				

