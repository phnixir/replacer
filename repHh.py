file = open("text.txt","r")
gcon = file.read()

gcon = gcon.replace("G","H")
gcon = gcon.replace("g","h")

file = open("text.txt","w")
file.write(gcon)
file.close

print(gcon)
input()
