import os
import sys
import pathlib

for i in sys.path:
    print(i)
print("################################################")
sys.path.insert(1, os.path.join(pathlib.Path(os.path.dirname(__file__)).parents[0], "LeetCode"))
for i in sys.path:
    print(i)
