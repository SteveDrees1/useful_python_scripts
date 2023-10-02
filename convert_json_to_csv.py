import pandas as pd
import os

os.chdir(r'C:\Users\BDDrees\Documents\r2d2_3dPrint')
cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

with open("python_Test.json") as inputFile:
    df = pd.read_json(inputFile)

df.to_csv(r'C:\Users\BDDrees\Desktop\csvfile.csv')
