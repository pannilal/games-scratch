# import pyttsx3

# engine = pyttsx3.init('sapi5 ')
# voices = engine.getproperty('voices')
# print(voices)
# engine.setproperty('voice', voices[0].id)


# def speak(audio):
#    pass
import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
window = turtle
window.title('praneel spiograph app')
for i in range(6):
    for colours in ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)



window.mainloop()