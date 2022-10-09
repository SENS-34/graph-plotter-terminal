import math
n=int(input("Graph size: "))
# ch=input("Character for graph: ")
print("  "*(n-2)+"GRAPH PLOTTER")
print(" "*(n)+"Equation examples: y=x, x**2 = y+2, x < -10, x**2 >= y, etc.")
print("  "*(n-3)+"ENTER 'undo' TO UNDO")
ch = "#"
eq=[]
cond = "False"
while True:
    for y in range(n,-n-1,-1):
        for x in range(-n,n+1):
            # print("(",x,",",y,")" ,end="")
            if "/x" in cond or "//x" in cond or "/y" in cond or "//y" in cond or "%x" in cond or "%y" in cond:
                try:
                    if y == 1 or x == 1 or eval(cond):
                        print(ch, end = " ")
                        pass
                    else:
                        print(end="  "*len(ch))
                except:
                     pass
            else:
                if y == 1 or x == 1 or eval(cond):
                    print(ch, end = " ")
                    pass
                else:
                    print(end="  "*len(ch))
        print()
    inp = input(f"Equation{len(eq)+1}: ").strip()
    if inp == "circle":
        inp = f"x**2+y**2<={n*15}"
    if inp == "undo":
        if len(eq)>=1:
            eq.pop()
    else:
        if ("=" in inp) and (inp[inp.index("=")-1] not in ["<",">","!"]) and (inp[inp.index("=")+1] != "="):
            inp = inp[:inp.index("=")] + "=" + inp[inp.index("="):]
        eq.append(inp)
    cond = " or ".join(eq)
    if inp == "undo" and len(eq)==0:
        cond = "False"

