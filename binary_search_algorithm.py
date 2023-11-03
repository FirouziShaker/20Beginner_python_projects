# a function that takes a list and target parameter
# multiple variable : middle, start, end, steps
# recursion or while loop
# increase the steps each time a split is done
# conditions to trak target position

def binary_search ( list , element ):
    middle = 0
    start = 0
    end = len(list)
    steps = 0
    
    while (start <= end):
        print("Step", steps , ":" , str(list[start:end+1]))
        
        steps = steps+1
        middle = (start + end ) //2
        
        if element == list[middle]:
            return middle
        
        if element < list[middle]:
            end = middle - 1
            
        else:
            start = middle + 1
            
    return -1

my_lsit = [1,2,3,4,5,6,7,8,9,10,11,12]
target = 4

binary_search(my_lsit,target)

for i in my_lsit:
    if i == 12:
        print("Found")