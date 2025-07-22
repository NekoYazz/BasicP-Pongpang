dis = int(input("ระยะทาง (Km) :"))
price1 = 10 
price2 = 15
price3 = 25
price4 = 35
price5 = 45

if dis >= 5 and dis <= 50:
    print(price1)
elif dis >= 51 and dis <= 100:
    print(price2)
elif dis >= 101 and dis <= 300:
    print(price3)
elif dis >= 301 and dis <= 500:
    print(price4)
elif dis > 500:
    print(price5)
else:
    print("งง")
# weight = int(input("น้ำหนัก (Kg) :"))
# height = int(input("ส่วนสูง (cm) :"))
# BMI = (weight / height) ** 2
# weight1 = "ผอม"
# weight2 = "ปกติ"
# weight3 = "ท้วม"
# weight4 = "อ้วน"
# weight5 = "อ้วนมาก"


# if BMI < 18.50:
#     print(weight1)
# elif BMI >= 18.50 and BMI >= 22.90:
#     print(weight2)
# elif BMI >= 23 and BMI <= 24.90:
#     print(weight3)
# elif BMI >= 25 and BMI <= 29.90:
#     print(weight4)
# elif BMI >= 30 :
#     print(weight5)






