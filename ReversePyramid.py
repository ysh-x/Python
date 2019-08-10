def ReversePyramid(Start,End,Element):
    for i in range(End,(Start-1),-1):
        for j in range(0,i,1):
            print(Element,end=" ")
        print()
Start = int(input("ROWS: "))
End = int(input("COLUMNS: "))
Element = input("ELEMENT: ")
ReversePyramid(Start,End,Element)
