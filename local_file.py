import ascii
import sys


path = sys.argv[1]
width = int(sys.argv[2])
height = int(sys.argv[3])
result = ascii.asciify_file(path, width, height)
print('Result: \n' + result)
