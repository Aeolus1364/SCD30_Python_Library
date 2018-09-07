import SCD30

sensor = SCD30.Sensor()
data = sensor.readRegister(0x0202, 3)
for i in data:
    print("{} {0:b}".format(i, i))