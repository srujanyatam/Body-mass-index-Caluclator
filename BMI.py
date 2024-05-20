height=int(input("enter the height in cm :"))
weight=int(input("enter the weight in Kg :"))
def bMI(height,weight):
    BMI=(weight/height**2)*10000
    if (BMI<16):
        return "severly under weight" , BMI
    elif(BMI >=16 and BMI< 18.5):
        return "Moderate Under weight" , BMI
    elif(BMI >=18.5 and BMI<25):
        return "Healthy Weight" , BMI
    elif(BMI >= 25 and BMI < 35):
        return "Over Weight",BMI
    elif(BMI >=35):
        return "Obesity",BMI
quote,BMI = bMI(height,weight)
print("your BMI is:{} & You are {}".format(BMI,quote))
