# SCD30_Python_Library

Development has stopped to to I2C stretching bug in the Raspberry Pi's BCM2835 chip. More information can be found here:
https://elinux.org/BCM2835_datasheet_errata#p35_I2C_clock_stretching

I would highly recommend paulvha's SCD30 pi library which was released earlier this month! It gets around the bug by using bitbanged I2C connection via another one of their libaries, twowire. I will link it below.

https://github.com/paulvha/scd30_on_raspberry
