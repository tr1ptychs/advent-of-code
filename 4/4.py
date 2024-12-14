def get_grid(file):
	grid = []
	with open(file, "r") as input:
		for line in input:
			grid.append(line.strip())
	return grid

def part1(grid):
	count = 0
	for i in range(len(grid[0])):
		for j in range(len(grid)):
			for u in [1, 0, -1]:
				for f in [1, 0, -1]:
					result = ""
					for o in range(4):
						new_i = i + (o * f)
						new_j = j + (o * u)
						if new_i < 0 or new_i >= len(grid[0]) or new_j < 0 or new_j >= len(grid):
							break
						result += grid[new_j][new_i]
					if result == "XMAS":
						count += 1
						# print(f"{i}, {j}, U:{u}, F:{f}, {new_i}, {new_j}")
	return count

def part2(grid):
	count = 0
	for i in range(len(grid[0])):
		for j in range(len(grid)):
			if grid[j][i] != "A":
				continue
			is_x = True
			for u in [1, -1]:
				for f in [1, -1]:
					new_i = i + f 
					new_j = j + u
					if new_i < 0 or new_i >= len(grid[0]) or new_j < 0 or new_j >= len(grid):
						is_x = False
						continue
					result = ""
					for o in [0,1,1]:
						new_i = new_i - (f*o)
						new_j = new_j - (u*o)
						if new_i < 0 or new_i >= len(grid[0]) or new_j < 0 or new_j >= len(grid):
							# print(f"{i}, {j}, U:{u}, F:{f}, {new_i}, {new_j}, out: {result}")
							is_x = False
							break
						result += grid[new_j][new_i]
					if result != "SAM" and result != "MAS":
						# print(f"{i}, {j}, U:{u}, F:{f}, {new_i}, {new_j}, out: {result}")
						is_x = False
					if not is_x:
						break
				if not is_x:
					break
			else:
				count += 1
	return count

if __name__ == "__main__":
	# input.txt demo_input.txt
	grid = get_grid('input.txt')
	print(part2(grid))
