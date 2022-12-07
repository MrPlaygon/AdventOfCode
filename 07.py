# Learning Classes

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

    def add_item(self, item):
        self.items.append(item)
        if type(item == Dir):
            self.hasDir = True

    def has_dir(self):
        return self.hasDir

    def get_dirs(self):
        dirs = []
        for i in self.items:
            if type(i) == Dir:
                dirs.append(i)
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
            s += i.to_string(indentation+1)
        return s


# Parsing

root = Dir("/", None)
curr = root

with open("07.txt") as f:
    for line in f:
        line = line.rstrip()
        print("Processing: " + line + "  --  Current Dir: " + curr.name)
        if line.startswith("$"):  # command like ls or cd
            if "ls" in line:  # do nothing
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
                print("Adding DIR with args: " + str(ls_args))
                curr.add_item(Dir(ls_args[1], curr))
            else:  # not a directory
                print("Adding FILE with args: " + str(ls_args))
                curr.add_item(File(ls_args[1], ls_args[0], curr))
        if curr == None:
            print("NAOW")
            print(root.to_string(0))

#print(root.to_string(0))
