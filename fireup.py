#!/usr/bin/python

# Import the os module, for the os.walk function
import os
 
# Set the directory you want to start from
rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    # print('Found directory: %s' % dirName)
    for fname in fileList:
        print('%s/%s' % (dirName,fname) ) 