def copy_file(command: str) -> None:
    command = command.split()
    with open(command[1], "r") as file_in, open(command[2], "w") as file_out:
        if command[0] != "cp" or command[1] == command[2]:
            file_out.write(file_in.read())
