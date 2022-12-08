with open("input.txt") as f:
    data = f.readlines()

file_system = {"subdirs": {}, "files": {}}

def get_dir(path):
    dir = file_system
    for p in path:
        dir = dir["subdirs"].get(p)
    return dir


dir_paths = []
for line in data:
    line = line.split()
    if line[0] == "$":
        command = line[1:]
        if len(command) == 1:  # ls
            continue
        elif  command[-1] == "..":  # one out
            dir_paths.pop()
        elif  command[-1] == "/":  # start
            dir_paths = []
        else:
            dir_paths.append(command[-1])
            
    elif line[0] == "dir":
        parent_dir = get_dir(dir_paths)
        parent_dir["subdirs"][line[-1]] = {"subdirs": {}, "files": {}}

    else:
        parent_dir = get_dir(dir_paths)
        size, name = int(line[0]), line[1]
        parent_dir["files"][name] = size


db = {}
def calc_dir_size(dir, dirname):
    files_size = sum([f_size for f_size in dir["files"].values()])
    folders_sizes = sum([calc_dir_size(subdir, f"{dirname}/{subdir_name}") for subdir_name, subdir in dir["subdirs"].items()])

    total = files_size + folders_sizes
    db[dirname] = total

    return total

calc_dir_size(file_system, "/")

free_space = 70000000 - db["/"]
necessary_space = 30000000 - free_space

size_dir_remove = max(db.values())
for dir_size in db.values():
    if dir_size > necessary_space:
        size_dir_remove = min(size_dir_remove, dir_size)

print(size_dir_remove)

