with open('example.txt','r') as file:
    content=file.read()
    print(content)
    with open('example.txt','r') as file:
        for line in file:
            print(line.strip())

with open('example.txt','w') as file:
    file.write('hello world:\n')
    file.write('i am good')
with open('example.txt','a') as file:
    file.write('hi,everyone')

    