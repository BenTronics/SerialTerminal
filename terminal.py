from serial import Serial
import msvcrt

#config.txt einlesen
conf_handler = open("config.txt", "r")
conf = conf_handler.readlines()

#com port öffnen
com = Serial()
com.timeout = 0.2
com.port = "COM" + str(conf[2].strip())
com.baudrate = int(conf[4].strip())
try:
    com.open()
except:
    print("COM Port nicht erreichbar, du Nugget!")
    exit()

#super loop

#serial readline print

#wenn benutzer taste gedrückt blockieren bis enter dann printen

#wenn "-q" einegeben com port schließen