'''
List Method Parser
Purpose: Parses all metods for lists
Usage:
    command count:                  number of actions to take on the list (probably want to keep this under 100k)
         <number>:                  enter a command from the below methods format:
                                        command arg1 arg2 ...
                                    ex:
                                        append 'new_element' 
         
Available methods:    
    append(new_element)             add new_element to end of list
    clear()                         remove all elements from the list
    count(element)                  returns the number of occurances of element in list
    extend(new_list)                add new_list to the end of list
    index(element)                  return the first location in the list where element is found or throw a ValueError 
    insert(index, new_element)      add new_element at index
    pop(<index>)                    remove an element from the list and return its value, if index is not provided the last 
                                        element will be popped
    print                           display the current state of the array
    remove(element)                 remove the first occurance of element
    reverse()                       place all elements of list in opposite order 
    sort(key, reverse=True|False)   sort the list according to function key with largest or smallest value first

Special considerations:
    Strings must be encapsulate by quotes:
        append 'element'            <= works ok 
        append element              <= not so much
        
    Spaces are currently reserved for separating arguments, so placing spaces insde of an argument will cause this to throw mysterious errors. For example:
        
        extend [1,2,3,4,5]          <= works ok 
        extend [1, 2, 3, 4, 5]      <= not so much
        
        append 'new_element'        <= works ok 
        append 'new element'        <= breaks in a funny, non-obvious (to me) manner
    
    Methods that return a value are functional but the return is thrown a way this causes pop() to look suspiciously like it just removed the last element. index() does not appear to do anything, yet. This is top on my resolution bucket.
    
Author: Arlo Gittings
Created: 2020-11-20
Updates: all times in UTC 
    2020-11-20 2200 Completed initial challenge on HackerRank
    2020-ll-21 0100 Created documentation for calling and known bugs
    2020-ll-21 0223 Added spacing and running command count 
'''
command_count = int(input('command count: '))

arr = []
commands = []

for c in range(command_count): 
    width = 1
    
    while command_count >= 10 ** width:
        width += 1 
    
    commands.append(input((' ' * (5 - width)) + 'command ' + str(c+1).rjust(width, ' ') + ': ').strip().split()) 

[print(arr) if cmd[0] == 'print' else eval('arr.'+cmd[0]+'('+', '.join(cmd[1:])+')') for cmd in commands]