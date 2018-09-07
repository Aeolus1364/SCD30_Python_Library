import smbus

class SCD30:  
    def __init__(self, port=1, address=0x61):
        self.bus = smbus.SMBus(port)
        self.adr = address

    def sendCommand(self, cmd):  # sends a 2 byte command
        data = [0]*2
        data[0] = cmd >> 8
        data[1] = cmd & 0xFF
        self.bus.write_i2c_block_data(self.adr, data[0], data[1:])

    def readRegister(self, reg):
        self.sendCommand(reg)

        data = bytearray(bus.read_i2c_block_data(self.adr, 0))
        return data

        # def calcCRC8(data, length):
        #   pass
