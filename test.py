import SCD30

sensor = SCD30()
data = sensor.readRegister(0x0202)
print(data)