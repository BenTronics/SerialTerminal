FG_COLOR=\
{
    "black" : "\033[30m",
    "red" : "\033[31m",
    "green" : "\033[32m",
    "yellow" : "\033[33m",
    "blue" : "\033[34m",
    "magenta" : "\033[35m",
    "cyan" : "\033[36m",
    "white" : "\033[37m",
    "gray" : "\033[90m",
    "none" : ""
}

BG_COLOR=\
{
    "black" : "\033[40m",
    "red" : "\033[41m",
    "green" : "\033[42m",
    "yellow" : "\033[43m",
    "blue" : "\033[44m",
    "magenta" : "\033[45m",
    "cyan" : "\033[46m",
    "white" : "\033[47m",
    "none" : ""
}

RESET = "\033[0m"

def colorize_str(string, fg="none", bg="none"):
    return FG_COLOR[fg] + BG_COLOR[bg] + string + RESET