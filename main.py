import terminal

user_char = ""
user_str = ""
while True:
    if terminal.char_in_buf():
        user_char = terminal.get_char()
        if user_char == "<backspace>":
            user_str = user_str[:-1]
            print("\b \b", end="", flush=True)
            user_char = ""
        elif user_char == "<enter>":
            print("")
            user_str = ""
        else:
            user_str += user_char
        print("\b " * len(user_str), end="")
        print("\r" + user_str, end="", flush=True)
        user_char = ""