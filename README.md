# Python UART Driver for Sensirion SFC6XXX

This repository contains the Python driver to communicate with a Sensirion SFC6XXX sensor over UART using the SHDLC protocol.

<center><img src="images/product-image-dummy.jpeg" width="300px"></center>

Click [here](https://sensirion.com/products/catalog/?filter_category=b460ae72-20ef-488d-8be1-e66a7d53db33/) to learn more about the Sensirion SFC6XXX sensor.

## Connect the sensor

1. Connect the sensor to a 24V power supply.
2. Connect the sensor to your host by using the provided USB cable

Please note that due to the delays introduced by the FTDI driver you can 
reach a maximum sampling frequency of about 20Hz with this setup.

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
