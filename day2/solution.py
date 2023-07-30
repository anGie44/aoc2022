from enum import Enum

class Parts(Enum):
    PART_ONE = 1
    PART_TWO = 2

class Move(object):
    def __init__(self, move, defeats, points):
        self.move = move
        self.defeats = defeats
        self.points = points
    
    def compete(self, other):
        # draw
        if self.move == other.move:
            return self.points + 3
        
        # win
        if self.defeats == other.move:
            return self.points + 6
        
        # lose
        return self.points

class MoveType(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Rock(Move):
    def __init__(self):
        super().__init__(MoveType.ROCK, MoveType.SCISSORS, 1)

class Paper(Move):
    def __init__(self):
        super().__init__(MoveType.PAPER, MoveType.ROCK, 2)

class Scissors(Move):
    def __init__(self):
        super().__init__(MoveType.SCISSORS, MoveType.PAPER, 3)

class DayTwo:
    def __init__(self, rounds):
        self.rounds = rounds
        self.moves = {
            MoveType.SCISSORS: Scissors(),
            MoveType.PAPER: Paper(),
            MoveType.ROCK: Rock(),
        }

    def toMove(self, c):
        if c == "A" or c == "X":
            return Rock()
        if c == "B" or c == "Y":
            return Paper()
        if c == "C" or c == "Z":
            return Scissors()
        
    def toMoveFromResult(self, other, result):
        # lose
        if result == "X":
            return self.moves[other.defeats]
        #draw
        if result == "Y":
            return other

        # win
        if result == "Z":
            r = [ v for (k,v) in self.moves.items() if v.defeats == other.move ]
            if len(r) > 0:
                return r[0]


    def play(self, part):
        points = 0

        for round in self.rounds:
            opponent, me = round.strip().split(' ')
            o = self.toMove(opponent)
            m = None
            if part == Parts.PART_ONE:
                m = self.toMove(me)
            if part == Parts.PART_TWO:
                m = self.toMoveFromResult(o, me)

            if m is not None:
                points += m.compete(o)

        return points


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        d2 = DayTwo(lines)
        p1_result = d2.play(Parts.PART_ONE)
        p2_result = d2.play(Parts.PART_TWO)      
        print('Part 1: {}\nPart 2: {}'.format(p1_result, p2_result))
