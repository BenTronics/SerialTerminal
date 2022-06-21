import terminal
from cmd_history import CMD_History
from serial_handler import Serial
from colored_string import colorize_str
import os
from time_stamp import get_time_stamp
import config

import logging
logging.basicConfig(filename="curser.log", filemode="w", level=logging.DEBUG, format="[{levelname}] {message}", style="{")
logger = logging.getLogger(__name__)

cmd_hist = CMD_History(30)
serial = Serial()
new_line = ""
new_line_LUT = {"CR":"\r", "LF":"\n", "CR+LF":"\r\n"}
user_char = ""
user_str = ""
serial_str = ""
curser_pos = 0
str_color = "cyan"

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")


config.restore_config()
print("Current config: \n" +config.to_string_current_config())

new_line = new_line_LUT[config.get_new_line()]
serial.set_new_line_char(new_line)

def delete_char(string, pos):
    return string[:pos] + string[pos+1:]


while True:
    if terminal.char_in_buf():
        user_char = terminal.get_char()
        # backspace
        if user_char == "<backspace>":
            if curser_pos != 0:
                logger.debug("<backspace>")
                logger.debug(f"{curser_pos=}")
                logger.debug(user_str)
                logger.debug((" " * curser_pos) + "!")
                print("\r" + " "*len(user_str), end="", flush=True)
                user_str = delete_char(user_str, curser_pos-1)
                logger.debug(f"{user_str}")
                print("\r" + colorize_str(user_str, str_color), end="", flush=True)
                print("\b"*((len(user_str)+1)-curser_pos), end="", flush=True)
                curser_pos -= 1
                if curser_pos < 0:
                    curser_pos = 0
                user_char = ""
        # enter
        elif user_char == "<enter>":
            print("\b \b"*len(user_str), end="\r", flush=True)
            serial.test_write(user_str)
            cmd_hist.add_item(user_str)
            print("\r",end="", flush=True)
            if user_str == "-q":
                print(colorize_str(user_str, str_color))
                print(colorize_str("Exit programm.", "yellow"))
                exit()
            elif user_str == "-lsconf":
                print(colorize_str(user_str, str_color))
                print("Current config:\n" + config.to_string_current_config() + "\n")
                print("Available configs:\n" + config.to_string_config())
            elif "-chconf=" in user_str:
                print(colorize_str(user_str, str_color))
                try:
                    config.select_config(user_str[8:])
                    print(colorize_str(f"Changed config to {user_str[8:]}.", "green"))
                    new_line = config.get_new_line()
                    new_line = new_line_LUT[new_line]
                    serial.set_new_line_char(new_line)
                except:
                    print(colorize_str(f"Config {user_str[8:]} not found.", "red"))
            else:
                print(get_time_stamp() + "\t" + colorize_str(user_str, str_color) + (colorize_str(new_line.replace("\r", "\\r").replace("\n", "\\n"),"gray")))
            user_str = ""
        # arrow up
        elif user_char == "<arrow-up>":
            print("\b \b"*len(user_str), end="\r", flush=True)
            user_str = cmd_hist.read_backward()
            print(colorize_str(user_str, str_color), end="", flush=True)
            curser_pos = len(user_str)
        # arrow down
        elif user_char == "<arrow-down>":
            print("\b \b"*len(user_str), end="\r", flush=True)
            user_str = cmd_hist.read_forward()
            print(colorize_str(user_str, str_color), end="", flush=True)
            curser_pos = len(user_str)
        # arrow left
        elif user_char == "<arrow-left>":
            curser_pos -= 1
            if curser_pos < 0:
                curser_pos = 0
            print("\r" + colorize_str(user_str, str_color) + ("\b" * (len(user_str)-curser_pos)), end="", flush=True)
            logger.debug("<arrow-left>")
            logger.debug(f"{curser_pos=}")
            logger.debug(user_str)
            logger.debug((" " * curser_pos) + "!")
        # arrow right
        elif user_char == "<arrow-right>":
            curser_pos += 1
            if curser_pos > len(user_str):
                curser_pos = len(user_str)
            print("\r" + colorize_str(user_str, str_color) + ("\b" * (len(user_str)-curser_pos)), end="", flush=True)
            logger.debug("<arrow-right>")
            logger.debug(f"{curser_pos=}")
            logger.debug(user_str)
            logger.debug((" " * curser_pos) + "!")
        # unwanted keys
        elif user_char == "<tab>" or user_char == "<none>":
            pass
        # regular char
        else:
            user_str = user_str[:curser_pos] + user_char + user_str[curser_pos:]
            print("\b " * len(user_str), end="")
            print("\r" + colorize_str(user_str, str_color), end="", flush=True)
            print("\b"*((len(user_str)-curser_pos)-1), end="", flush=True)
            if curser_pos == len(user_str)-1:
                curser_pos = len(user_str)
            else:
                curser_pos += 1
                if curser_pos > len(user_str):
                    curser_pos = len(user_str)
        user_char = ""
    
    
    if serial.test_inWaiting():
        serial_str = serial.test_readline()
        print("\b \b"*len(user_str), end="\r", flush=True)
        print(get_time_stamp() + "\t" + serial_str.replace("\r", colorize_str("\\r", "gray")).replace("\n", colorize_str("\\n", "gray")))
        print("\r" + colorize_str(user_str, str_color), end="", flush=True)

    
    
        