# Develop a logic that reads a person's height and weight,
# calculates their BMI, and shows their status, according to the table below.
# - Under 18.5: Low weight.
# - Between 18.5 and 25: ideal weight.
# - 25 to 30: Excess weight.
# - 30 to 40: Obesity
# - Over 40: morbid obesity
from colorama import init
init()
p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))
bmi = p / (a*a)

if(bmi < 18.5):
    print('\033[33mbmi= 61{:.2f}, Low weight'.format(bmi))
elif(bmi >= 18.5 and bmi <= 25):
    print('\033[33mbmi= {:.2f}, ideal weight!'.format(bmi))
elif(bmi >= 25 and bmi <= 30):
    print('\033[33mbmi= {:.2f}, Excess weight!'.format(bmi))
elif(bmi >= 30 and bmi <= 40):
    print('\033[33mbmi= {:.2f}, Obesidty!'.format(bmi))
elif(bmi > 40):
    print('\033[33mbmi= {:.2f}, Morbid Obesity!'.format(bmi))
    