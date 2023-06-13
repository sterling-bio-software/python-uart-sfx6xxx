# Instructions to get started

You can find all the necessary instructions to help you get started with DIY-multiple MFC Evaluation Kit in the document here:
[DIY SFx6xxx User Instructions.pdf](DIY%20SFx6xxx%20User%20Instructions.pdf)
# Python implementation and Example Application

## Simple setup with python drivers

Add the Python package sensirion-uart-sfx6xxx to your environment. For
help with installation and implementation of your evaluation kit refer
to the documentation found in the [Useful Resources](#useful-resources)
section.

After plugging the USB cable into your computer, verify the COM-Port
your setup is connected to. This is the COM-Port you should reference in
the ShdlcSerialPort() command as seen in **Figure 3**. An example code
snippet for operating 3 MFC's at the same time can be downloaded from
the [Sensirion github](#python-drivers-and-documentation).

## Common Mistakes

### Address is not recognized

It is necessary to define the address of your MFC for use. The SHDLC
address must be specified over the SHDLC channel as seen in **Figure
3**. This must be done with each device individually.

### Change to slave address

When changing the slave address with "set_slave_address()" make sure
this corresponds to the address set over the "ShdlcChannel()" command.

### Correct baud rate

Make sure you set the correct baud rate for your application.

# Useful resources

## Python Drivers and Documentation

SFC6000/SFM6000 Datasheet

<https://sensirion.com/resource/datasheet/sfc6000d_sfm6000d>

Python driver

<https://github.com/Sensirion/python-uart-sfx6xxx>

Or use pip to install it directly from your command line:

    pip install sensirion_uart_sfx6xxx

Installation guide and documentation

[Sensirion SFX6XXX SHDLC Python Driver --- sensirion_uart_sfx6xxx 1.0.0
documentation](https://sensirion.github.io/python-uart-sfx6xxx/)

SFC6000/SFM6000 RS485 Guide

<https://sensirion.com/resource/application_note/SHDLC_Interface_Reference_SFC6xxx_SFM6xxx_RS485>

![](media/image6.emf)
