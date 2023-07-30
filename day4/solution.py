from enum import Enum

class Parts(Enum):
    PART_ONE = 1
    PART_TWO = 2

class DayFour:
    def __init__(self, lines):
        self.lines = lines

    def fullyContained(self, t1, t2):
        if t1[0] <= t2[0] and t1[1] >= t2[1]:
            return True
        if t2[0] <= t1[0] and t2[1] >= t1[1]:
            return True
        return False
    
    def overlap(self, t1, t2):
        t = (t2, t1) if t1[0] > t2[0] else (t1, t2)

        return t[0][1] >= t[1][0]

    def parseAssignments(self, line):
       return list(map(lambda x: tuple([int(item) for item in x.split('-')]), line.split(',')))
    
    def run(self, t):
        count = 0
        for line in self.lines:
            assignments = self.parseAssignments(line)
            if len(assignments) != 2:
                continue
            ae1, ae2 = assignments[0], assignments[1]

            if t == Parts.PART_ONE:
                if self.fullyContained(ae1, ae2):
                    count += 1
           
            if t == Parts.PART_TWO:
                if self.overlap(ae1, ae2):
                    count +=1
        
        return count
        

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
        d4 = DayFour(lines)
        part_one_result = d4.run(Parts.PART_ONE)
        part_two_result = d4.run(Parts.PART_TWO)
        print('Part 1: {}\nPart 2: {}'.format(part_one_result, part_two_result))
