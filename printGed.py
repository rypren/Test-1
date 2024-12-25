# the name of the file
filename = "rypren Släktträd 240310 - may-oct.ged"

fh = open(filename, 'r')
found = False
for line in fh:
    if line.find("NAME") != -1:
        print(line.strip())
        count = 0
    if line.find("DEAT") != -1:
        found = True
        count = count+1
        print(line.strip())
    elif found:
        print(line.strip())
        found = False
        if count > 1:
            print("=======================")
            print(line.strip())
fh.close()
