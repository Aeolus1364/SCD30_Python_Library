import smbus

class Sensor:

    POLYNOMIAL = 0x31
    INITIALIZATION = 0xFF

    COMMAND_DATA_READY = 0x0202
    COMMAND_READ_MEASUREMENT = 0x0300

    def __init__(self, port=1, address=0x61):
        self.bus = smbus.SMBus(port)
        self.adr = address

    def readMeasurement(self):
        if self.dataReady():
            data = self.readRegister(self.COMMAND_READ_MEASUREMENT, 18)
            co2m = data[0:3]
            co2l = data[3:6]
            tempm = data[6:9]
            templ = data[9:12]
            humm = data[12:15]
            huml = data[15:18]
            check = [self.verify(co2m), self.verify(co2l)]
            return check
        else:
            print("Data not ready")

    def dataReady(self):
        data = self.readRegister(self.COMMAND_DATA_READY, 3)
        ready = self.verify(data)
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

    def compareCRC8(self, data, crc):
        calc = self.calcCRC8(data)
        return calc == crc

    def verify(self, data):
        value = data[0:2]
        crc = data[2]
        return crc == self.calcCRC8(value)

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