import math
n=int(input("Graph size: "))
# ch=input("Character for graph: ")
print("  "*(n-2)+"GRAPH PLOTTER")
print(" "*(n)+"Equation examples: y==x, x**2 == y+2, x < -10, x**2 >= y, etc.")
ch = "#"
inp = "False"
while True:
    for y in range(n,-n-1,-1):
        for x in range(-n,n+1):
            # print("(",x,",",y,")" ,end="")
            if "/x" in inp or "//x" in inp or "/y" in inp or "//y" in inp or "%x" in inp or "%y" in inp:
                try:
                    if y == 1 or x == 1 or eval(inp):
                        print(ch, end = " ")
                    else:
                        print(end="  "*len(ch))
                except:
                     pass
            else:
                if y == 1 or x == 1 or eval(inp):
                    print(ch, end = " ")
                else:
                    print(end="  "*len(ch))
        print()
    inp = input("Equation: ").strip()
    if ("=" in inp) and (inp[inp.index("=")-1] not in ["<",">","!"]) and (inp[inp.index("=")+1] != "="):
        inp = inp[:inp.index("=")] + "=" + inp[inp.index("="):]
    if inp == "circle":
        inp = "x**2+y**2<=n*15"
