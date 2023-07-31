import re
import functools
from enum import Enum
from copy import deepcopy

class Parts(Enum):
    PART_ONE = 1
    PART_TWO = 2

class DayFive():
    def __init__(self, lines):
        self.lines = lines

    def parseInput(self):
        idx = 0
        stacks = None
        pattern = "\[[A-Z]\]"

        for i, line in enumerate(self.lines): 
            match = re.search(pattern, line)
            if match:
                for m in re.finditer(pattern, line):
                    column = int(m.start()/(len(m.group(0))+1))

                    if not stacks:
                        stacks = [[] for _ in range(0, column+1)]

                    for _ in range(len(stacks), column+1):
                        stacks.append([])
                    
                    stacks[column].append(re.sub("\[|\]", "", m.group(0)))
            elif line.startswith("move"):
                idx = i
                break
            
        return stacks, self.lines[idx:]
            

    def crateDance(self, part, stacks, directions):
        for direction in directions:
            match = re.search(r"(\b\d+).+(\b\d+).+(\b\d+)", direction)
            if match:
                if len(match.groups()) < 3:
                    continue
                n = int(match.group(1))
                fromCol = int(match.group(2)) - 1
                toCol = int(match.group(3)) - 1

                extractedCrates = [stacks[fromCol].pop(0) for _ in range(0, n) if len(stacks[fromCol]) > 0]
               
                if part == Parts.PART_ONE:
                    # FIFO
                    for crate in extractedCrates:
                        stacks[toCol].insert(0, crate)

                elif part == Parts.PART_TWO:
                    # LIFO
                    stacks[toCol] = extractedCrates + stacks[toCol]

        return stacks
   
    def topStackCrates(self, stacks):
        return functools.reduce(lambda a, b: a+b, [s.pop(0) for s in stacks])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        d5 = DayFive(lines)
        s1, d1 = d5.parseInput()
        s2, d2 = deepcopy(s1), deepcopy(d1)
        rs1 = d5.crateDance(Parts.PART_ONE, s1, d1)
        part_one_result = d5.topStackCrates(rs1)
        rs2 = d5.crateDance(Parts.PART_TWO, s2, d2)
        part_two_result = d5.topStackCrates(rs2)
        print("Part 1: {}\nPart 2: {}".format(part_one_result, part_two_result))
