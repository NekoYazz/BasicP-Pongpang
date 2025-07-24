# Monster_HP = 100 
# Axe = 10
# Sword = 20
# Spear = 30

# print ("fight paste 1 exit paste 2" )
# while True :
#     choice = int(input("input 1 , 2 "))
#     if choice == 2:
#         print ("Escape")
#         break
#     elif choice == 1:
#         round = int(input("ตีกี่รอบ:"))
#     for i in range(1 ,round, +1):
#             print ("select : Axe Sword Spear")
#             weapon = (input("choose: "))
#             if weapon == Axe:
#                 Monster_HP -= Axe 
#                 print ("Hp left: " , Monster_HP)
#             elif weapon == Sword:
#                 Monster_HP -= Sword 
#                 print ("Hp left: " , Monster_HP)
#             elif weapon == Spear:
#                 Monster_HP -= Spear
#                 print ("Hp left: " , Monster_HP)    
#             else:
#                 print ("NO WEAPON Choose")
#     if Monster_HP <= 0 :
#         print ("Monster Dead")

monster = 100
arrow = 10
bomb = 50
sword = 25

while True:
    print("1.โจมตีมอนเตอร์")
    print("2.หนีดีกว่า")
    choice = int(input("พิมพ์ 1 / 2 เพื่อเลือก: "))
    if choice == 1:
        round = int(input("จะตีกี่ที่ใส่เลขไอ่สัส: "))
        for i in range(round):
            print("1.ใช้ดาบ")
            print("2.ใช้ธนู")
            print("3.ใช้ระเบิด")
            weapon = int(input("เลือกอาวุธ: "))
            if weapon == 1:
                monster = monster - sword
                print(monster)
            elif weapon == 2:
                monster = monster - arrow
                print(monster)
            elif weapon == 3:
                monster = monster - bomb
                print(monster)
                
            if monster < 0:
                monster = 20
                print(monster)
            elif monster == 0:
                print("win")
                break
        print("lose")
        break
    elif choice == 2:
        break


        

