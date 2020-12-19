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


def main():  # logic and connect everything
    if len(sys.argv) == 1:
        helpTodo()

    elif sys.argv[1] == 'help':
        helpTodo()

    else:
        print('invalid command')


if __name__ == '__main__':
    main()
    # reportTodo()
