#!/home/norag/Development/Python_project/bin/python
'''simple command line tool'''
import sys

if __name__ == "__main__":
    print(f"The first argument is: {sys.argv[0]}")
    if len(sys.argv) >=2:
        print(f"The second argumet is: {sys.argv[1]}")
    if len(sys.argv) >= 3:
        print(f"The third argumet is: {sys.argv[2]}")
    if len(sys.argv) >=4:
        print(f"The fourth argument is: {sys.argv[3]}")
