import heapq
import sys

# Use min-heap
# Reference: https://docs.python.org/3/library/heapq.html#module-heapq
def populateHeap(h, val, maxLength):
        if len(h) < maxLength or val > h[0]:
                heapq.heappush(h, val)
        if len(h) > maxLength:
                heapq.heappop(h)


def calculateMaxNCalories(lines, n):
        elf_calories = 0
        h = []

        for line in lines:
                l = line.strip()
                if not l:
                        populateHeap(h, elf_calories, n)
                        elf_calories = 0
                else:
                        elf_calories += int(l)

        return sum(heapq.nlargest(n, h))

if __name__ == "__main__":
        if len(sys.argv) != 2:
                print("Please provide input filename")
                exit(1)
        with open(sys.argv[1],  "r") as f:
                lines = f.readlines()
                part_one_result = calculateMaxNCalories(lines, 1)
                part_two_result = calculateMaxNCalories(lines, 3)
                
                print('Part 1:{}\nPart 2:{}'.format(part_one_result, part_two_result))
