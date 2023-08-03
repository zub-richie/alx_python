#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    inputArgs = sys.argv

    # print (len(inputArgs) - 1, "arguments:")
    if len(inputArgs) > 1:
        print(len(inputArgs) - 1, "arguments:")
    else:
        print (len(inputArgs) - 1, "arguments.")
    for i, inputArgs in enumerate(inputArgs[1:], 1):
        # print(f"{i}: {arg}")
        print("{}: " "{}".format(i, inputArgs))

# for i in inputArgs[2:]:
#     print(i)

# print("{}:" "{}".format(i, inputArgs))