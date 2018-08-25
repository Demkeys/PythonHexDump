#   This script produces a hexdump of the mentioned file
#   Argument #1: Path of file.
#   Argument #2: Number of blocks to read.
#   NOTE: Argument #2 is not the number of bytes per block.
#   Each block's size is 16, so the script will try to read 16 bytes per block.

import sys
path = ""
blocksToRead = 0

def mainlogic():
    try:
        myfile = open(path, "rb")                               # Open file
        bcount = 0                                              # Byte count

        for r in range(blocksToRead):                           # For loop runs based on blocksToRead
            b = myfile.read(16)                                 # Read 16 bytes from file
            stringToPrint = ""                                  # Final string to print
            offset = format(bcount, '08x')                      # File Offset text, formatted to 8 digit hex, with padding of zeros
            hexBytes = ""                                       # File Bytes in hex
            strValues = ""                                      # File Bytes as text

            hexByteCount = 0                                    # Bytes count so that empty spaces can be added if less than 16
            for hexByte in b:                                   # Iterate through bytes
                hexBytes += (format(hexByte, '02x') + ' ')      # Format hexByte to 2 digit hex, with padding of zero
                hexByteCount+=1                                 
            hexByteCount = 16 - hexByteCount                    # Calculate how many empty spaces need to be added
            for r in range(hexByteCount):                       # Add empty spaces
                hexBytes += '   '

            strValues = "|"
            strValueCount = 0                                   # Bytes count so that empty spaces can be added if less than 16
            for strValue in b:                                  # Iterate through bytes
                if strValue > 32 and strValue < 126:            # If strValue is a printable character, excluding \n,\t,etc.
                    strValues += (chr(strValue))                # Convert to char and append strValues string
                else:                                           # Else
                    strValues += '.'                            # Append strValues string with a '.'
                strValueCount += 1
            strValueCount = 16 - strValueCount                  # Calculate how many empty spaces need to be added
            for r in range(strValueCount):                      # Add empty spaces
                strValues += ' '
            strValues += "|"

            stringToPrint = offset + '  ' + hexBytes + '  ' + strValues # Create final line, adding spaces where necessary
            print(stringToPrint)
            bcount += len(b)                                    # Increment total byte count

            if len(b) < 16:                                     # If byte count of current iteration was less than 16, break for loop
                break
        myfile.close()                                          # Close file
    except OSError as err:                                      # Catch exception if file is not found
        print(err)

def helptext():
    print("This script reads a file and produces a hexdump of it's bytes.")
    print("Argument #1: Path of file")
    print("Argument #2: Number of blocks to read.")
    print("NOTE: Argument #2 is not the number of bytes per block.")
    print("Each block's size is 16, so the script will try to read 16 bytes per block.")

if __name__ == "__main__":
    if len(sys.argv) < 3:                                       # If less than 3 arguments
        if sys.argv[1] == "--help":                             # Check if the argument is "--help"
            helptext()
            sys.exit()
        else:                                                   # Othersie, user entered invalid arguments
            print('Invalid arguments')                          
            sys.exit()
    try:                                                        # Make sure Argument #2 is always a number
        blocksToRead = int(sys.argv[2])                         
        if blocksToRead < 1:                                    # Make sure blocksToRead is never 0 or less
            print("Number of blocks can't be less than 1.")
            sys.exit()
        path = sys.argv[1]                                      # Store file path, it will be checked in a different try block
        mainlogic()
    except ValueError as err:
        print("Unable to convert to number")

    
