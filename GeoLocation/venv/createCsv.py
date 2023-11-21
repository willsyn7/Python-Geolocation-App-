import csv

'''row = ['2', ' Marie', ' California']
with open('locations.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)
    lines[2] = row #changed the second one
    #print(lines)
with open('locations1.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

readFile.close()
writeFile.close()
'''

def read_csv():
    with open('locations.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
    for line in lines:
        yield line

print("yielding")
data = next(read_csv(), None)
if data is not None:
    print(data)

def add_location(location, name, city, country):
    row1 = [[location,name, city, country]]
    print(row1)

    with open("locations1.csv", "w+") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(row1)


add_location("100 street","Sirocuser", "Ny", "america")
