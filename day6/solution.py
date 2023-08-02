from queue import Queue

class DaySix():
    def markerPosition(self, line, nchar):
        q = Queue()

        for idx, c in enumerate(list(line)):
            if c not in q.queue:
                q.put(c)  
            else:
                # pop off all elements until we reach c, inclusive
                while c in q.queue:
                    q.get(c)
                q.put(c)

            if q.qsize() == nchar:
                return idx + 1            

        # no position found
        return -1
                    
            

if __name__ == "__main__":
    with open("input.txt", "r") as  f:
        line = f.readline()
        d6 = DaySix()
        part_one_result = d6.markerPosition(line, 4)
        part_two_result = d6.markerPosition(line, 14)
        print('Part 1: {}\nPart 2: {}'.format(part_one_result, part_two_result))