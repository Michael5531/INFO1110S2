import sys
location_list = []
file_location = open(sys.argv[1], "r").readlines()
i = 0
while i < len(file_location):
    update = file_location[i].rstrip()
    location_list.append(update)
    i += 1
print(location_list)
