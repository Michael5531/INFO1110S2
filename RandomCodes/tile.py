import sys
length = int(sys.argv[1])
if length % 2 == 0:
    print("Error: tile height must be an odd number")
    quit()
if len(sys.argv[2]) > length * 3:
    print("Error: name must fit within {} characters".format(length * 3))
    quit()

ad = "+|+"
i = 0
while i < int((length / 2) - 0.5):
    line = ad *((i * 2) + 1)
    if len(line) < 3*length:
        sm = int((3 * length - len(line)) / 2)
        line = "-" * sm + line + "-" *sm
    print(line)
    i += 1
line = sys.argv[2].upper()
if len(line) < 3 * length:
    sm = int((3 * length - len(line)) / 2)
    line = "-" * sm + line + "-" * sm
    if len(line) < 3 *length:
        line = "-" + line
print(line)

i = int((length / 2)- 0.5)-1
while i < int((length / 2)- 0.5) and i > -1:
    line =ad * ((i * 2) + 1)
    if len(line) <3 * length:
        sm = int((3 * length - len(line)) / 2)
        line = "-" * sm + line + "-" * sm
    print(line)
    i -= 1