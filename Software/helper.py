class Helper:
    def __init__(self):
        return None

    def intToBytes(self, number):
        number = hex((1 << 16) + number)
        number = int(number, 16)
        low = int(number & 0xff)
        high = int((number >> 8) & 0xff)

        nums = [high, low]

        return nums

## bitsToByte: packages 8 bits into a byte
    def bitsToByte(self, b0, b1, b2, b3, b4, b5, b6, b7):
        bitlist = [b7,b6,b5,b4,b3,b2,b1,b0]
        out = 0
        for bit in bitlist:
            out = (out << 1) | bit

        return out
        
