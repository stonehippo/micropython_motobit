# SparkFun moto:bit driver for BBD micro:bit micropython

The [SparkFun moto:bit](https://www.sparkfun.com/products/15713) is a motor controller carrier for the [BBC micro:bit](https://microbit.org). This board is also available as part of the [SparkFun micro:bot kit](https://www.sparkfun.com/products/16275).

SparkFun provides a MakeCode extension for using this board, but no driver for working with the board using micro:bit-flavored [micropython](https://microbit.org/get-started/user-guide/python-editor/). Given the spiffy new [micro:bit Python Editor](https://python.microbit.org/v/3), it would nice to be able to program this motor controller in micropython. This class makes that easy to do.

## Usage
The Python Editor supports creating additional files (in the `Project` tab). My suggestion is to copy `motobit.py` contents into a new file. Once that's done, it's pretty easy to get things going:

```python
from motobit import Motobit

mb = Motobit()
mb.set_motor_speed(Motobit.RIGHT, 55)
mb.set_motor_speed(Motobit.LEFT, 55, reverse=True)
mb.enable() # turn on the motors, and go!
...
mb.disable() # turn the motors off
```

That should pretty much do it. I think the code above is pretty clear, if you want to understand what the driver is doing.

This code was based on [the moto:bit PXT extension](https://github.com/sparkfun/pxt-moto-bit).

## Note

This could was originally available as a [gist](https://gist.github.com/stonehippo/6b9f2f0d4cbec54f61ddb91adcd0b289); migrated to this repo to make it easier to find and update.
