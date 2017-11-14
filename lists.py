if __name__ == '__main__':
    avaliable_commands = ["insert", "print", "remove", "append", "sort", "pop", "reverse"]
    final_list = []
    command_num = int(input())

    for i in range(command_num):

        commands = input().split()

        try:
            command_index = avaliable_commands.index(commands[0])
        except ValueError:
            print("That command is not a valid one...")
            break
        
        if commands[0] == "insert":

        elif commands[0] == "print":
            pass
        elif commands[0] == "remove":
            pass
        elif commands[0] == "append":
            pass
        elif commands[0] == "sort":
            pass
        elif commands[0] == "pop":
            pass
        else: # reverse
            pass

        
