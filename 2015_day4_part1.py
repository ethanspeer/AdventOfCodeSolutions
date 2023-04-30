import hashlib
import sys

puzzle_input = input("Enter your puzzle input: ")
placeholder = puzzle_input
my_string_bytes = puzzle_input.encode('utf-8')
md5_hash = ""

for i in range(sys.maxsize):
    puzzle_input += str(i+1)
    bytes = puzzle_input.encode('utf-8')
    md5_hash = hashlib.md5(bytes).hexdigest()
    puzzle_input = placeholder
    if(md5_hash[:5] == "00000"):
        print("Answer:", i+1)
        break


