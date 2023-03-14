# Python UART Driver for Sensirion SFX6XXX

This repository contains the Python driver to communicate with a Sensirion sensor of the SFX6XXX family over UART using the SHDLC protocol.

<center><img src="images/product-image-sfx6xxx.png" width="300px"></center>

Click [here](https://sensirion.com/sfc6000) to learn more about the Sensirion SFX6XXX sensor family.



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

You can connect your sensor over the provided USB cable.  
For special setups check out the sensor pinout in the section below.

<details><summary>Sensor pinout</summary>
<p>
<img src="images/product-pinout-sfx6xxx.png" width="300px">

| *Pin* | *Cable Color* | *Name* | *Description*  | *Comments* |
|-------|---------------|:------:|----------------|------------|
| 1 | brown | VDD | Supply Voltage | +24V
| 2 | white | D+ |  | 
| 3 | black | D- |  | 
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
