from enum import Enum
import functools

class PriorityType(Enum):
    COMPARTMENT = 1
    GROUP = 2

class DayThree:
    def __init__(self, lines):
        self.lines = lines
    
    def sharedItem(self, t, lines):
        if t == PriorityType.COMPARTMENT:
            line = lines[0]
            idx = int(len(line)/2)
            p1, p2 = line[0:idx], line[idx:]

            return set(p1).intersection(p2).pop()
        if t == PriorityType.GROUP:
            s = set(lines[0])

            for line in lines[1:]:
                s = s.intersection(line)
                     
            return s.pop()
    
    def priority(self, item):
        if item.isupper():
            return ord(item) - ord("A") + 27
        if item.islower():
            return ord(item) - ord("a") + 1
        return 0

    def run(self, t):
        if t == PriorityType.COMPARTMENT:
            return functools.reduce(lambda a, b: a+b, [self.priority(self.sharedItem(PriorityType.COMPARTMENT, [line])) for line in self.lines])
        if t == PriorityType.GROUP:
            # group of 3
            list_of_three = list(zip(self.lines, self.lines[1:], self.lines[2:]))[::3]
            d = [ list(tt) for tt in list_of_three ]
            return functools.reduce(lambda a, b: a+b, [self.priority(self.sharedItem(PriorityType.GROUP, group)) for group in d])



if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        d3 = DayThree(lines)
        part_one_result = d3.run(PriorityType.COMPARTMENT)
        part_two_result = d3.run(PriorityType.GROUP)
        print('Part 1: {}\nPart 2: {}'.format(part_one_result, part_two_result))