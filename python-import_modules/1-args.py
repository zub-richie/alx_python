#!/usr/bin/python3
import sys

inputArgs = sys.argv

print (len(inputArgs) - 1, "arguments:")

for i, arg in enumerate(inputArgs[1:], 1):
    print(f"{i}: {arg}")

# for i in inputArgs[2:]:
#     print(i)

# print("{}:" "{}".format(i, inputArgs))