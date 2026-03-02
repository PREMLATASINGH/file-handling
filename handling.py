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
    file.write('hi,everyone:\n')
lines=['first line:\n','second line:\n','third line\n']
with open('example.txt','a') as file:
    file.writelines(lines)
data=b'\x00\x01\x02'
with open('example.bin','wb') as file:
    file.write(data)
with open('example.bin','rb') as file:
    content=file.read()
    print(content)
with open('example.txt','w+') as file:
   file.write('i am learning:\n')
   file.write('i am data analyst:\n')
   ##file.seek(0)
   content=file.read()
   print(content)