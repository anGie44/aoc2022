import heapq
import sys

class DayOne:
        def __init__(self, lines):
                self.lines = lines
                self.h = []
        
        def refreshHeap(self):
                self.h = []
        
        # Use min-heap
        # Reference: https://docs.python.org/3/library/heapq.html#module-heapq
        def populateHeap(self, val, maxLength):
                if len(self.h) < maxLength or val > self.h[0]:
                        heapq.heappush(self.h, val)
                if len(self.h) > maxLength:
                        heapq.heappop(self.h)
        
        def calculateMaxNCalories(self,  n):
                elf_calories = 0
        
                for line in self.lines:
                        l = line.strip()
                        if not l:
                                self.populateHeap(elf_calories, n)
                                elf_calories = 0
                        else:
                                elf_calories += int(l)
        
                return sum(heapq.nlargest(n, self.h))

if __name__ == "__main__":
        if len(sys.argv) != 2:
                print("Please provide input filename")
                exit(1)
        with open(sys.argv[1],  "r") as f:
                lines = f.readlines()
                d1 = DayOne(lines)
                part_one_result = d1.calculateMaxNCalories(1)
                d1.refreshHeap()
                part_two_result = d1.calculateMaxNCalories(3)
                print('Part 1: {}\nPart 2: {}'.format(part_one_result, part_two_result))
