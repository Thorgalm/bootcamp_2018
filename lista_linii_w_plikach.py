#1 rozwiązanie listdir
import os

# def check_dir(path):
#     # print(f'Checking in {path}')
#     for name in os.listdir(path):
#         # print(f'Checking: {name}')
#         if os.path.isfile(os.path.join(path,name)):
#             if name.endswith('.py'):
#                 print(os.path.join(path,name))
#         if os.path.isdir(name):
#             check_dir(os.path.join(path,name))
#
# check_dir(os.getcwd())

# . to bieżacy folder lub os.getcwd (current working dir)

#2 rozwiązanie os.walk

# def check_dir2(path):
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             if filename.endswith('.py'):
#                 print(os.path.join(root, filename))
#
# check_dir2(os.getcwd())

#3 rozwiązanie glob

# import glob
# def check_dir3(path):
#     for filename in glob.glob('**/*.py', recursive=True):
#         print(os.path.join(filename))

# check_dir3(os.getcwd())

#4 rozwiązanie

from pathlib import Path

def  check_dir4(path):

    def searching_all_files(directory):
        dirpath = Path(directory)
        assert (dirpath.is_dir())
        file_list = []
        for x in dirpath.iterdir():
            if x.is_file():
                if x.suffix == '.py':
                    file_list.append(x)
            elif x.is_dir():
                file_list.extend(searching_all_files(x))
        return file_list

    lines_sum = 0
    for x in searching_all_files(path):
        with open(x) as f:
            lines_no = len(f.readlines())
            lines_sum += lines_no
            print(lines_sum)

#brakuje kilku linii

# rozwiazanie prowadzacego

from pathlib import Path

def searching_all_files(directory):
    dirpath = Path(directory)
    assert (dirpath.is_dir())
    file_list = []
    for x in dirpath.iterdir():
        if x.is_file():
            file_list.append(x)
        elif x.is_dir():
            file_list.extend(searching_all_files(x))
    return file_list

def file_lines(file):
    with open(file) as f:
        return len(f.readlines())

def lines_in_file(file_list):
    out = {}
    for file in file_list:
        if file.suffix in [".py", '.txt', '.csv']:
            out[file] = file_lines(file)
    return out

files = searching_all_files('.')
lines = lines_in_file(files)

for k, v in lines.items():
    print(f"{k}\t\t{v}")
print("Suma: ", sum(lines.values()))