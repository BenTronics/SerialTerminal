import msvcrt

__arrow_char = b"\x00"

__arrow_char_LUT = {
    b"H" : "<arrow-up>",
    b"P" : "<arrow-down>",
    b"K" : "<arrow-left>",
    b"M" : "<arrow-right>"
    }

__backspace = b"\x08"

__tab = b"\t"

__enter = b"\r"

def get_char():
    char = msvcrt.getch()
    char2 = ""   
    if char == __arrow_char:
        char2 = msvcrt.getch()
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
    if msvcrt.kbhit():
        return True
    else:
        return False 

def __is_ascii(ch):
    try:
        ch.decode("ascii")
        return True
    except:
        return False
