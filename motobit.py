# Use the SparkFun moto:bit with micro:bit micropython
# https://www.sparkfun.com/products/15713
#
# copyright 2022 George White <stonehippo@gmail.com>
# MIT License

from microbit import i2c
import array

class Motobit:
    LEFT = 8448 # address of the left motor
    RIGHT = 8192 # address of the right motor
    ENABLE = array.array('b', (0x70,0x01))
    DISABLE = array.array('b', (0x70,0x00))
    def __init__(self, address=0x59, enabled=False) -> None:
        self.address = address
        self.i2c = i2c
        self.enable() if enabled else self.disable()
    def command(self, buf) -> None:
        self.i2c.write(self.address, bytes(buf))
    def enable(self) -> None:
        self.command(Motobit.ENABLE)
    def disable(self) -> None:
        self.command(Motobit.DISABLE)
    def set_motor_speed(self, motor=0, speed=0, reverse=False) -> None:
        power = min(abs(speed), 127)
        power = (127 - power) if reverse else (power + 128)
        self.command((motor + power).to_bytes(2, 'big'))
    def polarity(self, motor=0, invert=False) -> None:
        i = 1 if invert else 0
        if motor is Motobit.RIGHT:
            self.command((4608 + i).to_bytes(2, 'big'))
        elif motor is Motobit.LEFT:
            self.command((4864 + i).to_bytes(2, 'big'))

