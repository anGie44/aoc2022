import heapq
import sys

class DayOne:
	def __init__(self, lines):
		self.lines = lines

	def populateHeap(self, h, val, maxLength):
		if len(h) < maxLength or val > h[0]:
			heapq.heappush(h, val)
		if len(h) > maxLength:
			heapq.heappop(h)

	def calculateMaxNCalories(self, n):
		elf_calories = 0
		h = []

		for line in self.lines:
			l = line.strip()
			if not l:
				self.populateHeap(h, elf_calories, n)
				elf_calories = 0
			else:
				elf_calories += int(l)
		
		self.populateHeap(h, elf_calories, n)
	
		return sum(heapq.nlargest(n, h))

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Please provide input filename")
		exit(1)
	with open(sys.argv[1],  "r") as f:
		lines = f.readlines()
		d1 = DayOne(lines)
		part_one_result = d1.calculateMaxNCalories(1)
		part_two_result = d1.calculateMaxNCalories(3)
		print('Part 1: {}\nPart 2: {}'.format(part_one_result, part_two_result))
