# Read Operations

# Step-1 : Open file
file = open("data.txt")

# Step-2 : Read file
# data = file.read()

# data = file.readline()

data = file.readlines()
print(data)

# Step-3 : Close file
file.close()
