import copy
def read_grid(name):
	grid = []
	with open(name, 'r') as file:
		for line in file:
			row = []
			for char in line.strip():
				row.append(char)
			grid.append(row)
	return grid

def starting_coordinates(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == '^':
				return (i, j)

def rotate(vector):
	if vector == (-1, 0):
		return (0, 1)
	if vector == (0, 1):
		return (1, 0)
	if vector == (1, 0):
		return (0, -1)
	if vector == (0, -1):
		return (-1, 0)

def get_next(position, direction):
	return (position[0] + direction[0], position[1] + direction[1])

def inside_grid(position, grid):
	return 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0])

def char(grid, position):
	return grid[position[0]][position[1]]

def part1(grid):
	visited = set()
	position = starting_coordinates(grid)
	direction = (-1, 0)
	visited.add(position)
	next = get_next(position, direction)
	while inside_grid(next, grid):
		if char(grid, next) == '#':
			direction = rotate(direction)
		else:
			position = next
			visited.add(position)
		next = get_next(position, direction)
	return len(visited)

def dir_print(dir):
	if dir == (0, 1):
		return '>'
	if dir == (0, -1):
		return '<'
	if dir == (1, 0):
		return 'v'
	if dir == (-1, 0):
		return '^'
	if dir == 0:
		return 'O'

def print_grid(grid, visited):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if (i, j) in visited:
				print(dir_print(visited[(i, j)][-1]), end='')
			else:
				print(grid[i][j], end='')
		print()
	print()


def loops(grid, position, direction, visited):
	# it's slow but it works
	vis = copy.deepcopy(visited)
	obstacle = get_next(position, direction)
	if obstacle in vis:
		return False
	vis[obstacle] = [0]
	pos = position
	dir = rotate(direction)
	next = get_next(pos, dir)
	while inside_grid(next, grid):
		if next in vis and dir in vis[next]: 
			# print_grid(grid, vis)
			return True
		if char(grid, next) == '#' or next == obstacle:
			dir = rotate(dir)
		else:
			pos = next
		if pos not in vis:
			vis[pos] = []
		if dir not in vis:
			vis[pos].append(dir)
		next = get_next(pos, dir)
	return False


def part2(grid):
	visited = {}
	obstructions = set()
	start = starting_coordinates(grid)
	direction = (-1, 0)
	position = start
	next = get_next(position, direction)
	while inside_grid(next, grid):
		if char(grid, next) == '#':
			direction = rotate(direction)
		else:
			if loops(grid, position, direction, visited):
				obstructions.add(next)
				position = next
			position = next
		if position not in visited:
			visited[position] = []
		visited[position].append(direction)
		next = get_next(position, direction)
	return len(obstructions)

if __name__ == "__main__":
	print(part1(read_grid('input.txt')))
	print(part2(read_grid('input.txt')))
