# Accept hex number
hex_num = input("Enter a 16-bit hexadecimal number: ")
# Convert hex → int → binary
value = int(hex_num, 16)      # hex to integer
binary_str = format(value, '016b')   # 16-bit binary

print(f"Hex: {hex_num.upper()}")
print(f"Binary (16-bit): {binary_str}")

bin1 = binary_str[:8]
bin2 = binary_str[8:]
print("First 8:", bin1, " Last 8:", bin2)

def checksum(bin1,bin2):

    # --- Binary addition ---
    carry = 0
    result = ""

    for i in range(7, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])
   
        total = bit1 + bit2 + carry
        result = str(total % 2) + result  # FIXED (prepend instead of append)
        carry = total // 2

    # If carry remains
    if carry == 1:
        temp = int(result, 2) + 1
        result = format(temp, '08b')

    print("Sum:", result)


    r = ""
    for i in result:
        if i == "0":
            r += "1"
        else:
            r += "0"

    print("Checksum:", r)

    # if there is no error
    c_e = 0
    e_result = ""
    for i in range(7, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])
        bit3 = int(r[i])
   
        total = bit1 + bit2 + bit3 + c_e
        e_result = str(total % 2) + e_result
        c_e = total // 2

    if c_e == 1:   # FIXED carry variable
        temp = int(e_result, 2) + 1
        e_result = format(temp, '08b')

    print("Error check sum:", e_result)

    # Complement of error result
    e_r = ""
    for i in e_result:
        if i == "0":
            e_r += "1"
        else:
            e_r += "0"
    #print("Final complement (should be 00000000 if no error):", e_r)
    if(e_r != "00000000"):
        print("there is an error")
    else:
        print("no error")

    #if there is an error( lets flip the 4th position)
    l = list(bin1)
    if(l[3] == '0'):
        l[3] = '1'
    else:
        l[3] = '0'

    bin1_f = "".join(l)

    c_e = 0
    e_result = ""
    for i in range(7, -1, -1):
        bit1 = int(bin1_f[i])
        bit2 = int(bin2[i])
        bit3 = int(r[i])
   
        total = bit1 + bit2 + bit3 + c_e
        e_result = str(total % 2) + e_result
        c_e = total // 2

    if c_e == 1:   # FIXED carry variable
        temp = int(e_result, 2) + 1
        e_result = format(temp, '08b')

    print("Error check sum:", e_result)

    # Complement of error result
    e_r = ""
    for i in e_result:
        if i == "0":
            e_r += "1"
        else:
            e_r += "0"
    #print("Final complement (should be 00000000 if no error):", e_r)
    if(e_r != "00000000"):
        print("there is an error")
    else:
        print("no error")

checksum(bin1,bin2)

# second part
print()
print()

name = input("enter your name:")


blist = []
ascii_l = []
for i in name:
    ascii_c = ord(i)
    ascii_l.append(ascii_c) # ASCII code
    string = format(ascii_c, '08b')  # 8-bit binary
    blist.append(string)
    #print(f"{ch} -> ASCII {ascii_c} -> Binary {binary_str}")

# If you want full binary string:

full = "".join(blist)
#print("Full binary representation:", full)
length = len(full)
print("length:",length)
h = int(length/2)
print("ascii:",ascii_l)
b1 = full[:h]
b2 = full[h:]
print("First half:", b1, "\nLast half:", b2)

checksum(b1,b2)