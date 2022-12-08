from typing import List, Dict, Set

input_day7 = open("input_day7", "r").read().split('\n')
terminal_output = [line.split(' ') for line in input_day7]


class File():
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __eq__(self, other):
        return self.name == other.name


class Directory():
    def __init__(self, full_name, parent):
        self.full_name = full_name
        self.parent = parent
        self.children = []
        self.files = []

    def __eq__(self, other):
        return self.full_name == other.full_name

    def add_child(self, dir):
        if dir not in self.children:
            self.children.append(dir)

    def add_file(self, file):
        if file not in self.files:
            self.files.append(file)

    @property
    def total_size(self):
        return sum([file.size for file in self.files]) + sum([child.total_size for child in self.children])


def change_dir(name, dirs) -> Directory:
    return list(filter(lambda x: x.full_name == name, dirs))[0]


def process_command(line, cur_dir, dirs):
    if line[1] == 'ls':
        pass  # nothing to do
    elif line[1] == 'cd':
        if line[2] == '/':
            cur_dir = change_dir('/', dirs)
        elif line[2] == '..' and cur_dir.full_name != '/':
            cur_dir = cur_dir.parent
        else:
            full_name = f"{cur_dir.full_name}{line[2]}/".replace('//','/')
            cur_dir = change_dir(full_name, dirs)
    return cur_dir

def process_line(line, cur_dir, dirs):
    if line[0] == '$':
        cur_dir = process_command(line, cur_dir, dirs)
    elif line[0] == 'dir':
        full_name = f'{cur_dir.full_name}{line[1]}/'
        new_dir = Directory(full_name, cur_dir)
        cur_dir.add_child(new_dir)
        if new_dir not in dirs:
            dirs.append(new_dir)
    else:
        cur_dir.add_file(File(line[1], int(line[0])))
    return cur_dir


current_dir = Directory('/', None)
directories = [current_dir]
for terminal_line in terminal_output:
    current_dir = process_line(terminal_line, current_dir, directories)

#print(sum([dir.total_size for dir in directories if dir.total_size <= 100000]))

free_space = 70000000 - directories[0].total_size
required_extra_space = 30000000 - free_space
sizes = [dir.total_size for dir in directories if dir.total_size >= required_extra_space]
sizes.sort()
print(min(sizes, key=lambda x: x-required_extra_space))
