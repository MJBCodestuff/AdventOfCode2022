signal = open("input").read()

foundPacket = False
for i in range(3, len(signal)):
    if len(set(signal[i - 4:i])) == 4 and not foundPacket:
        print(f"Packet Start: {i}")
        foundPacket = True
    if len(set(signal[i - 14:i])) == 14:
        print(f"Message Start: {i}")
        break



