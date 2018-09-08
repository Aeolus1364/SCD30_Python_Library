import smbus

class Sensor:

    POLYNOMIAL = 0x31
    INITIALIZATION = 0xFF

    COMMAND_DATA_READY = 0x0202

    def __init__(self, port=1, address=0x61):
        self.bus = smbus.SMBus(port)
        self.adr = address


    def dataReady(self):
        data = self.readRegister(self.COMMAND_DATA_READY, 3)
        print(data)
        print(data[0:1])
        ready = data[0] << 8 | data[1]
        crc = self.calcCRC8(data[0:1])
        print(crc, data[2])
        if crc == data[2]:
            print("Verified")
        else:
            print("Not Verified")
        return ready

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
        crc = self.INITIALIZATION

        for byte in data:
            crc ^= byte
            for bit in range(8):
                if crc & 0x80:
                    crc = (crc << 1) ^ self.POLYNOMIAL
                else:
                    crc = (crc << 1)
                crc = crc % 256

        return crc