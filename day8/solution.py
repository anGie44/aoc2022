import functools
import heapq
from time import time

class DayEight():
    def __init__(self, data):
        self.matrix = [ [int(c) for c in line.strip()] for line in data ]
        self.n_rows = len(self.matrix)
        self.n_columns = len(self.matrix[0])
        self.n_visible = (self.n_columns * 2) + 2 * (self.n_rows - 2) 
        self.interior_tree_coords = [(x,y) for x in range(1, self.n_columns-1) for y in range(1, self.n_rows-1)]

    def is_visible_left(self, x, y):
        row = self.matrix[y]
        for col in range(x-1, -1, -1):
            if row[col] >= row[x]:
                return False
        return True
    
    def is_visible_right(self, x, y):
        row = self.matrix[y]

        for col in range(x+1, self.n_columns):
            if row[col] >= row[x]:
                return False

        return True
    
    def is_visible_top(self, x, y):
        for row in range(y-1, -1, -1):
            if self.matrix[row][x] >= self.matrix[y][x]:
                return False
        return True
    
    def is_visible_bottom(self, x, y):
        for row in range(y+1, self.n_rows):
            if self.matrix[row][x] >= self.matrix[y][x]:
                return False
        return True

    def is_visible(self, coordinate):
        x, y = coordinate[0], coordinate[1]

        # look Left, Top, Right, Bottom
        # visible if ALL trees between it and an edge are shorter
        
        return self.is_visible_left(x,y) or self.is_visible_right(x, y) \
                or self.is_visible_top(x, y) or self.is_visible_bottom(x, y)
    
    def total_visible_trees(self):
        return self.n_visible + [self.is_visible(coordinate) for coordinate in self.interior_tree_coords].count(True) 
    
    def populate_scores_heap(self, h, val):
        if len(h) < 1 or val > h[0]:
            heapq.heappush(h, val)
        if len(h) > 1:
            heapq.heappop(h)

    def viewing_distance_left(self, x, y):
        count = 0
        row = self.matrix[y]

        for col in range(x-1, -1, -1):
            if row[col] < row[x]:
                count += 1
            elif row[col] >= row[x]:
                count += 1
                break
        return count
    
    def viewing_distance_right(self, x, y):
        count = 0
        row = self.matrix[y]

        for col in range(x+1, self.n_columns):
            if row[col] < row[x]:
                count += 1
            elif row[col] >= row[x]:
                count += 1
                break
        return count
    
    def viewing_distance_top(self, x, y):
        count = 0
        
        for row in range(y-1, -1, -1):
            if self.matrix[row][x] < self.matrix[y][x]:
                count += 1
            elif self.matrix[row][x] >= self.matrix[y][x]:
                count += 1
                break
        return count
    
    def viewing_distance_bottom(self, x, y):
        count = 0
        for row in range(y+1, self.n_rows):
            if self.matrix[row][x] < self.matrix[y][x]:
                count += 1         
            elif self.matrix[row][x] >= self.matrix[y][x]:
                count += 1
                break
        return count

    def scenic_score(self, coordinate):
        x, y = coordinate[0],  coordinate[1]
        viewing_distances = []

        viewing_distances.append(self.viewing_distance_left(x,y))
        viewing_distances.append(self.viewing_distance_right(x,y))
        viewing_distances.append(self.viewing_distance_top(x,y))
        viewing_distances.append(self.viewing_distance_bottom(x,y))

        return functools.reduce(lambda a, b: a*b, viewing_distances)
                        
    def highest_scenic_score(self):
        h = []

        for coordinate in self.interior_tree_coords:
            self.populate_scores_heap(h, self.scenic_score(coordinate))            
        
        return sum(heapq.nlargest(1, h))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        d8 = DayEight(lines)

        time_start = time()
        part_one_result = d8.total_visible_trees()
        time_end = time()
        duration = time_end - time_start
        print(f'Part 1 Total Time: {duration} seconds')
        print(f'Part 1 Result: {part_one_result}')  

        time_start = time()
        part_two_result = d8.highest_scenic_score()
        time_end = time()
        duration = time_end - time_start
        print(f'Part 2 Total Time: {duration} seconds')
        print(f'Part 2 Result: {part_two_result}')  