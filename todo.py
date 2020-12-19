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


def main():  # logic and connect everything
    if len(sys.argv) == 1:
        helpTodo()
    elif sys.argv[1] == 'ls':
        lsTodo()
    elif sys.argv[1] == 'help':
        helpTodo()

    elif len(sys.argv) == 3:  # if text is not passed in quotes after arg
        if sys.argv[1] == 'add':
            addTodo(sys.argv[-1])

    else:
        print('invalid command')


if __name__ == '__main__':
    main()
    # reportTodo()
