# ## read

# f=open("b.txt",'r')
# for x in f:
#     print(x)
# f.close()  

# # write
# def writefile(fname,content,mode='w'):    # overwrites

#     f=open(fname,mode)
#     f.write(content)
#     f.close()

# writefile("b.txt","This")

# # write at begining
# def writefilebeg(fname,content,mode='a'):     # appends in last

#     f=open(fname,mode)
#     f.seek(0)
#     f.write(content)
#     f.close()

# writefilebeg("b.txt","This")

with open("b.txt") as file:
 data=file.readlines()
 for line in data:
     word=line.split()
     print(*word)
 
 