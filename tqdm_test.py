from tqdm import tqdm
import time

new_numbers = []

for i in tqdm (range(10)):
    time.sleep(3) # can modify from here the time 
    new_numbers.append(i ** 2)
    
print(f'Squeared numbers:{new_numbers}')
    
