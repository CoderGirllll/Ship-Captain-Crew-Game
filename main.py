import tkinter as tk
from functions import dice_display
from PIL import Image, ImageTk

#Main Program
root = tk.Tk()

root.attributes("-fullscreen", True)
root.title("Ship, Captain, Crew Game")

#Adding Backdrop
bg_image = Image.open("Styles\Background.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#Label for game title
title = tk.Label(root, text="SHIP, CAPTAIN, CREW!", font=("Roman", 60)).pack()

#Button to roll the dice
roll = tk.Button(root, text="ROLL THE DICE", font=("san-serif", 25), command=lambda:dice_display(dice, score)).place(x = 640, y = 400)

#Label for dice roll
dice = tk.Label(root, font=("san-serif", 120))

score = tk.Label(root, font=("san-serif", 40))

#Exit Button
exit = tk.Button(root, text="EXIT", font=("san-serif", 20), command=lambda:quit()).place(x = 730, y = 750)

root.mainloop()