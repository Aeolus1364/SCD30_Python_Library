import SCD30

sensor = SCD30.SCD30()
data = sensor.readRegister(0x0202, 2)
print(data)