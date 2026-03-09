import os

fileHandle = open('files/musa_daily_dairy.md', 'a')
fileHandle.write("### I learned about List, Tuples, Set, Dictionary in Python")
fileHandle.write("### Also, learned about open() for file handling, and 'os' package in python - relative and absolute file paths")
fileHandle.close()


# os.remove('files/musa_daily_dairy.md')