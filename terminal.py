from serial import Serial
import msvcrt

#config.txt einlesen
conf_handler = open("config.txt", "r")
conf = conf_handler.readlines()

#com port öffnen
com = Serial()
com.timeout = 0.1
com.port = "COM" + str(conf[1].strip())
com.baudrate = int(conf[3].strip())
try:
    com.open()
except:
    print("COM Port nicht erreichbar, du Nugget!")
    exit()

if conf[5].strip() == "\r":
    new_line = "\r"
elif conf[5].strip() == "\n":
    new_line = "\r\n"
elif conf[5] .strip() == "\r\n":
    new_line = "\r\n"
else:
    new_line = ""

print("starte Terminal")

user_key = ""
user_str = ""
serial_line = ""

#super loop
while True:
    #serial readline print
    if com.inWaiting:
        serial_line = com.readline().decode("iso-8859-1")
        if serial_line != "":
            print(serial_line)
    #wenn benutzer taste gedrückt blockieren bis enter dann printen
    
    if msvcrt.kbhit():
        user_key = msvcrt.getche().decode()
        user_str += user_key
        if user_key == "\r":
            #wenn "-q" einegeben com port schließen
            if user_str.strip() == "-q":
                print("beende das programm")
                exit()
            com.write((user_str + new_line).encode())
            print("User> " + user_str.replace("\r", "").replace("\n", ""))
            user_str = ""
