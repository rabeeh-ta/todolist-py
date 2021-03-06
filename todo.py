"""
    this was fun,
    I am a noob with not a lot of real world experience, maybe done something wrong too because your automated test was not working so i manually tested everything, hope someone sees the code and give me some feedback, took my whole evening. :) 
                                @rabeeh-ta
"""

import sys  # for grabing the
from datetime import date  # current yyyy-mm-dd


def helpTodo():  # help function
    print("""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics""")


def lsTodo():  # print all the todos inside todo.txt
    # open the txt iterate trough the lines and print with an index number
    f = open('./db/todo.txt', 'r')
    for indx, line in enumerate(f.readlines()):
        print(f'[{indx+1}] {line}')
    f.close()


def addTodo(passed_todo):  # add a todo to todo.txt
    # open txt add the new todo close
    f = open('./db/todo.txt', 'a')
    f.write(f'{passed_todo}\n')
    f.close()
    print(f'Added todo: "{passed_todo}"')


def delTodo(del_indx):  # remove a todo by its index

    try:
        # opening file to get the lines and storing in array
        f = open('./db/todo.txt', 'r')
        lines = f.readlines()
        f.close()

        # deleting that one line from the array
        del lines[int(del_indx)-1]

        # pushing the array to a new txt file clean and simple ;)
        f = open('./db/todo.txt', 'w+')
        for line in lines:
            f.write(line)
        f.close()

        print(f'Deleted todo #{del_indx}')

    except IndexError:
        print(f'Error: todo #{del_indx} does not exist, Nothing deleted')


def doneTodo(done_indx):  # mark a todo as done and move to done.txt with time

    try:
        # opening file to get the lines and storing in array
        f = open('./db/todo.txt', 'r')
        lines = f.readlines()
        f.close()

        # adding the done todo to done.txt file
        f = open('./db/done.txt', 'a')
        f.write(f'x {date.today()} {lines[int(done_indx)-1]}')
        f.close()

        # deleting that one line from the array
        del lines[int(done_indx)-1]

        # pushing the array to a new txt file clean and simple ;)
        f = open('./db/todo.txt', 'w+')
        for line in lines:
            f.write(line)
        f.close()

        print(f'Marked todo #{done_indx} as done')
    except IndexError:
        print(f'Error: todo #{done_indx} does not exist')


def reportTodo():  # all the stats of todos
    # open both txt files and get lengths
    f = open('./db/todo.txt', 'r')
    pending = f.readlines()
    f.close()
    f = open('./db/done.txt', 'r')
    completed = f.readlines()
    f.close()
    #print(pending, completed)

    # print the whole report
    print(f'{date.today()} Pending: {len(pending) if len(pending)-1 >= 0 else "0"} Completed: {len(completed) if len(completed)-1 >= 0 else "0"}')  # fix -1 if 0


def main():  # logic and connect everything
    if len(sys.argv) == 1:
        helpTodo()
    elif sys.argv[1] == 'ls':
        lsTodo()
    elif sys.argv[1] == 'help':
        helpTodo()
    elif sys.argv[1] == 'report':
        reportTodo()
    elif len(sys.argv) == 3:  # if text is not passed in quotes after arg
        if sys.argv[1] == 'add':
            addTodo(sys.argv[-1])
        elif sys.argv[1] == 'del':
            delTodo(sys.argv[-1])
        elif sys.argv[1] == 'done':
            doneTodo(sys.argv[-1])
    else:
        print('invalid command')


if __name__ == '__main__':
    main()
    # reportTodo()
