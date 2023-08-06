import re

class TreeNode:
    def __init__(self, filename, filesize):
        self.filename = filename
        self.filesize = filesize
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        self.child = child
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0 
        p = self.parent
        while p :
            p = p.parent
            level += 1
        return level
    
    def get_node_total_value(self):
        if self == None:
            return 0
        elif self.children:
            return self.filesize + sum([ child.get_node_total_value() for child in self.children ])
        else:
            return self.filesize
    
    def filter_directories_by_total_size(self, size, dirs):
        if not self.children:
            return dirs
        
        if self.get_node_total_value() <= size:
            dirs.append(self.get_node_total_value())

        for each in self.children:
            each.filter_directories_by_total_size(size, dirs)
        
        return dirs

    def print_tree(self):
        print('  '*self.get_level() + '|--', end = '')
        print(self.filename, self.get_node_total_value())
        if self.children:
            for each in self.children:
                each.print_tree() 
    
    # Inclusive
    def get_all_directories(self, dirs):
        if not self.children:
            return dirs
        
        dirs.append((self.filename, self.get_node_total_value()))

        for each in self.children:
            each.get_all_directories(dirs)
        
        return dirs

class DaySeven:
    def __init__(self, lines):
        self.root = self.build_tree(lines)

    def build_tree(self, lines):
        root = TreeNode(lines[0].strip().split(' ')[-1], 0)
        
        currNode = root
        for i, line in enumerate(lines[1:]):
            l = line.strip()
            if l == "$ ls":
                # list contents of most recent node
                continue
            elif l.startswith("$ cd"):
                dirName = line.split(' ')[-1].strip()
                match = re.search("[a-zA-Z0-9]+", dirName)
                if not match:
                    # Assume a ".."
                    currNode = currNode.parent
                    continue
                filteredChildren = [c for c in currNode.children if c.filename == dirName]
                currNode = filteredChildren[0]
            else:
                # filenames
                s, n = l.split(' ')
                node = None
                if s == "dir":
                    node = TreeNode(n.strip(), 0)
                else:
                    node = TreeNode(n.strip(), int(s))
                currNode.add_child(node)

        return root
    
    def tree_directories(self):
        return self.root.get_all_directories([])
    
    def root_total_size(self):
        return self.root.get_node_total_value()
    
    def sum_of_all_directories_lte(self, val):
        return sum(self.root.filter_directories_by_total_size(val, []))

    def size_of_smallest_dir_to_delete_for_space(self, freeSpace, requiredFreeSpace):
        dirs = self.root.filter_directories_by_total_size(requiredFreeSpace, [])
        return [dir for dir in sorted(dirs) if dir + freeSpace >= requiredFreeSpace][0]
    


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        d7 = DaySeven(lines)
        part_one_result = d7.sum_of_all_directories_lte(100000)
        print(part_one_result)
        part_two_result = d7.size_of_smallest_dir_to_delete_for_space(70000000-d7.root_total_size(), 30000000)
        print(part_two_result)