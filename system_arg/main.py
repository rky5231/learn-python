# from sys import argv
# import sys

# print("The no of cmd line arguments: ", len(argv))
# print("The list of cmd line arguemts: ", argv)
# print("The Command Line arguments one by one: ")
# for i in argv:
#     print(i)


# -------------------------------------------------------

from sys import argv

argv = argv[1:]
argv = [eval(i) for i in argv]
print("Sum is: ", sum(argv))


