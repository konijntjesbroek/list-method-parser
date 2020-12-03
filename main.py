'''
01234567890123456789012345678901234567890123456789012345678901234567890123456789
          1         2         3         4         5         6         7
List Method Parser
Author: Arlo Gittings
Created: 2020-11-20
Updates: see change log
Purpose: Parses all metods for lists
Usage:
    command count:                  number of actions to take on the list 1-100
                                    i for interactive
                                    q to quit

         <number>:                  enter a command from the below methods
                                    format: command arg1 arg2 ...
                                    ex:
                                        append 'new_element'

                                    If interective mode is chosen commands may
                                    be entered one at a time, after which the
                                    array and any returns will be printed to
                                    the console

Available methods:
    append(new_element)             add new_element to end of list
    clear()                         remove all elements from the list
    count(element)                  returns the number of occurances of element
                                    in list.
    extend(new_list)                add new_list to the end of list
    index(element)                  return the first location in the list where
                                    element is found or throw a ValueError
    insert(index, new_element)      add new_element at index
    pop(<index>)                    remove an element from the list and return
                                    its value, if index is not provided the
                                    last element will be popped
    print                           display the current state of the array
    remove(element)                 remove the first occurance of element
    reverse()                       place all elements of list in opposite
                                    order
    sort(key, reverse=True|False)   sort the list according to function key
                                    with largest or smallest value first

Special considerations:
    Strings must be encapsulate by quotes:
        append 'element'            <= works ok
        append element              <= not so much

    Spaces are currently reserved for separating arguments, so placing spaces
    insde of an argument will cause this to throw mysterious errors.
    For example:

        extend [1,2,3,4,5]          <= works ok
        extend [1, 2, 3, 4, 5]      <= not so much

        append 'new_element'        <= works ok
        append 'new element'        <= breaks in a funny, non-obvious manner

    Methods that return a value are functional but the return is thrown a way
    this causes pop() to look suspiciously like it just removed the last
    element. index() does not appear to do anything, yet. This is top on my
    resolution bucket.

          1         2         3         4         5         6         7
01234567890123456789012345678901234567890123456789012345678901234567890123456789
'''


def welcome():

    greetings = '''Welcome to the list method toy!

    This tool has been created to familiarize myself with the list methods
    available in python 3. Originally it was created to solve a simple
    challenge on HackerRank. Then it sorta took over if you need anything, feel
    free to drop me a message
    '''
    print(greetings)


def get_input():
    prompt = 'b for batch\ni for interactive\nq to quit\n\nSelect Mode: '
    while True:
        input_mode = input(prompt).strip()
        if input_mode.isnumeric():
            return input_mode
        elif input_mode.lower() == 'b':
            return 'batch'
        elif input_mode.lower() == 'i':
            return 'interactive'
        elif input_mode.lower() == 'q':
            return False
        else:
            print('invalid command')


def b_mode(command_count):
    arr = []
    commands = []
    holder = ''
    while not command_count.isnumeric():
        command_count = input('Enter the number of commands to run: ').strip()
    command_count = int(command_count)

    for c in range(command_count):
        width = 1
        while command_count >= 10 ** width:
            width += 1
        commands.append(input((' ' * (5 - width)) + 'command ' +
                              str(c+1).rjust(width, ' ') +
                              ': ').strip().split())
    for cmd in commands:
        if cmd[0].lower() == 'print':
            print(f'holder: {holder}\narr: {arr}\n')
        elif cmd[0].lower() == 'pop' or cmd[0].lower() == 'count':
            holder = eval('arr.'+cmd[0]+'('+', '.join(cmd[1:])+')')
        else:
            eval('arr.'+cmd[0]+'('+', '.join(cmd[1:])+')')


def i_mode():
    arr = []
    holder = ''

    print('Entering interactive mode\nPress q to quit')
    cmd = input('command: ').strip().split()

    while cmd[0][0].lower() != 'q':
        if cmd[0].lower() == 'print':
            print(f'holder: {holder}\narr: {arr}\n')
        elif cmd[0].lower() == 'pop' or cmd[0].lower() == 'count':
            holder = eval('arr.'+cmd[0]+'('+', '.join(cmd[1:])+')')
        else:
            eval('arr.'+cmd[0]+'('+', '.join(cmd[1:])+')')
            
        cmd = input('command: ').strip().split()


welcome()
parse_mode = get_input()

while parse_mode:
    if parse_mode == 'interactive':
        i_mode()
    else:
        b_mode(parse_mode)

    parse_mode = get_input()
