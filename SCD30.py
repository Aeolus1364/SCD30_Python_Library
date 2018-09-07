import smbus

class SCD30:  
    def __init__(self, port=1, address=0x61):
        self.bus = smbus.SMBus(port)
        self.adr = address

    def sendCommand(self, cmd, val=None):  # sends a 2 byte command
        if val:
            data = []
            data[0] = val >> 8
            data[1] = val & 0xFF

            # crc = calcCRC8(data)

            self.bus.write_byte(self.adr, cmd >> 8)  # sends the MSB
            self.bus.write_byte(self.adr, cmd & 0xFF)  # sends the LSB
            self.bus.write_byte(self.adr, data[0])
            self.bus.write_byte(self.adr, data[1])
            self.bus.write_byte(self.adr, crc)

        else:
            self.bus.write_byte(self.adr, cmd >> 8)  # sends the MSB
            self.bus.write_byte(self.adr, cmd & 0xFF)  # sends the LSB

    def readRegister(self, reg):
        self.bus.write_byte(self.adr, reg >> 8)
        self.bus.write_byte(self.adr, reg & 0xFF)

        msb = self.bus.read_byte()
        lsb = self.bus.read_byte()
        data = msb << 8 | lsb
        return data

        # def calcCRC8(data, length):
        #   pass
