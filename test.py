import SCD30
from time import sleep

sensor = SCD30.Sensor()
t = sensor.readRegister(0x0202, 3)
r = {}
data = []
for i in range(0, 5):
	counter = 0
	for j in range(10):
		print("{0} seconds test {1}".format(i, j)
		data = sensor.readRegister(0x0202, 4)
		if data[0] == 0:
			counter += 1
		else:
			counter -= 1
		sleep(i)
	r[i] = counter
print(r)
