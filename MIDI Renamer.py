import os, re

path = 'D:/Music/Midi Samples/Midis/'
files = os.listdir(path)

delete_count = 0
rename_count = 0

for index, file in enumerate(files):
    rename = False
    curr_file = str(file)
    try:
        next_file = str(files[index + 1])
    except IndexError:
        pass
    curr_split_before = ''
    curr_split_after = ''
    split_phrase = ''

    if re.search(' - Edit', curr_file):
        split_phrase = ' - Edit'
        curr_split_before = curr_file.split(split_phrase)[0] + '.mid'
        curr_split_after = curr_file.split(split_phrase)[1]
    elif re.search(' -Edit', curr_file):
        split_phrase = ' -Edit'
        curr_split_before = curr_file.split(split_phrase)[0] + '.mid'
        curr_split_after = curr_file.split(split_phrase)[1]
    elif re.search('- Edit', curr_file):
        split_phrase = '- Edit'
        curr_split_before = curr_file.split(split_phrase)[0] + '.mid'
        curr_split_after = curr_file.split(split_phrase)[1]
    elif re.search('Edit ', curr_file):
        split_phrase = 'Edit '
        curr_split_before = curr_file.split(split_phrase)[0] + '.mid'
        curr_split_after = curr_file.split(split_phrase)[1]
    elif re.search('-  Edit', curr_file):
        split_phrase = '-  Edit'
        curr_split_before = curr_file.split(split_phrase)[0] + '.mid'
        curr_split_after = curr_file.split(split_phrase)[1]
    elif re.search(' - Sesh', curr_file):
        split_phrase = ' - Sesh'
        curr_split_before = curr_file.split(split_phrase)[0] + '.mid'
        curr_split_after = curr_file.split(split_phrase)[1]
    elif re.search('- Sesh', curr_file):
        split_phrase = '- Sesh'
        curr_split_before = curr_file.split(split_phrase)[0] + '.mid'
        curr_split_after = curr_file.split(split_phrase)[1]
    elif re.search('- Wildrage', curr_file):
        split_phrase = '- Wildrage'
        curr_split_before = curr_file.split(split_phrase)[0] + '.mid'
        curr_split_after = curr_file.split(split_phrase)[1]
    elif re.search('- Plasmus642', curr_file):
        split_phrase = '- Plasmus642'
        curr_split_before = curr_file.split(split_phrase)[0] + '.mid'
        curr_split_after = curr_file.split(split_phrase)[1]
    elif re.search('-  Plasmus642', curr_file):
        split_phrase = '-  Plasmus642'
        curr_split_before = curr_file.split(split_phrase)[0] + '.mid'
        curr_split_after = curr_file.split(split_phrase)[1]
    elif re.search(' - WIP', curr_file):
        split_phrase = ' - WIP'
        curr_split_before = curr_file.split(split_phrase)[0] + '.mid'
        curr_split_after = curr_file.split(split_phrase)[1]
    elif re.search('-  VERY WIP', curr_file):
        split_phrase = '-  VERY WIP'
        curr_split_before = curr_file.split(split_phrase)[0] + '.mid'
        curr_split_after = curr_file.split(split_phrase)[1]
    elif re.search(' VERY WIP', curr_file):
        split_phrase = ' VERY WIP'
        curr_split_before = curr_file.split(split_phrase)[0] + '.mid'
        curr_split_after = curr_file.split(split_phrase)[1]
    elif re.search(' - NF', curr_file):
        split_phrase = ' - NF'
        curr_split_before = curr_file.split(split_phrase)[0] + '.mid'
        curr_split_after = curr_file.split(split_phrase)[1]
    elif re.search(' -NF', curr_file):
        split_phrase = ' -NF'
        curr_split_before = curr_file.split(split_phrase)[0] + '.mid'
        curr_split_after = curr_file.split(split_phrase)[1]

    if curr_split_before == next_file:
        os.remove(path + curr_file)
        delete_count += 1
    else:
        if curr_split_after == '.mid':
            if not os.path.isfile(path + curr_split_before):    # If a correctly named file exists, don't make a new one
                new_curr_file = curr_split_before
                rename = True
        elif curr_split_after == '':
            rename = False
        elif curr_split_after != '':
            if not os.path.isfile(path + curr_split_before):    # If a correctly named file exists, don't make a new one
                new_curr_file = curr_split_before
                rename = True

    if rename:
        os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(new_curr_file)])))
        rename_count += 1

print('Files deleted: ' + str(delete_count))
print('Files renamed: ' + str(rename_count))