with open("bowling.txt","r") as file:
    list=[]
    for line in file:
        stripped=line.strip()
        splitted=stripped.split(";")
        i=0
        new=[]
        for char in splitted:
            if i==0 or i==1:
                new.append(str(splitted[i]))
            else:
                new.append(int(splitted[i]))
            i+=1
        list.append(new)

    a=0
    for karakter in range(len(list)):
        toplam=0
        for eleman in list[karakter][2:]:
            toplam+=int(eleman)
        list[a].insert(0,toplam)
        a+=1
    sorted_list=sorted(list,reverse=True)

    for oyuncu in range(len(sorted_list)):
        print(f"{sorted_list[oyuncu][1]} {sorted_list[oyuncu][2]} {sorted_list[oyuncu][0]}")

    zero=[]
    x=0
    for sayi in list:
        zeroes=0
        tens=0
        for deger in sayi:
            if deger==0:
                zeroes+=1
            elif deger==10:
                tens+=1
        list[x].insert(0,tens)
        zero.append(f"{list[x][2]} {list[x][3]} has missed all the pins {zeroes} time.")
        x+=1

    second_sorted_list=sorted(list,reverse=True)

    maximum=max(a[0] for a in second_sorted_list)


    print(f"{second_sorted_list[0][2]} {second_sorted_list[0][3]} has knocked the all the pins {second_sorted_list[0][0]} times.")
    for player in range(len(zero)):
        if zero[player][-7]!="0":
            print(zero[player])
