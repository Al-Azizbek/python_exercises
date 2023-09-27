# this code can help when I made the list but the path is chnage, can update txt file easily


old_path = '/mnt/nas/testfolder/'
new_path = '/mnt/suger/OULU_WorkSpace/'

# Open original file in read mode and new file in write mode
with open('/home/suger01/Downloads/Train.csv', 'r') as old_file, \
     open('./Train.csv', 'w') as new_file:

    # Read lines from the old file
    lines = old_file.readlines()

    # Iterate over lines
    for line in lines:
        # Replace old path with new path
        new_line = line.replace(old_path, new_path)

        # Write updated line to new file
        new_file.write(new_line)
