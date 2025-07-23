Monster_HP = 100 
Axe = 10
Sword = 20
Spear = 30

print ("fight paste 1 exit paste 2" )
while True :
    choice = int(input("input 1 , 2 "))
    if choice == 2:
        print ("Escape")
        break
    elif choice == 1:
        round = int(input("ตีกี่รอบ:"))
    for i in range(1 ,round, +1):
            print ("select : Axe Sword Spear")
            weapon = (input("choose: "))
            if weapon == Axe:
                Monster_HP -= Axe 
                print ("Hp left: " , Monster_HP)
            elif weapon == Sword:
                Monster_HP -= Sword 
                print ("Hp left: " , Monster_HP)
            elif weapon == Spear:
                Monster_HP -= Spear
                print ("Hp left: " , Monster_HP)    
            else:
                print ("NO WEAPON Choose")
    if Monster_HP <= 0 :
        print ("Monster Dead")


        

