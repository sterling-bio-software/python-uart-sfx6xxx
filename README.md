# Python UART Driver for Sensirion SFC6XXX

**NOTE: the tests are currently not running (postprocessing delay is missing in the test-cases)**

This repository contains the Python driver to communicate with a Sensirion SFC6XXX sensor over UART using the SHDLC protocol.

<center><img src="images/product-image-dummy.jpeg" width="300px"></center>

Click [here](https://sensirion.com/products/product-categories/) to learn more about the Sensirion SFC6XXX sensor.





## Connect the sensor

You can connect your sensor over the provided USB cable.  
For special setups check out the sensor pinout in the section below.

<details><summary>Sensor pinout</summary>
<p>
<img src="images/product-pinout-dummy.jpeg" width="300px">

| *Pin* | *Cable Color* | *Name* | *Description*  | *Comments* |
|-------|---------------|:------:|----------------|------------|
| 1 | red | VDD | Supply Voltage | 3.3 or 5V
| 2 | black | GND | Ground | 
| 3 | green | RX | UART: Transmission pin for communication | 
| 4 | yellow | TX | UART: Receiving pin for communication | 
| 5 | blue | SEL | Interface select | Leave floating or pull to VDD to select UART
| 6 | purple | NC | Do not connect | 


</p>
</details>

## Documentation & Quickstart

See the [documentation page](https://sensirion.github.io/python-uart-sfc6xxx) for an API description and a 
[quickstart](https://sensirion.github.io/python-uart-sfc6xxx/execute-measurements.html) example.


## Contributing

We develop and test this driver using our company internal tools (version
control, continuous integration, code review etc.) and automatically
synchronize the `master` branch with GitHub. But this doesn't mean that we
don't respond to issues or don't accept pull requests on GitHub. In fact,
you're very welcome to open issues or create pull requests :-)

### Check coding style

The coding style can be checked with [`flake8`](http://flake8.pycqa.org/):

```bash
pip install -e .[test]  # Install requirements
flake8                  # Run style check
```

In addition, we check the formatting of files with
[`editorconfig-checker`](https://editorconfig-checker.github.io/):

```bash
pip install editorconfig-checker==2.0.3   # Install requirements
editorconfig-checker                      # Run check
```

## License

See [LICENSE](LICENSE).
