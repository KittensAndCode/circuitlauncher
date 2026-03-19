# CircuitLauncher
A launcher program for CircuitPython devices.

## Installation
To use it, simply upload all the files in the `upload` directory into the root of your device.
If you would rather import it too, that is perfectly fine and will work.

## Configuration
To configure the launcher, edit the `settings.toml` file on your device.
The setting that controls the launcher is the `PROGRAMS` setting. The format for the programs is `R:G:B:DIR:MOD`. R, G, and B are short for the red green blue values of the LED. DIR is short for directory (of the program you want to run) and MOD is short for the module name (filename without the `.py`).
