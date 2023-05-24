import os, re

path = 'D:/Music/Midi Samples/Midis/'   # The path to your MIDI folder
files = os.listdir(path)

delete_count = 0
rename_count = 0

for index, file in enumerate(files):
    rename = False
    curr_file = str(file)   # The current file being checked
    try:
        next_file = str(files[index + 1])   # The file after the one being checked currently
    except IndexError:
        pass
    curr_split_before = ''
    curr_split_after = ''
    split_phrase = ''

    def func_splits(phrase):
        global curr_split_before, curr_split_after
        curr_split_before = curr_file.split(phrase)[0] + '.mid'
        curr_split_after = curr_file.split(phrase)[1]

    if re.search(split_phrase := ' - Edit', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := ' -Edit', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := '- Edit', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := 'Edit ', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := ' -  Edit', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := '-  Edit', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := ' - Sesh', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := '- Sesh', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := '- Wildrage', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := '- Plasmus642', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := '-  Plasmus642', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := ' - WIP', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := '-  VERY WIP', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := ' VERY WIP', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := ' WIP', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := ' - NF', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := ' -NF', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := '- NF', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := ' - Eman7081', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := ' - Grey42', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := ' - Nohpets', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := '- 10CD', curr_file):
        func_splits(split_phrase)
    elif re.search(split_phrase := ' - Jaden Balogh', curr_file):
        func_splits(split_phrase)

    if curr_split_before == next_file:
        os.remove(path + curr_file)
        delete_count += 1
    else:
        if curr_split_after == '.mid':
            if not os.path.isfile(path + curr_split_before):  # If a correctly named file exists, don't make a new one
                new_curr_file = curr_split_before
                rename = True
        elif curr_split_after == '':
            rename = False
        elif curr_split_after != '':
            if not os.path.isfile(path + curr_split_before):  # If a correctly named file exists, don't make a new one
                new_curr_file = curr_split_before
                rename = True

    if rename:
        os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(new_curr_file)])))
        rename_count += 1

print('Files deleted: ' + str(delete_count))
print('Files renamed: ' + str(rename_count))
