# PythonHexDump
### Simple script to create a hexdump of a file in a specific format. It displays the input offset in hexadecimal, followed by sixteen space-separated hexadecimal bytes split into two columns, followed by the same sixteen bytes as printable characters, enclosed within '|' characters.

* __This script produces a hexdump of the mentioned file__
* __Argument #1: Path of file.__
* __Argument #2: Number of blocks to read.__
* __NOTE: Argument #2 is not the number of bytes per block.__
* __Each block's size is 16, so the script will try to read 16 bytes per block.__
* __Use --help flag for info.__

__Example hexdump:__
![](https://github.com/Demkeys/PythonHexDump/blob/master/screencap3.png "Screenshot")


