import os
import sys
if os.name == "nt":
    from msvcrt import getch
    from msvcrt import kbhit
else:
    import tty
    import termios
    from select import select
    stdin_fd = sys.stdin.fileno()
    tty_attr = termios.tcgetattr(stdin_fd)
    tty.setraw(stdin_fd)
    getch = lambda : sys.stdin.read(1).encode()

if os.name == "nt":
    __arrow_char = b"\x00"

    __arrow_char_LUT = {
        b"H" : "<arrow-up>",
        b"P" : "<arrow-down>",
        b"K" : "<arrow-left>",
        b"M" : "<arrow-right>"
        }
else:
    __arrow_char = b"\x1b"

    __arrow_char_LUT = {
        b"[A" : "<arrow-up>",
        b"[B" : "<arrow-down>",
        b"[D" : "<arrow-left>",
        b"[C" : "<arrow-right>"
        }


if os.name == "nt":
    __backspace = b"\x08"
else:
    __backspace = b"\x7f"

__tab = b"\t"

__enter = b"\r"

def get_char():
    char = getch()
    char2 = ""   
    if char == __arrow_char:
        char2 = getch()
        if os.name != "nt":
            char2 += getch()
        return __arrow_char_LUT[char2]
    elif char == __backspace:
        return "<backspace>"
    elif char == __enter:
        return "<enter>"
    elif char == __tab:
        return "<tab>"
    elif __is_ascii(char):
        return char.decode(encoding="ascii" ,errors="replace")
    else:
        return "<none>"

def char_in_buf():
    if os.name == "nt":
        return kbhit()
    else:
        dr, dw, de = select([sys.stdin], [], [], 0)
        return dr != []

def __is_ascii(ch):
    try:
        ch.decode("ascii")
        return True
    except:
        return False
