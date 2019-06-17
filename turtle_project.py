from turtle import *
import pyfiglet
import os
import time
os.system('cls' or 'clear')
mybanner = pyfiglet.figlet_format(' Snow flake' , font='banner3-D')
print(mybanner)
print("A Funny script writed by mpspy :)")
time.sleep(3)
t = Turtle()
t.speed(0)
b = 180
for c in range(5):
    a = 9*c
    for i in range (100):
        t.circle(i,a)
        t.right(b)
        t.circle(i,a)
        t.right(b)
        t.circle(i,a)
        t.right(b)
        t.circle(i,a)
input("Press any key to continue...")        
