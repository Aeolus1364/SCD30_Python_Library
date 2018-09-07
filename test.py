import smbus

class SCD30:
  ADR = 0x61
  
  def init(self, port=1):
    self.bus = smbus.SMBus(port)
    
  def sendCommand(self, cmd):  # sends a 2 byte command
    bus.write_byte(ADR, cmd >> 8)  # sends the MSB
    bus.write_byte(ADR, cmd & 0xFF)  # sends the LSB
  
  def readRegister(self, reg):
    bus.write_byte(ADR, reg >> 8)
    bus.write_byte(ADR, reg & 0xFF)
    
    msb = bus.read_byte()
    lsb = bus.read_byte()
    data = msb << 8 | lsb
    
    return data
