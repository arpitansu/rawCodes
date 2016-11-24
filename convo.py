
fileName = "a.txt"
arr = ["Lorem", "Ipsum"]

str = open(fileName, 'r').read()

a =""
for i in arr:
    a =  str.replace(i, "\n\n"+i)
out = open("conv.txt","w")
out.write(a)
out.close()


