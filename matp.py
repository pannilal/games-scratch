import matplotlib.pyplot as plt
import tkinter
from tkinter.constants import *

tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=1)
label = tkinter.Label(frame, text="Hello! I  am Praneel ")
label1 = tkinter.Label(frame, text="this is my 1 gui ")
frame1 = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame1.pack(fill=BOTH, expand=2)


def M():
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 35, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]
    men_std = [2, 3, 4, 1, 2]
    women_std = [3, 5, 2, 3, 3]
    width = 0.35

    fig, ax = plt.subplots()

    ax.bar(labels, men_means, width, yerr=men_std, label='Men')
    ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
           label='Women')

    ax.set_ylabel('Scores')
    ax.set_title('Scores in a football match')
    ax.legend()

    plt.show()


def anik():
    import numpy as np

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Example data
    people = ('navin', 'navin', 'mansi', 'anika')
    y_pos = np.arange(len(people))
    performance = 3 + 10 * np.random.rand(len(people))
    error = np.random.rand(len(people))

    ax.barh(y_pos, performance, xerr=error, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Performance')
    ax.set_title('How fast do you want to go today?')

    plt.show()


def an():
    import numpy as np
    import matplotlib.pyplot as plt

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # Compute areas and colors
    N = 150
    r = 2 * np.random.rand(N)
    theta = 2 * np.pi * np.random.rand(N)
    area = 200 * r ** 2
    colors = theta

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)


label.pack(fill=X, expand=1)
label1.pack(fill=X, expand=2)
button = tkinter.Button(frame, text="football score", command=M)
button.pack(side=BOTTOM)
button = tkinter.Button(frame1, text="Exit", command=tk.destroy)
button.pack(side=BOTTOM)
button = tkinter.Button(frame, text="speed of people", command=anik)
button.pack(side=BOTTOM)
button = tkinter.Button(frame, text="pie chart", command=an)
button.pack(side=BOTTOM)

tk.mainloop()
