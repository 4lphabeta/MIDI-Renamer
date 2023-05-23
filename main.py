# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os
path = 'D:/Music/Midi Samples/Midis'
files = os.listdir(path)


for index, file in enumerate(files):
    filename = os.path.basename(path)
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))