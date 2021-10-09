
grille="""349287501
000000700
000509002
200095007
001000400
800720005
100402000
008000000
000000376"""

dict={}

splitt = grille.split("\n")
print(splitt)

for i in splitt:
    dict[i]=range(9)

print(dict)

for i in dict.items():
    print(i)