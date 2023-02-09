Run tests
=========

Unit tests can be run with `pytest <https://pytest.org>`_.

To install requried packages for testing:

.. code-block:: bash

    pip install -e .[test]       # Install requirements


We provide a mock implementation of the sensor in `sensirion_uart_sfc6xxx/response_provider.py`.
To run tests against the mock just run pytest:

.. code-block:: bash

    pytest                         # Run all tests using a mocked sensor
    

To run the tests against real hardware, you must have your SFC6XXX sensor connected to a Serial Port of your developement machine.
Pass the serial port used, e.g. COM1, when running the tests:

.. code-block:: bash

    pytest --serial-port=COM1       # Run all tests against connected sensor
