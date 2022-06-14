import terminal
from cmd_history import CMD_History
from serial_handler import Serial

cmd_hist = CMD_History(30)
serial = Serial()
user_char = ""
user_str = ""
serial_str = ""

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
            serial.test_write(user_str)
            cmd_hist.add_item(user_str)
            print("\r",end="", flush=True)
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
        elif user_char == "<arrow-left>" or user_char == "<arrow-right>" or user_char == "<tab>" or user_char == "<none>":
            pass
        # regular char
        else:
            user_str += user_char
            print("\b " * len(user_str), end="")
            print("\r" + user_str, end="", flush=True)
        user_char = ""
    
    if serial.test_inWaiting():
        serial_str = serial.test_readline()
        print("\b \b"*len(user_str), end="\r", flush=True)
        print(serial_str)
        print("\r" + user_str, end="", flush=True)
    
    
        