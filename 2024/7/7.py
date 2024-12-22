import re

def read_input(name):
	equations = []
	with open(name, 'r') as file:
		for line in file:
			line = line.replace(":", "")
			line = line.replace("\n", "")
			parts = line.split(" ")
			equation = [int(part) for part in parts]
			equations.append(equation)
	return equations

def part1(equations):
	sum = 0
	for equation in equations:
		answer = equation[0]
		old = [equation[1]]
		new = []
		for i in range(2, len(equation)):
			next = equation[i]
			for val in old:
				new.append(val + next)
				new.append(val * next)
				new.append(int(str(val)+str(next)))
			old = new
			new = []
		if answer in old:
			sum += answer
	return sum

if __name__ == "__main__":
	print(test(read_input('input.txt')))
