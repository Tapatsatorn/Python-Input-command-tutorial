class module():
    current_user = ''
    #current_user = input('current user : ')

    def show_help():
        """Display help commands."""
        print('''''')

    def command_loop():
        while True:
            cmd = input(f"<Users\\{module.current_user}\\{parts[0]}> $ ")
            parts = cmd.split(" ", 2)

            if cmd in ("exit()", "break"):
                break
            elif parts[0] == "": #module name
                command = parts[1] if len(parts) > 1 else ""
                argument = parts[2] if len(parts) > 2 else ""

                if command == "" and argument:
                    print('Hello world!')
                elif command == "-h" or command == 'help':
                    module.show_help()
                else:
                    print(f"Unknown command. Type '{parts[0]} -h' for help.")