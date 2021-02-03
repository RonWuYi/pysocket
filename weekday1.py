import os
import sys
import pathlib

# for i in sys.path:
#     print(i)
# print("################################################")
# sys.path.insert(1, os.path.join(pathlib.Path(os.path.dirname(__file__)).parents[0], "LeetCode"))
# for i in sys.path:
#     print(i)
prixfile = []

strs = ["flower","flow","flight"]
def new_func(prixfile, strs):
    for i in zip(*strs):
        if len(set(i)) == 1:
            prixfile.append(i[0])
        # print(i),    
        # else:
        #     break
    return "".join(prixfile)

print(new_func([], strs))