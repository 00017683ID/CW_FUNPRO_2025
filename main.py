# A fitness tracker with multiple profiles that stores daily steps, sleep, mood, and weight,
# #  calculates 7-day averages + BMI, and shows history per profile.
# Profile: { name, gender, age, height_cm }
# DailyEntry: { profile_name, date, steps, sleep_hours, mood, weight_kg }


import tkinter as tk


#GUI with Tkinter

root = tk.Tk()
root.configure(bg="#f0f0f0")
root.title("Fitness Tracker")
root.resizable(False, False)
root.geometry("800x600")

profile_screen = tk.Frame(root, bg="#f0f0f0", width=800, height=600)
profile_screen.grid_propagate(False)
profile_screen.grid(row=0, column=0, sticky='nsew')



#left frame content
left_frame = tk.Frame(profile_screen, bg="#ffffff", width=(400-30), height=570,)
left_frame.grid( row=0, column=0, padx=15, pady=15, sticky='nsew')
left_frame.grid_propagate(False)
left_frame_label = tk.Label(left_frame, text="Profiles", background="#ffffff", font=("inter", 20),)
left_frame_label.grid(row=0, column=0, pady=(0,10), sticky='ew')
profile_frame =tk.Frame(left_frame, bg='#4A90E2', height=40, width=(400-30))
profile_frame.grid_propagate(False)
profile_frame.grid(row=1, column=0, pady=(0,10), sticky='we')
profile_frame.grid_columnconfigure(0, weight=1)
profile_label = tk.Label(profile_frame, text="Profile,dfjsndfjdf,dfjdjfdf", background="#4A90E2", font=("inter", 10), fg="#ffffff")
profile_btn_go = tk.Button(profile_frame, text="Go", background="#006AE5", font=("inter", 10), fg="#ffffff",)
profile_btn_delete = tk.Button(profile_frame, text="Delete", background="#006AE5", font=("inter", 10), fg="#ffffff",)
profile_label.grid(row=0, column=0, sticky='w')
profile_btn_go.grid(row=0, column=1, padx=5, pady=5 ,sticky='e')
profile_btn_delete.grid(row=0, column=2,padx=5, pady=5, sticky='e')

# right frame content
right_frame = tk.Frame(profile_screen, bg="#ffffff", width=(400-30), height=570,)
right_frame.grid( row=0, column=1, padx=15, pady=15,sticky='nsew')
right_frame.grid_propagate(False)
right_frame.grid_columnconfigure(0, weight=1)
right_frame_label = tk.Label(right_frame, text="Create a new Profile", background="#ffffff", font=("inter", 20),)
right_frame_label.grid(row=0, column=0, pady=(0,10), sticky='ew')
right_frame_name = tk.Frame(right_frame, bg='#4A90E2', height=40, width=(400-30))
#right frame name input
right_frame_name.grid(row=1, column=0, pady=(0,10), sticky='we')
right_frame_name.grid_propagate(False)
right_frame_name.grid_columnconfigure(0, weight=1)
right_frame_name_label = tk.Label(right_frame_name, text="Name:", background="#4A90E2", font=("inter", 20), fg="#ffffff")
right_frame_name_label.grid(row=0, column=0, sticky='w', padx=5)
right_frame_name_entry = tk.Entry(right_frame_name, font=("inter", 15)) 
right_frame_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')
#right frame gender radio buttons
right_frame_gender = tk.Frame(right_frame, bg='#4A90E2', height=40, width=(400-30))
right_frame_gender.grid(row=2, column=0, pady=(0,10), sticky='we')
right_frame_gender.grid_propagate(False)
right_frame_gender.grid_columnconfigure(1, weight=1)
right_frame_gender_label = tk.Label(right_frame_gender, text="Gender:", background="#4A90E2", font=("inter", 20), fg="#ffffff")
right_frame_gender_label.grid(row=0, column=0, sticky='w', padx=5)
right_frame_gender_radio_male = tk.Radiobutton(right_frame_gender, text="Male", value="Male", font=("inter", 12), bg='#4A90E2', fg="#ffffff")
right_frame_gender_radio_male.grid(row=0, column=1, padx=10, pady=5, sticky='e')
right_frame_gender_radio_female = tk.Radiobutton(right_frame_gender, text="Female", value="Female", font=("inter", 12), bg='#4A90E2', fg="#ffffff")         
right_frame_gender_radio_female.grid(row=0, column=2, padx=5, pady=5, sticky='e')

# right frame age input
right_frame_age = tk.Frame(right_frame, bg='#4A90E2', height=40, width=(400-30))
right_frame_age.grid(row=3, column=0, pady=(0,10), sticky='we')
right_frame_age.grid_propagate(False)
right_frame_age.grid_columnconfigure(1, weight=1)
right_frame_age_label = tk.Label(right_frame_age, text="Age:", background="#4A90E2", font=("inter", 20), fg="#ffffff")
right_frame_age_label.grid(row=0, column=0, sticky='w', padx=5)
right_frame_age_entry = tk.Entry(right_frame_age, font=("inter", 15)) 
right_frame_age_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

# right frame height input
right_frame_height = tk.Frame(right_frame, bg='#4A90E2', height=40, width=(400-30))
right_frame_height.grid(row=4, column=0, pady=(0,10), sticky='we')
right_frame_height.grid_propagate(False)
right_frame_height.grid_columnconfigure(1, weight=1)
right_frame_height_label = tk.Label(right_frame_height, text="Height (cm):", background="#4A90E2", font=("inter", 15), fg="#ffffff")
right_frame_height_label.grid(row=0, column=0, sticky='w', padx=5)
right_frame_height_entry = tk.Entry(right_frame_height, font=("inter", 15)) 
right_frame_height_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

# inpput validation error feild
right_frame.grid_rowconfigure(5, weight=1)
right_frame_error = tk.Frame(right_frame, background="#ffffff" )
right_frame_error.grid(row=5, column=0, pady=5, sticky='nwse')
right_frame_error.grid_propagate(False)
right_frame_error.grid_columnconfigure(0, weight=1)
right_frame_error_label = tk.Label(right_frame_error, text="", background="#ffffff", font=("inter", 12), fg="#505050", wraplength=355, justify='left')
right_frame_error_label.grid(row=0, column=0, sticky='w', padx=5)

# right frame create profile button
right_frame_create_btn = tk.Button(right_frame, text="Create Profile", background="#136FDA", font=("inter", 15, "bold"), fg="#000000",)
right_frame_create_btn.grid(row=6, column=0, pady=10, sticky='ew', padx=40)







root.mainloop()