#Zadanie z obliczaniem BMI

weight=float(input("Podaj swoją wagę w kg:"))
height=float(input("Podaj swój wzrost w metrach:"))

bmi=float(weight/height**2)

if(bmi<18.5):
    print("Twoje BMI wynosi:", round(bmi,2), "Masz niedowagę!")
elif(18.5<=bmi<=24.9):
    print("Twoje BMI wynosi:", round(bmi,2), ". Waga w normie.")
elif(bmi>=25):
    print("Twoje BMI wynosi:", round(bmi,2), ". Masz nadwagę.")
elif(25<=bmi<=29.9):
    print("Twoje BMI wynosi:", round(bmi,2),". Okres przed otyłością.")
elif(30<=bmi<=34.9):
    print("Twoje BMI wynosi:", round(bmi,2),". Pierwszy stopień otyłości.")
elif(35<=bmi<=39.9):
    print("Twoje BMI wynosi:", round(bmi,2),". Drugi stopień otyłości.")
else:
    print("Twoje BMI wynosi:", round(bmi,2),". Trzeci, najwyższy stopień otyłości!!!")

