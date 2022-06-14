import serial
import serial.tools.list_ports
#------- Test driver -------
from random import randint
import logging
logging.basicConfig(filename="serial.log", filemode="w", level=logging.DEBUG, format="[{levelname}] {message}", style="{")
#---------------------------

class Serial(serial.Serial):

    def __init__(self, new_line_char="\r\n"):
        super().__init__()
        self.new_line_char = new_line_char
        #------- Test driver -------
        self.test_data = ["test_data_0", "test_data_1", "test_data_2", "test_data_3", "test_data_4", "test_data_5", "test_data_6", "test_data_7", "test_data_8", "test_data_9"]
        self.test_ptr = 0
        #---------------------------

    def set_new_line_char(self, char):
        self.new_line_char = char

    def write(self, msg):
        super().write((msg + self.new_line_char).encode("ascii", erros="replace"))

    def list_ports(self):
        ports = []
        for port in (serial.tools.list_ports.comports()):
            ports.append(port[0])
        return ports
    
    #------- Test driver -------
    def test_inWaiting(self):
        if randint(0, 1000000000) % 2000000 == 0:
            return True
        else:
            return False
    
    def test_readline(self):
        data = self.test_data[self.test_ptr]
        logging.debug("Rx>" + data)
        self.test_ptr += 1
        if self.test_ptr >= len(self.test_data):
            self.test_ptr = 0
        return data

    def test_write(self, line):
        logging.debug("Tx>" + ((line + self.new_line_char).replace("\r", "\\r")).replace("\n", "\\n"))
    #---------------------------