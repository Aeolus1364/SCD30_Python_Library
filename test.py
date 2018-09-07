import smbus

class SCD30:
  ADR = 0x61
  
  def init(self, port=1):
    self.bus = smbus.SMBus(port)
    
  def sendCommand(self, cmd, val=None):  # sends a 2 byte command
    data = []
    if val:
      data[0] = val >> 8
      data[1] = val & 0xFF
      
      crc = calcCRC8(data)
      
      bus.write_byte(ADR, cmd >> 8)  # sends the MSB
      bus.write_byte(ADR, cmd & 0xFF)  # sends the LSB
      bus.write_byte(ADR, data[0])
      bus.write_byte(ADR, data[1])
      bus.write_byte(ADR, crc)
    
    else:
      bus.write_byte(ADR, cmd >> 8)  # sends the MSB
      bus.write_byte(ADR, cmd & 0xFF)  # sends the LSB
  
  def readRegister(self, reg):
    bus.write_byte(ADR, reg >> 8)
    bus.write_byte(ADR, reg & 0xFF)
    
    msb = bus.read_byte()
    lsb = bus.read_byte()
    data = msb << 8 | lsb
    return data
  
  def calcCRC8(data, length):
