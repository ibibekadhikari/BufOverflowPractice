# Iterate over numbers from 1 to 255
for x in range(1, 256):
    # Construct the string representation
    # "\\x" represents a backslash followed by an 'x'
    # "{:02x}".format(x) formats the value of x as a two-digit hexadecimal number
    string_representation = "\\x" + "{:02x}".format(x)
    
    # Print the string representation without a newline
    print(string_representation, end='')
    
# Print a newline character to move to the next line
print()