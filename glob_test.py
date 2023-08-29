import glob # importing glob from library

seperator = 200 * '-'

files = glob.glob('*.csv') # find csv extension files from current directory

files = glob.glob('V*.csv') # find csv files starts with V.. in current directory.

files = glob.glob('//home/suger01/Desktop/CDCN_suger/*.csv') # go to the path and search certain files

files = glob.glob('./**/*.csv',  recursive=True) # when I use recursive 'TRUE', it means that path first go to the one file, then all files, and get csv file.

# files = glob.glob('./*.csv', root_dir='temp') # set path as a root DIR

files = glob.glob('./*') # getting all folder paths in current DIR

print(files) 


print(seperator)

for i in glob.iglob('./*'):
    print(i) # iglob return iterator not list which is better to memory efficency
    
print(seperator)