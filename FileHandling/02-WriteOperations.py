# Write Operations

# Step-1 : Open file
# If file already exists then open file otherwise creates a new file and open it
# 'w' mode overwrite the file content
# file = open("dataset.txt", "w")

# 'a' - append mode - append the content in existing file
file = open("dataset.txt", "a")
data = "\nThis text needs to be store in file"

# Step-2 : Write the file
file.write(data)

# Step-3 : Close the file
file.close()
