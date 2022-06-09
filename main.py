import terminal
from cmd_history import CMD_History

cmd_hist = CMD_History(30)
user_char = ""
user_str = ""

while True:
    if terminal.char_in_buf():
        user_char = terminal.get_char()
        # backspace
        if user_char == "<backspace>":
            print("\b \b", end="", flush=True)
            user_str = user_str[:-1]
            print("\r" + user_str, end="", flush=True)
            user_char = ""
        # enter
        elif user_char == "<enter>":
            print("")
            cmd_hist.add_item(user_str)
            user_str = ""
        # arrow up
        elif user_char == "<arrow-up>":
            print("\b \b"*len(user_str), end="\r", flush=True)
            user_str = cmd_hist.read_backward()
            print(user_str, end="", flush=True)
        # arrow down
        elif user_char == "<arrow-down>":
            print("\b \b"*len(user_str), end="\r", flush=True)
            user_str = cmd_hist.read_forward()
            print(user_str, end="", flush=True)
        # unwanted keys
        elif user_char == "<arrow-left>" or user_char == "<arrow-right>" or user_char == "<tab>":
            pass
        # regular char
        else:
            user_str += user_char
            print("\b " * len(user_str), end="")
            print("\r" + user_str, end="", flush=True)
        user_char = ""