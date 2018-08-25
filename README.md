# PythonHexDump
Simple script to create a hexdump of a file in a specific format.

* This script produces a hexdump of the mentioned file
* Argument #1: Path of file.
* Argument #2: Number of blocks to read.
* NOTE: Argument #2 is not the number of bytes per block.
* Each block's size is 16, so the script will try to read 16 bytes per block.
