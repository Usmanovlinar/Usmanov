import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("file_1", type= str)
parser.add_argument("way", type= str)
args = parser.parse_args()
folder =[]
for i in os.walk(args.way):
    folder.append(i)
for address, dirs, files in folder:
    for file in files:
        if args.file_1 == file:
            print(address+'/' + file)
            break