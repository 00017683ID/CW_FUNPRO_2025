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
### Profile Screen ###
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
right_frame_create_btn.grid(row=6, column=0, pady=10, sticky='wn', padx=40)

### end of a profile screen ###

### statboard screen ###
statboard_screen = tk.Frame(root, bg="#f0f0f0", width=800, height=600)
statboard_screen.grid(row=0, column=0, sticky='nsew')
statboard_screen.grid_propagate(False)
statboard_screen.grid_columnconfigure(0, weight=1)
statboard_screen.grid_columnconfigure(1, weight=1)


# navigation 
navigation_frame = tk.Frame(statboard_screen, bg="#f0f0f0", width=800, height=50)
navigation_frame.grid(row=0, column=0, columnspan=2, sticky='ew')
navigation_frame.grid_propagate(False)
navigation_frame.grid_columnconfigure(0, weight=1)
navigation_label = tk.Label(navigation_frame, text="Hello, Makhmudjan, June 11 2005", background="#f0f0f0", font=("inter", 20),)
navigation_label.grid(row=0, column=0, sticky='w', padx=15)
navigation_btn_profile = tk.Button(navigation_frame, text="Back to profiles", background="#006AE5", font=("inter", 16), fg="#000000", height=1, width=15)
navigation_btn_profile.grid(row=0, column=1, padx=15, pady=5 ,sticky='e')

# left stats_frame 
stats_frame = tk.Frame(statboard_screen, bg="#ffffff", width=(400-30), height=300,)
stats_frame.grid( row=1, column=0, padx=15, pady=15, sticky='wn')
stats_frame.grid_propagate(False)

steps_frame = tk.Frame(stats_frame, bg='#4A90E2', height=60, width=(400-20))
steps_frame.grid(row=0, column=0, pady=(0,20), sticky='we')
steps_frame.grid_propagate(False)
steps_frame.grid_columnconfigure(0, weight=1)
steps_label = tk.Label(steps_frame, text="Steps Today: 10,000 dfdf  dfd f  df", background="#4A90E2", font=("inter", 14), fg="#ffffff")
steps_label.grid(row=0, column=0, sticky='w', padx=5, pady=10)

sleep_frame = tk.Frame(stats_frame, bg='#4A90E2', height=60, width=(400-20))
sleep_frame.grid(row=1, column=0, pady=(0,20), sticky='we')
sleep_frame.grid_propagate(False)
sleep_frame.grid_columnconfigure(0, weight=1)
sleep_label = tk.Label(sleep_frame, text="Sleep Today: 10,000 dfdf  dfd f  df", background="#4A90E2", font=("inter", 14), fg="#ffffff")
sleep_label.grid(row=1, column=0, sticky='w', padx=5, pady=10)

mood_frame = tk.Frame(stats_frame, bg='#4A90E2', height=60, width=(400-20))
mood_frame.grid(row=3, column=0, pady=(0,20), sticky='we')
mood_frame.grid_propagate(False)
mood_frame.grid_columnconfigure(0, weight=1)
mood_label = tk.Label(mood_frame, text="feeling Today: 10,000 dfdf  dfd f  df", background="#4A90E2", font=("inter", 14), fg="#ffffff")
mood_label.grid(row=3, column=0, sticky='w', padx=5, pady=10)

weight_frame = tk.Frame(stats_frame, bg='#4A90E2', height=60, width=(400-20))
weight_frame.grid(row=4, column=0, sticky='we')
weight_frame.grid_propagate(False)
weight_frame.grid_columnconfigure(0, weight=1)
weight_label = tk.Label(weight_frame, text="Weight Today: 10,000 dfdf  dfd f  df", background="#4A90E2", font=("inter", 14), fg="#ffffff")
weight_label.grid(row=4, column=0, sticky='w', padx=5, pady=10)

# dates stat input frame
date_stat_frame = tk.Frame(statboard_screen, bg="#ffffff", width=(400-30), height=300,)
date_stat_frame.grid( row=1, column=1, padx=15, pady=15, sticky='en')
date_stat_frame.grid_propagate(False)
date_stat_frame.grid_columnconfigure(0, weight=1)

steps_input_frame = tk.Frame(date_stat_frame, bg='#4A90E2', height=50, width=(400-20))
steps_input_frame.grid(row=0, column=0, pady=(0,10), sticky='we')
steps_input_frame.grid_propagate(False)
steps_input_frame.grid_columnconfigure(1, weight=1)
steps_input_label = tk.Label(steps_input_frame, text="This day's steps:", background="#4A90E2", font=("inter", 14), fg="#ffffff")
steps_input_label.grid(row=0, column=0, sticky='w', padx=5, pady=10)
steps_input_entry = tk.Entry(steps_input_frame, font=("inter", 15))
steps_input_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

sleep_input_frame = tk.Frame(date_stat_frame, bg='#4A90E2', height=50, width=(400-20))
sleep_input_frame.grid(row=1, column=0, pady=(0,10), sticky='we')
sleep_input_frame.grid_propagate(False)     
sleep_input_frame.grid_columnconfigure(1, weight=1)
sleep_input_label = tk.Label(sleep_input_frame, text="This day's sleep (hrs):", background="#4A90E2", font=("inter", 14), fg="#ffffff")
sleep_input_label.grid(row=0, column=0, sticky='w', padx=5, pady=10)
sleep_input_entry = tk.Entry(sleep_input_frame, font=("inter", 15)) 
sleep_input_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

mood_input_frame = tk.Frame(date_stat_frame, bg='#4A90E2', height=50, width=(400-20))
mood_input_frame.grid(row=2, column=0, pady=(0,10), sticky='we')
mood_input_frame.grid_propagate(False)
mood_input_frame.grid_columnconfigure(1, weight=1)
mood_input_frame.grid_columnconfigure(2, weight=1)
mood_input_label = tk.Label(mood_input_frame, text="This day's mood:", background="#4A90E2", font=("inter", 14), fg="#ffffff")
mood_input_radio_happy = tk.Radiobutton(mood_input_frame, text="Happy", value="Happy", font=("inter", 12), bg='#4A90E2', fg="#ffffff")
mood_input_radio_happy.grid(row=0, column=1, padx=3, pady=5, sticky='e')
mood_input_radio_neutral = tk.Radiobutton(mood_input_frame, text="Neutral", value="Neutral", font=("inter", 12), bg='#4A90E2', fg="#ffffff")
mood_input_radio_neutral.grid(row=0, column=2, padx=3, pady=5, sticky='e')
mood_input_radio_sad = tk.Radiobutton(mood_input_frame, text="Sad", value="Sad", font=("inter", 12), bg='#4A90E2', fg="#ffffff")
mood_input_radio_sad.grid(row=0, column=3, padx=3, pady=5, sticky='e')
mood_input_label.grid(row=0, column=0, sticky='w', padx=5, pady=10)

weight_input_frame = tk.Frame(date_stat_frame, bg='#4A90E2', height=50, width=(400-20))
weight_input_frame.grid(row=3, column=0, sticky='we')
weight_input_frame.grid_propagate(False)
weight_input_frame.grid_columnconfigure(1, weight=1)
weight_input_label = tk.Label(weight_input_frame, text="This day's weight (kg):", background="#4A90E2", font=("inter", 14), fg="#ffffff")
weight_input_label.grid(row=0, column=0, sticky='w', padx=5, pady=10)
weight_input_entry = tk.Entry(weight_input_frame, font=("inter", 15))
weight_input_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

date_stat_submit_btn = tk.Button(date_stat_frame, text="Submit Entry", background="#136FDA", font=("inter", 16, "bold"), fg="#000000", height=1)
date_stat_submit_btn.grid(row=4, column=0, sticky='WENS', pady=(20,0), padx=20)

# BMI and text suggestion frame
bmi_frame = tk.Frame(statboard_screen, bg="#ffffff", width=(800-30), height=200,)
bmi_frame.grid( row=2, column=0, columnspan=2, padx=15, pady=5, sticky='nsew')
bmi_frame.grid_propagate(False)
bmi_frame.grid_columnconfigure(0, weight=1)
bmi_frame.grid_rowconfigure(1, weight=1)
bmi_label = tk.Label(bmi_frame, text="Your BMI is 22.5 - Normal weight", background="#ffffff", font=("inter", 15),)
bmi_label.grid(row=0, column=0, sticky='w', padx=15, pady=5)
bmi_suggestion_label = tk.Label(bmi_frame, text="Great job! Keep maintaining a balanced diet and regular exercise to stay healthy. rwerwe wer we rwe rw er wer we rw rew er wer we fs dv erg aegt kjrt gkjt kghj atkha tkh tk", background="#ffffff", font=("inter", 12), wraplength=720, justify='left')
bmi_suggestion_label.grid(row=1, column=0, sticky='wn', padx=15)

# BTN to refer to history screen
history_btn = tk.Button(bmi_frame, text="View History", background="#136FDA", font=("inter", 16, "bold"), fg="#000000", height=1)
history_btn.grid(row=2, column=0, sticky='e', padx=15, pady=(0, 10))

### end of statboard screen ###

# history screen

history_screen = tk.Frame(root, bg="#f0f0f0", width=800, height=600)
history_screen.grid(row=0, column=0, sticky='nsew')
history_screen.grid_propagate(False)
history_screen.grid_columnconfigure(0, weight=1)

history_nav_frame = tk.Frame(history_screen, bg="#f0f0f0", width=800, height=50)
history_nav_frame.grid(row=0, column=0, sticky='ew')
history_nav_frame.grid_propagate(False)
history_nav_frame.grid_columnconfigure(0, weight=1)
history_nav_label = tk.Label(history_nav_frame, text="Select a date you want to know more about and edit", background="#f0f0f0", font=("inter", 16),)
history_nav_label.grid(row=0, column=0, sticky='w', padx=15)
history_nav_btn_statboard = tk.Button(history_nav_frame, text="Back to Stats", background="#006AE5", font=("inter", 16), fg="#000000", height=1, width=15)
history_nav_btn_statboard.grid(row=0, column=1, padx=15, pady=5 ,sticky='e')

history_list_container = tk.Frame(history_screen, bg="#ffffff", width=(800-30), height=500,)
history_list_container.grid( row=1, column=0, padx=15, pady=15, sticky='nsew')
history_list_container.grid_propagate(False)
history_list_container.grid_columnconfigure(0, weight=1)

# units loop here
history_list_frame = tk.Frame(history_list_container, bg="#4A90E2", width=(800-60), height=50,)
history_list_frame.grid_propagate(False)
history_list_frame.grid_columnconfigure(0, weight=1)
history_list_frame.grid(row=0, column=0, pady=(0,5), sticky='we')
history_list_label = tk.Label(history_list_frame, text="History Entries ahsdhasvdha asgdvgasdvg gasvdgs", background="#4A90E2", font=("inter", 14),)
history_list_label.grid(row=0, column=0, sticky='w', pady=5, padx=5)
history_btn_view = tk.Button(history_list_frame, text="View and Edit", background="#006AE5", font=("inter", 10), fg="#000000",)
history_btn_view.grid(row=0, column=1, padx=5, pady=5 ,sticky='e')







root.mainloop()