FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


# print("hello from functions") this gets executed as we imported functions in main
# if we don't want the above to happen write it as...
# the code below gets executed only if we run functions.py directly
if __name__ == "__main__":  # the value of name is the name of current file
    print("Hello")
    print(get_todos())
