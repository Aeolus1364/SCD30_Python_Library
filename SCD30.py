import smbus

class Sensor:
    def __init__(self, port=1, address=0x61):
        self.bus = smbus.SMBus(port)
        self.adr = address

        self.polynomial = 0x31
        self.intialization = 0xFF



    def sendCommand(self, cmd):  # sends a 2 byte command
        data = [0]*2
        data[0] = cmd >> 8
        data[1] = cmd & 0xFF
        self.bus.write_i2c_block_data(self.adr, data[0], data[1:])

    def readRegister(self, reg, length):
        self.sendCommand(reg)

        data = self.bus.read_i2c_block_data(self.adr, 0, length)
        return data

    def calcCRC8(self, data):
        crc = self.intialization

        for byte in data:
            crc ^= byte
            for bit in range(8):
                if crc & 0x80:
                    crc = (crc << 1) ^ self.polynomial
                else:
                    crc = (crc << 1)
                crc = crc % 256

        return crc