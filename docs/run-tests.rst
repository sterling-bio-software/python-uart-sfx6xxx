Run tests
=========

Unit tests can be run with `pytest <https://pytest.org>`_:

.. code-block:: bash

    pip install -e .[test]                       # Install requirements
    pytest -m "not needs_device"                 # Run tests without hardware
    pytest                                       # Run all tests
    pytest -m "needs_device"                     # Run all tests for SFC6XXX


The tests with the marker `needs_device` have following requirements:

- The SFC6XXX sensor must be connected to a Serial Port of your developement machine.
- Pass the serial port where the sensor is connected with
  `--serial-port`, e.g. `pytest --serial-port=COM7`
