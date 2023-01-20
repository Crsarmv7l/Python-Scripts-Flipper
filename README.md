# Python-Scripts-Flipper
A variety of Python scripts for generating valid Flipper Signals

After the work on the TPMS-Flipper project https://github.com/Crsarmv7l/TPMS-Flipper, I have continued to build Flipper Zero signal generating python scripts on a semi-random basis. The goals are to become better acquainted with python, and continue learning about RF signals analysis and generation

Some Examples:

![Screenshot 2023-01-12 10 53 34 AM](https://user-images.githubusercontent.com/85343771/213736959-976b85a9-4e4f-4cfc-8c77-4fd8711cf8c8.png)
![Screenshot 2023-01-12 12 02 58 AM](https://user-images.githubusercontent.com/85343771/213736966-2e322289-94f7-4d0a-82a5-42205916d5b0.png)

All Python scripts contained here are my own work

If you are attempting to spoof a Weather station, you must play the signals you generate for 1-2min as they often update only every few minutes. I suggest using subghz playlist and repeats.

- Code_gen from this project is used to generate the Flipper subs in conjunction with my scripts and timing setups https://github.com/triq-org/tx_tools
- Protocol information is obtained from rtl_433 https://github.com/merbanan/rtl_433
- Evil Pete's ook to sub script is used to convert the final generated .cu8 to a flipper sub. https://github.com/evilpete/flipper_toolbox

I make no promises as to the quality of the python on here, only that anything posted WILL generate a valid reading on rtl_433 when transmitted from the Flipper.
