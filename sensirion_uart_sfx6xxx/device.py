#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2023 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:     sensirion-driver-generator 0.23.0
# Product:       sfx6xxx
# Model-Version: 2.0.0
#
"""
The class Sfx6xxxDeviceBase implements the low level interface of the sensor.
The class Sfx6xxxDevice extends the Sfx6xxxDeviceBase. It provides additional functions to ease the use of the
sensor.
"""

import time
from sensirion_driver_adapters.transfer import execute_transfer
from sensirion_driver_support_types.mixin_access import MixinAccess
from sensirion_uart_sfx6xxx.commands import (DeviceReset, GetArticleCode, GetBaudrate, GetCalibration,
                                             GetCalibrationFullscale, GetCalibrationGasId, GetCalibrationGasUnit,
                                             GetCalibrationValidity, GetCurrentFullscale, GetCurrentGasId,
                                             GetCurrentGasUnit, GetNumberOfCalibrations, GetProductName,
                                             GetProductType, GetSerialNumber, GetSetpoint, GetSlaveAddress,
                                             GetUserControllerGain, GetUserInitStep, GetVersion, MeasureRawFlow,
                                             MeasureRawThermalConductivityWithClosedValve, MeasureTemperature,
                                             ReadAveragedMeasuredValue, ReadMeasuredValue, SetBaudrate, SetCalibration,
                                             SetCalibrationVolatile, SetSetpoint, SetSetpointAndReadMeasuredValue,
                                             SetSlaveAddress, SetUserControllerGain, SetUserInitStep)


class Sfx6xxxDeviceBase:
    """Low level API implementation of SFX6XXX"""

    def __init__(self, channel):
        self._channel = channel

    @property
    def channel(self):
        return self._channel

    def set_setpoint(self, setpoint):
        """
        Set the flow setpoint as a physical value which is
        used by the flow controller as reference input.

        :param setpoint:
            The new setpoint.
        """
        transfer = SetSetpoint(setpoint)
        return execute_transfer(self._channel, transfer)

    def get_setpoint(self):
        """
        Get the current flow setpoint as a physical value.

        :return setpoint:
            The current setpoint.
        """
        transfer = GetSetpoint()
        return execute_transfer(self._channel, transfer)[0]

    def read_measured_value(self):
        """
        The command returns the latest measured flow as physical value.

        :return measured_value:
            The latest measured flow.
        """
        transfer = ReadMeasuredValue()
        return execute_transfer(self._channel, transfer)[0]

    def read_averaged_measured_value(self, measurements):
        """
        The command returns the average of given number of flow measurement as physical
        value. A single measurement has a duration of 1ms, so the command response time
        depends on the given number of measurements to average.

        :param measurements:
            number of measurements to average (1..100)

        :return averaged_measured_value:
            The averaged flow measurement.
        """
        transfer = ReadAveragedMeasuredValue(measurements)
        return execute_transfer(self._channel, transfer)[0]

    def set_setpoint_and_read_measured_value(self, setpoint):
        """
        This command is a combination of the two commands set_setpoint (0x00) and
        read_measured_value (0x08). It is intended for process data exchange
        (setpoint and flow) and saves a lot of protocol overhead compared to separate
        command usage.

        :param setpoint:
            The new setpoint as physical value.

        :return measured_value:
            The latest measured flow as physical value.
        """
        transfer = SetSetpointAndReadMeasuredValue(setpoint)
        return execute_transfer(self._channel, transfer)[0]

    def set_user_controller_gain(self, gain):
        """
        Set the user controller gain.

        :param gain:
            The user controller gain to set.
        """
        transfer = SetUserControllerGain(gain)
        return execute_transfer(self._channel, transfer)

    def get_user_controller_gain(self):
        """
        Get the user controller gain.

        :return gain:
            The current user controller gain.
        """
        transfer = GetUserControllerGain()
        return execute_transfer(self._channel, transfer)[0]

    def set_user_init_step(self, init_step):
        """
        Set the init step of flow controller.

        :param init_step:
            the user init step to set.
        """
        transfer = SetUserInitStep(init_step)
        return execute_transfer(self._channel, transfer)

    def get_user_init_step(self):
        """
        Get the user init step of flow controller.

        :return init_step:
            The current user init step.
        """
        transfer = GetUserInitStep()
        return execute_transfer(self._channel, transfer)[0]

    def measure_raw_flow(self):
        """
        Return the measured raw flow ticks from the sensor.

        :return flow:
            Measured raw flow in ticks.
        """
        transfer = MeasureRawFlow()
        return execute_transfer(self._channel, transfer)[0]

    def measure_raw_thermal_conductivity_with_closed_valve(self):
        """
        Perform a thermal conductivity measurement and return the measured raw tick
        value. The valve is automatically closed during the measurement.

        :return thermal_conductivity:
            Measured raw thermal conductivity in ticks.
        """
        transfer = MeasureRawThermalConductivityWithClosedValve()
        return execute_transfer(self._channel, transfer)[0]

    def measure_temperature(self):
        """
        Return the temperature of flow sensor.

        :return temperature:
            Measured temperature [°C].
        """
        transfer = MeasureTemperature()
        return execute_transfer(self._channel, transfer)[0]

    def get_number_of_calibrations(self):
        """
        Get the number of calibrations, i.e. how many calibration the device memory is
        able to hold.

        :return number_of_calibrations:
            Number of calibrations.
        """
        transfer = GetNumberOfCalibrations()
        return execute_transfer(self._channel, transfer)[0]

    def get_calibration_validity(self, index):
        """
        Check whether there exists a valid calibration at a specific index or not.

        :param index:
            The index to check whether there is a valid calibration or not.

        :return validity:
            Whether there exists a valid calibration at the specified index or not.
        """
        transfer = GetCalibrationValidity(index)
        return execute_transfer(self._channel, transfer)[0]

    def get_calibration_gas_id(self, index):
        """
        Get the gas ID of a specific calibration index.

        :param index:
            The calibration index to read the requested information from.

        :return gas_id:
            The read gas ID.
        """
        transfer = GetCalibrationGasId(index)
        return execute_transfer(self._channel, transfer)[0]

    def get_calibration_gas_unit(self, index):
        """
        Get the gas unit of a specific calibration index.

        :param index:
            The calibration index to read the requested information from.

        :return prefix:
            Medium unit prefix, see appendix for encoding.
        :return unit:
            Medium unit, see appendix for encoding.
        :return timebase:
            Timebase, see appendix for encoding.
        """
        transfer = GetCalibrationGasUnit(index)
        return execute_transfer(self._channel, transfer)

    def get_calibration_fullscale(self, index):
        """
        Get the fullscale flow of a specific calibration index.

        :param index:
            The calibration index to read the requested information from.

        :return fullscale:
            The read fullscale flow in the unit of the corresponding calibration.
        """
        transfer = GetCalibrationFullscale(index)
        return execute_transfer(self._channel, transfer)[0]

    def get_current_gas_id(self):
        """
        Get the gas ID of the currently active calibration.

        :return gas_id:
            The read gas ID.
        """
        transfer = GetCurrentGasId()
        return execute_transfer(self._channel, transfer)[0]

    def get_current_gas_unit(self):
        """
        Get the gas unit of the currently active calibration.

        :return prefix:
            Medium unit prefix, see datasheet for encoding.
        :return unit:
            Medium unit, see datasheet for encoding.
        :return timebase:
            Timebase, see datasheet for encoding.
        """
        transfer = GetCurrentGasUnit()
        return execute_transfer(self._channel, transfer)

    def get_current_fullscale(self):
        """
        Get the fullscale flow of the currently active calibration.

        :return fullscale:
            The read fullscale flow in the unit of the corresponding calibration.
        """
        transfer = GetCurrentFullscale()
        return execute_transfer(self._channel, transfer)[0]

    def set_calibration(self, calibration_number):
        """
        This command stops the controller, changes the used calibration of the flow
        controller and starts the controller. The selected calibration is stored
        and also used after a power-on or reset.

        :param calibration_number:
            The calibration number to activate.
        """
        transfer = SetCalibration(calibration_number)
        return execute_transfer(self._channel, transfer)

    def get_calibration(self):
        """
        Get the actual set calibration number of flow controller.

        :return calibration_number:
            The current activated calibration number.
        """
        transfer = GetCalibration()
        return execute_transfer(self._channel, transfer)[0]

    def set_calibration_volatile(self, calibration_number):
        """
        This command stops the controller, changes the used calibration of the flow
        controller and starts the controller. The selected calibration is not stored to
        a non volatile memory.

        :param calibration_number:
            The calibration number to activate.
        """
        transfer = SetCalibrationVolatile(calibration_number)
        return execute_transfer(self._channel, transfer)

    def set_slave_address(self, slave_address):
        """
        Sets the SHDLC slave address of the device.

        :param slave_address:
            The new slave address to set.
        """
        transfer = SetSlaveAddress(slave_address)
        return execute_transfer(self._channel, transfer)

    def get_slave_address(self):
        """
        Gets the SHDLC slave address of the device.

        :return slave_address:
            The current slave address of the device.
        """
        transfer = GetSlaveAddress()
        return execute_transfer(self._channel, transfer)[0]

    def set_baudrate(self, baudrate):
        """
        Sets the SHDLC baudrate of the device.

        :param baudrate:
            The new baudrate in bit/s. Allowed values are 9600, 19200, 38400, 57600 and
            115200 (default)
        """
        transfer = SetBaudrate(baudrate)
        return execute_transfer(self._channel, transfer)

    def get_baudrate(self):
        """
        Gets the SHDLC baudrate of the device.

        :return baudrate:
            Current baudrate in bit/s.
        """
        transfer = GetBaudrate()
        return execute_transfer(self._channel, transfer)[0]

    def get_product_type(self):
        """
        Gets the product type from the device.

        :return product_type:
            String containing the product type.
        """
        transfer = GetProductType()
        return execute_transfer(self._channel, transfer)[0]

    def get_product_name(self):
        """
        Gets the product name from the device.

        :return product_name:
            String containing the product name.
        """
        transfer = GetProductName()
        return execute_transfer(self._channel, transfer)[0]

    def get_article_code(self):
        """
        Get the article code of the device. This information is also contained on the product label.

        :return article_code:
            The article code as an ASCII string.
        """
        transfer = GetArticleCode()
        return execute_transfer(self._channel, transfer)[0]

    def get_serial_number(self):
        """
        Gets the serial number of the SFx6xxx sensor.

        :return serial_number:
            String containing the serial number of the SFx6xxx sensor.
        """
        transfer = GetSerialNumber()
        return execute_transfer(self._channel, transfer)[0]

    def get_version(self):
        """
        Gets the version information for the hardware, firmware and SHDLC protocol.

        :return firmware_major:
            Firmware major version number.
        :return firmware_minor:
            Firmware minor version number.
        :return firmware_debug:
            Firmware debug state. If the debug state is set, the firmware is in development.
        :return hardware_major:
            Hardware major version number.
        :return hardware_minor:
            Hardware minor version number.
        :return protocol_major:
            Protocol major version number.
        :return protocol_minor:
            Protocol minor version number.
        """
        transfer = GetVersion()
        return execute_transfer(self._channel, transfer)

    def device_reset(self):
        """Executes a reset on the device. This has the same effect as a power cycle."""
        transfer = DeviceReset()
        return execute_transfer(self._channel, transfer)


class Sfx6xxxDevice(Sfx6xxxDeviceBase):
    """Driver class implementation of SFX6XXX"""

    #: Access to base class
    sfx6xxx = MixinAccess()

    def __init__(self, channel):
        super().__init__(channel)

    def close_valve(self):
        """Switch device off (close the valve by setting setpoint to 0)"""
        return self.set_setpoint(0)
