# A fitness tracker with multiple profiles that stores daily steps, sleep, mood, and weight,
# #  calculates 7-day averages + BMI, and shows history per profile.
# Profile: { name, gender, age, height_cm }
# DailyEntry: { profile_name, date, steps, sleep_hours, mood, weight_kg }


import tkinter as tk


#GUI with Tkinter

root = tk.Tk(bg='#F5F7FA')
root.title("Fitness Tracker")
root.geometry("700x500")
root.left_frame = tk.Frame(root, bg="#ffffff", width= calc(700/2 - 32), height=470, )
root.left_frame.pack(side='left', fill='both', expand=True)

root.mainloop()