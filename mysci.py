# Initialize my data variable
data = []

#Read the data file
filename = "data/wxobs20170821.txt"
with open(filename, 'r') as datafile:
    
    # Read the first three lines (header)    
    data = datafile.read()
    for _ in range(3):         # _ could also be i, j....
   #     print(_)
        datafile.readline()
 
    # Read and parse the rest of the file
    for line in datafile:
        datum = line.split()
        data.append(datum)

# DEBUG
for datum in data:
   print(datum) 
