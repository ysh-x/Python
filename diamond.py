def pyramid(Start,End,Element):
    for i in range((Start-1),(End+1),1):
        for j in range(0,i,1):
            print(Element,end=" ")
        print()

Start = int(input("ROWS: "))
End = int(input("COLUMNS: "))
Element = input("ELEMENT: ")
pyramid(Start,End,Element)
