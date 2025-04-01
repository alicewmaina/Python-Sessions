# Opening a file in read mode
with open('./Week 4/example.txt', 'r') as file:
    content = file.read()
    print(content)

# opening a file in write mode

with open("./Week 4/example.txt", "w") as file: 
    file.write("Hello, Python!")

# opening a file in append mode


