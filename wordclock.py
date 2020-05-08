#word clock by 4efk
from num2words import num2words
import time
import turtle

#Window customization
a=input('Background color: ')
b=input('Text color: ')

#Turtle setup
sc=turtle.Screen()
sc.bgcolor(a)
turtle.setup(width=630, height=350)
t=turtle.Turtle()
t.hideturtle()
t.color(b)

#Creating main function
def get_time():
    #Time in number form
    thing1= time.strftime('%I')
    #Time in text form in capitals (thing11 == hours, thing22 == minutes)
    thing11= num2words(thing1).upper()
    thing2= time.strftime('%M')
    thing22= num2words(thing2).upper()
    #Some if statements for like 'past', 'to', 'quarter',...
    if int(thing2) == 15:
        thing22='QUARTER'
        magicword='PAST'

    if int(thing2) == 30:
        thing22='HALF'
        magicword='PAST'

    if int(thing2) == 45:
        thing22='QUARTER'
        magicword='TO'
        thing11=num2words(int(thing1)+1).upper()

    if int(thing2) < 30 and int(thing2) != 15:
        magicword='PAST'

    if int(thing2) == 0:
        thing22='EXACTLY'
        magicword=thing11
        thing11='O´CLOCK'

    if int(thing2) > 30 and int(thing2) != 45:
        thing22=num2words(60-int(thing2)).upper()
        magicword='TO'
        thing11=num2words(int(thing1)+1).upper()

    #Writing it on the screen
    t.write('IT IS '+thing22+' '+magicword+' '+thing11, move=False, align='center', font=('Arial', 25, 'bold'))

while True:
    get_time()
    time.sleep(1)
    t.undo()
