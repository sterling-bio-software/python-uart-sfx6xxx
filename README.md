# Python UART Driver for Sensirion SFX6XXX

This repository contains the Python driver to communicate with a 
Sensirion mass flow controller of the SFC6XXX family or a gas flow sensor of the SFM6XXX family over UART using the SHDLC protocol.

<center><img src="images/product-image-sfx6xxx.png" width="300px"></center>

Click [here](https://sensirion.com/sfc6000) to learn more about the Sensirion SFC6XXX mass flow controller family.

Click [here](https://sensirion.com/sfm6000) to learn more about the Sensirion SFM6XXX gas flow sensor family.


## Supported sensor types

- [SFC6000](https://sensirion.com/products/catalog/SFC6000/)
- [SFC6000D-5SLM](https://sensirion.com/products/catalog/SFC6000D-5slm/)
- [SFC6000D-50SLM](https://sensirion.com/products/catalog/SFC6000D-50slm/)
- [SFC6000D-20SLM](https://sensirion.com/products/catalog/SFC6000D-20slm/)
- [SFM6000](https://sensirion.com/products/catalog/SFM6000)
- [SFM6000D-20SLM](https://sensirion.com/products/catalog/SFM6000D-20slm)
- [SFM6000D-50SLM](https://sensirion.com/products/catalog/SFM6000D-50slm)
- [SFM6000D-5SLM](https://sensirion.com/products/catalog/SFM6000D-5slm)

The following instructions and examples use a *SFC6000*.

## Connect the sensor

The sensor needs to be connected to a 24V power supply.
Plug in the <a href="https://sensirion.com/products/catalog/EK-F5x">evaluation kit cable</a> to power and connect the USB port to your Raspberry Pi.

Please note that due to the delays introduced by the FTDI driver you can 
reach a maximum sampling frequency of about 20Hz with this setup.

For special setups check out the sensor pinout in the section below.

<details><summary>RS485 interface pinout</summary>
<p>
<img src="images/product-pinout-sfx6xxx.png" width="300px">

| *Pin* | *Cable Color* | *Name* | *Description*  | *Comments* |
|-------|---------------|:------:|----------------|------------|
| 1 | brown | VDD | Supply Voltage | +24V
| 2 | white | D+ | RS485 | 
| 3 | black | D- | RS485 | 
| 4 | blue | GND | Ground | 


</p>
</details>

## Documentation & Quickstart

See the [documentation page](https://sensirion.github.io/python-uart-sfx6xxx) for an API description and a 
[quickstart](https://sensirion.github.io/python-uart-sfx6xxx/execute-measurements.html) example.


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
