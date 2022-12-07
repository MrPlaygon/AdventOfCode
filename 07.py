# Learning Classes
import timeit


class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent

    def get_size(self):
        return self.size

    def to_string(self, indentation):
        s = "   " * indentation + "- FILE " + self.name + " " + str(self.size) + "\n"
        return s


class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.items = []
        self.hasDir = False
        self.parent = parent

    def __str__(self):
        return self.name + "-" + str(self.get_size())

    def __repr__(self):
        return self.name + "-" + str(self.get_size())

    def add_item(self, item):
        self.items.append(item)
        if type(item == Dir):
            self.hasDir = True

    def has_dir(self):
        return self.hasDir

    def get_dirs(self, recursive):
        dirs = []
        for i in self.items:
            if type(i) == Dir:
                dirs.append(i)
                if recursive:
                    dirs.extend(i.get_dirs(True))
        return dirs

    def get_dir(self, name):
        for i in self.items:
            if i.name == name:
                return i

    def get_size(self):
        size = 0
        for i in self.items:
            size += i.get_size()
        return size

    def to_string(self, indentation):
        s = "   " * indentation + "- DIR " + self.name + "\n"
        for i in self.items:
            s += i.to_string(indentation + 1)
        return s


# Parsing

root = Dir("/", None)
curr = root

with open("07.txt") as f:
    for line in f:
        line = line.rstrip()
        print("Processing: " + line + "  --  Current Dir: " + curr.name)
        if line.startswith("$"):  # command like ls or cd
            if "$ ls" == line:  # do nothing
                pass
            elif "cd" in line:  # change current directory
                folder_to_go_to = line.split(" ")[-1]
                if folder_to_go_to == "..":
                    curr = curr.parent
                elif folder_to_go_to == "/":  # cd /
                    curr = root
                else:
                    curr = curr.get_dir(folder_to_go_to)
        else:  # output from ls (create folders) (todo: check if exist)
            ls_args = line.split(" ")
            if ls_args[0] == "dir":  # a directory
                curr.add_item(Dir(ls_args[1], curr))
            else:  # not a directory
                curr.add_item(File(ls_args[1], int(ls_args[0]), curr))

print(root.to_string(0))

# Part 1
dirs = [root]
dirs.extend(root.get_dirs(True))
print("List: ", len(dirs))
dirs = list(filter(lambda x: x.get_size() < 100000, dirs))
print("List: ", len(dirs))

sum = 0
for i in dirs:
    sum += i.get_size()
print("Sum Part 1: ", sum)

# Part 2
total_space = 70000000
unused_needed = 30000000
max_possible_in_use = total_space - unused_needed
space_used = root.get_size()
space_to_delete = space_used - max_possible_in_use
print("Space to delete: ", space_to_delete)
dirs = [root]
dirs.extend(root.get_dirs(True))
print("List: ", len(dirs))
dirs = list(filter(lambda x: x.get_size() >= space_to_delete, dirs))
dirs.sort(key=lambda x: x.get_size())
print(dirs)
print("List: ", len(dirs))
print("Part 2 : ", dirs[0])






def with_lambda():
    dirs = [root]
    dirs.extend(root.get_dirs(True))
    dirs = list(filter(lambda x: x.get_size() < 100000, dirs))


def wo_lambda():
    dirs = [root]
    dirs.extend(root.get_dirs(True))
    for element in dirs:
        if element.get_size() < 100000:
            dirs.remove(element)


print(timeit.timeit(with_lambda, number=100))
print(timeit.timeit(wo_lambda, number=100))
