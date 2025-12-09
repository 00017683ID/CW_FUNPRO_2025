# A fitness tracker with multiple profiles that stores daily steps, sleep, mood, and weight,
# #  calculates 7-day averages + BMI, and shows history per profile.
# Profile: { name, gender, age, height_cm }
# DailyEntry: { profile_name, date, steps, sleep_hours, mood, weight_kg }

# Notes for documentation the logis is following the fisrt screen to open is the profile one so user in that screen can create a profile 
# then delete a profile or go to the stats of that profile. in order to do so I decided to pack muy rendering of UI of profile screen in a function
# so i could updtae data in the profile screen acroding to added new profiel or deleted ones so every time any btn is pushed 
# idealy i want to make so it destryes old profile screen and crates a new one with updated data

import tkinter as tk
from tkinter import messagebox
from datetime import date

users = [
    {
        "name": "Makhmudjan",
        "gender": "Male",
        "age": 18,
        "height": 175.0,
        'order': 1
    },
    {
        "name": "Malika",
        "gender": "Female",
        'age': 25,
        "height": 165.0,
        "order": 2
    },
        {
        "name": "Malika",
        "gender": "Female",
        'age': 25,
        "height": 165.0,
        "order": 3
    },
        {
        "name": "Malika",
        "gender": "Female",
        'age': 25,
        "height": 165.0,
        "order": 4
    },
        {
        "name": "Malika",
        "gender": "Female",
        'age': 25,
        "height": 165.0,
        "order": 5
    },
        {
        "name": "Malika",
        "gender": "Female",
        'age': 25,
        "height": 165.0,
        "order": 6
    },
        {
        "name": "Malika",
        "gender": "Female",
        'age': 25,
        "height": 165.0,
        "order": 7
    },
        {
        "name": "Malika",
        "gender": "Female",
        'age': 25,
        "height": 165.0,
        "order": 8
    },
        {
        "name": "Malika",
        "gender": "Female",
        'age': 25,
        "height": 165.0,
        "order": 9
    },
        {
        "name": "Malika",
        "gender": "Female",
        'age': 25,
        "height": 165.0,
        "order": 10
    },
        {
        "name": "Malika",
        "gender": "Female",
        'age': 25,
        "height": 165.0,
        "order": 11
    },
        {
        "name": "Malika",
        "gender": "Female",
        'age': 25,
        "height": 165.0,
        "order": 12
    },
]

enteries = [
    {
        "profile_name": "Makhmudjan",
        "date": "2025-12-07",
        "steps": 9500,
        "sleep_hours": 7.5,
        "mood": 1,
        "weight_kg": 68.7,
    },
    {
        "profile_name": "Makhmudjan",
        "date": "2025-12-08",
        "steps": 12340,
        "sleep_hours": 6,
        "mood": 0,
        "weight_kg": 68.5,
    },
    {
        "profile_name": "Makhmudjan",
        "date": "2025-12-09",
        "steps": 8000,
        "sleep_hours": 8,
        "mood": -1,
        "weight_kg": 68.9,
    },
    {
        "profile_name": "Malika",
        "date": "2025-12-07",
        "steps": 4000,
        "sleep_hours": 5,
        "mood": 0,
        "weight_kg": 75.2,
    },
    {
        "profile_name": "Malika",
        "date": "2025-12-08",
        "steps": 10200,
        "sleep_hours": 7,
        "mood": 1,
        "weight_kg": 74.9,
    },
]
current_user= [0]

class profile:
    def __init__(self, user, entries):
        self.name = user['name']
        self.entries = entries
        self.gender = user['gender']
        self.age = user['age']
        self.height_cm = user['height']
    def calculate_bmi(self):
        weight = 0
        for entry in reversed(self.entries):
            if entry['profile_name'] == self.name:
                weight = entry['weight_kg']
                break
        height_m = self.height_cm / 100
        bmi = weight / (height_m ** 2)
        return round(bmi, 2)
    def calculate_averages(self):
        steps = []
        sleep_hours = []
        mood = []
        weight_kg = []
        for entry in reversed(self.entries):
            if entry['profile_name'] == self.name:
                steps.append(entry['steps'])
                sleep_hours.append(entry['sleep_hours'])
                mood.append(entry['mood'])
                weight_kg.append(entry['weight_kg'])
        if steps == [] or sleep_hours == [] or mood == [] or weight_kg == []:
                    return {
            "average_steps": 0,
            "average_sleep": 0,
            "sum_mood": 0,
            "average_weight": 0
            }
        else:
            average_steps = sum(steps[0:6]) / len(steps[0:6])
            average_sleep = sum(sleep_hours[0:6]) / len(sleep_hours[0:6])
            sum_mood = sum(mood[0:6])
            average_weight = sum(weight_kg[0:6]) / len(weight_kg[0:6])

            return {
            "average_steps": round(average_steps, 2),
            "average_sleep": round(average_sleep, 2),
            "sum_mood": sum_mood,
            "average_weight": round(average_weight, 2)
        }


def show_profile_screen():
    profile_screen.tkraise()
def show_statboard_screen():
    statboard_screen.tkraise()
def show_history_screen():
    history_screen.tkraise()


# go to statboard screen function
def statboard_render(user, date, entries): 
    global current_user
    current_user = []
    current_user = profile(user, entries)
    navigation_label.config(text=f"Hello, {current_user.name}, {date}")
    steps_label.config(text=f"Your average steps for last 7 recorded days is: {current_user.calculate_averages()['average_steps']}")
    sleep_label.config(text=f"Your average sleep hours for last 7 recorded days is: {current_user.calculate_averages()['average_sleep']}")
    weight_label.config(text=f"Your average weight for last 7 recorded days is: {current_user.calculate_averages()['average_weight']}")
    bmi_label.config(text=f"Your BMI is {current_user.calculate_bmi()}")
    if current_user.calculate_averages()['sum_mood'] > 2:
        mood_label.config(text="You have been mostly happy in the last 7 recorded days")
    elif current_user.calculate_averages()['sum_mood'] < -2:
        mood_label.config(text="You have been mostly sad in the last 7 recorded days")
    else:
        mood_label.config(text="You have been mostly neutral in the last 7 recorded days")
    suggstions =''
    # BMI suggestions https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html
    if current_user.calculate_bmi() < 18.5:
        suggstions = "You are underweight. Consider a balanced diet with more calories and nutrients to reach a healthier weight " + suggstions
    elif 18.5 <= current_user.calculate_bmi() < 24.9:
        suggstions = "Great job! Keep maintaining a balanced diet and regular exercise to stay healthy " + suggstions
    elif 25 <= current_user.calculate_bmi() < 29.9:
        suggstions = "You are overweight consider a healthy diet and regular exercise to reach a healthier weight " + suggstions
    else:
        suggstions = "You are in the obese range please consult a healthcare professional " + suggstions
    #  steps suggestions https://www.uclahealth.org/news/article/how-many-steps-do-you-need-day-see-health-benefits
    if current_user.calculate_averages()['average_steps'] < 5000:
        suggstions = "Try to increase your daily physical activity. Aim for at least 7,000-8,000 steps per day to improve your overall health " + suggstions
    elif 5000 <= current_user.calculate_averages()['average_steps'] < 7500:
        suggstions = "You're on the right track! Try to reach 10,000 steps daily for optimal health benefits " + suggstions
    else:
        suggstions = "Excellent work on staying active! Keep up the great effort to maintain your health " + suggstions
    # sleep suggestions https://www.sleepfoundation.org/how-sleep-works/how-much-sleep-do-we-really-need
    if current_user.calculate_averages()['average_sleep'] < 7:
        suggstions = "Consider improving your sleep habits to ensure you're getting at least 7-9 hours of quality sleep each night " + suggstions
    elif 7 <= current_user.calculate_averages()['average_sleep'] <= 9:
        suggstions = "Great job on maintaining healthy sleep patterns! " + suggstions
    else:
        suggstions = "While getting enough sleep is important, consistently exceeding 9 hours may indicate underlying health issues " + suggstions
    # mood suggestions
    if current_user.calculate_averages()['sum_mood'] < -2:
        suggstions = "It seems you've been feeling down lately. Try reaching out to friends, family or try to relax more " + suggstions
    elif current_user.calculate_averages()['sum_mood'] > 2:
        suggstions = "It's great to see you're feeling positive! " + suggstions
    else:
        suggstions = "Balanced mood not too happy, not too sad, just right " + suggstions
    bmi_suggestion_label.config(text=suggstions)

    # checking if the current day entry exists
    for entry in entries:
        if entry['profile_name'] == user['name'] and entry['date'] == date:
            date_stat_submit_btn.config(text="Edit Entry")
            steps_input_entry.insert(0, entry['steps'])
            sleep_input_entry.insert(0, entry['sleep_hours'])
            weight_input_entry.insert(0, entry['weight_kg'])
            if entry['mood'] == 1:
                mood_input_radio_happy.select()
            elif entry['mood'] == 0:
                mood_input_radio_neutral.select()
            else:
                mood_input_radio_sad.select()
            break
        else:
            steps_input_entry.delete(0)
            sleep_input_entry.delete(0)
            weight_input_entry.delete(0)

    show_statboard_screen()
def adding_entry():
    steps = steps_input_entry.get()
    sleep = sleep_input_entry.get()
    weight = weight_input_entry.get()
    mood_value = 0
    wrong_input = []
    # input validation
    if steps == "" or sleep == "" or weight == "":
        wrong_input.append("All fields must be filled")
    if not steps.isdigit() or int(steps) < 0:
        wrong_input.append("steps must be a number that is more than 0 or equal to 0")
    if not sleep.isdigit() or float(sleep) < 0 or float(sleep) > 24:
        wrong_input.append("sleep hours must be a number between 0 and 24")
    if not weight.isdigit() or float(weight) <= 0:
        wrong_input.append("weight must be a number that is more than 0")
    if not wrong_input == []:
        tk.messagebox.showerror("Input Error", "\n".join(wrong_input))
        return

    if feeling.get() == "Happy":
        mood_value = 1
    elif feeling.get() == "Neutral":
        mood_value = 0
    else:
        mood_value = -1
    # check if entry for today already exists
    for entry in enteries:
        if entry['profile_name'] == current_user.name and entry['date'] == date.today().isoformat():
            entry['steps'] = int(steps)
            entry['sleep_hours'] = float(sleep)
            entry['weight_kg'] = float(weight)
            entry['mood'] = mood_value
            return
    # if not, create a new entry
    enteries.append({
        "profile_name": current_user.name,
        "date": date.today().isoformat(),
        "steps": int(steps),
        "sleep_hours": float(sleep),
        "weight_kg": float(weight),
        "mood": mood_value
    })
    print(enteries)

    

# profiles loop function for left frame in profile screen
def profile_loop(users_list):
    def profile_delete_btn(index):
        users.pop(index-1)
        # re-ordering the remaining profiles
        for i in range(len(users)):
            users[i]['order'] = i + 1
        # refreshing the profile left screen
        left_frame.destroy()
        profile_loop(users)
    
    left_frame = tk.Frame(profile_screen, bg="#ffffff", width=(400-30), height=570,)
    left_frame.grid( row=0, column=0, padx=15, pady=15, sticky='nsew')
    left_frame.grid_propagate(False)
    left_frame.grid_columnconfigure(0, weight=1)
    left_frame.grid_rowconfigure(1, weight=1)
    left_frame_label = tk.Label(left_frame, text="Profiles", background="#ffffff", font=("inter", 20),)
    left_frame_label.grid(row=0, column=0, pady=(0,10), sticky='ew')
    # scrollable area for profiles https://youtu.be/0WafQCaok6g
    area_frame = tk.Frame(left_frame, bg="#ffffff", width=(400-30), height=500)
    area_frame.grid(row=1, column=0, sticky='nsew',)
    canvas = tk.Canvas(area_frame, bg="#ffffff", width=(400-30),)
    scrollbar = tk.Scrollbar(area_frame, orient="vertical", command=canvas.yview, width=18)
    scrollable_frame = tk.Frame(canvas, bg="#ffffff", width=(400-30),)
    scrollable_frame.bind( "<Configure>", lambda e: canvas.configure( scrollregion=canvas.bbox("all") ) )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
 

    for user in users_list:
        profile_frame =tk.Frame(scrollable_frame, bg='#4A90E2', height=40, width=(380-30))
        profile_frame.grid_propagate(False)
        profile_frame.grid(row=user['order'], column=0, pady=(0,10), sticky='we')
        profile_frame.grid_columnconfigure(0, weight=1)
        profile_label = tk.Label(profile_frame, text=user["name"]+' Age: '+str(user['age']), background="#4A90E2", font=("inter", 10), fg="#ffffff")
        profile_btn_go = tk.Button(profile_frame, text="Go", command=lambda user_data=user: statboard_render(user_data, date.today().isoformat(), enteries), background="#006AE5", font=("inter", 10), fg="#ffffff",)
        profile_btn_delete = tk.Button(profile_frame, text="Delete", command=lambda order=user['order']: profile_delete_btn(order), background="#006AE5", font=("inter", 10), fg="#ffffff",)
        profile_label.grid(row=0, column=0, sticky='w')
        profile_btn_go.grid(row=0, column=1, padx=5, pady=5 ,sticky='e')
        profile_btn_delete.grid(row=0, column=2,padx=5, pady=5, sticky='e')

def create_profile():
    gender = str(gender_var.get())
    name = right_frame_name_entry.get()
    age = right_frame_age_entry.get()
    height = right_frame_height_entry.get()
    if name == "" or age == "" or height == "":
        right_frame_error_label.config(text="Please fill in all the fields to create a profile")
    elif name.isspace() or age.isspace() or height.isspace():
        right_frame_error_label.config(text="Fields cannot be just spaces")
    elif len(name) < 3:
        right_frame_error_label.config(text="Name must be at least 3 characters long")
    elif len(name) > 30:
        right_frame_error_label.config(text="Name cannot be longer than 30 characters")
    elif any(char.isdigit() for char in name):
        right_frame_error_label.config(text="Name cannot contain numbers.")
    elif any(not char.isalnum() and char != ' ' for char in name):
        right_frame_error_label.config(text="Name cannot contain special characters or spaces")
    elif not age.isdigit() or int(age) <= 0:
        right_frame_error_label.config(text="Please enter a number and it is positive for age field")
    elif float(age) <= 0:
        right_frame_error_label.config(text="Common, you can't be less than 1 year old!")
    elif float(age) > 120:
        right_frame_error_label.config(text="Don't lie you cannot be that old unless you are Ethel Caterham")
    elif not height.isdigit():
        right_frame_error_label.config(text="Please enter a number and it is positive for height field")
    elif float(height) < 50:
        right_frame_error_label.config(text="Height cannot be less than 50 cm")
    elif float(height) > 350:
        right_frame_error_label.config(text="Height cannot be more than 350 cm")
    elif any((user['name'].lower() == name.lower() for user in users)):
        right_frame_error_label.config(text="This user is already in the system")
    else:
        print(gender, name, age, height)
        users.append({
                "name": name,
                "gender": gender
                ,"age": int(age),
                "height": float(height),
                'order': len(users) + 1
            })
        profile_loop(users)
        right_frame_error_label.config(text="NEW USER IS ADDED")
        right_frame_name_entry.delete(0, tk.END)
        right_frame_age_entry.delete(0, tk.END)
        right_frame_height_entry.delete(0, tk.END)
        gender_var.set("Male")

    


#GUI with Tkinter

root = tk.Tk()
root.configure(bg="#f0f0f0")
root.title("Fitness Tracker")
root.resizable(False, False)
root.geometry("800x600")
# Variables needed for radion checkboxes
gender_var = tk.StringVar(value="Male")
feeling = tk.StringVar(value="Neutral")
### Profile Screen ###

profile_screen = tk.Frame(root, bg="#f0f0f0", width=800, height=600)
profile_screen.grid_propagate(False)
profile_screen.grid(row=0, column=0, sticky='nsew')



#left frame content and its profiles lists
profile_loop(users)

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
right_frame_gender_radio_male = tk.Radiobutton(right_frame_gender, text="Male", variable=gender_var , value="Male", font=("inter", 12), bg='#4A90E2', fg="#ffffff", selectcolor="#3772B5")
right_frame_gender_radio_female = tk.Radiobutton(right_frame_gender, text="Female", variable=gender_var , value="Female", font=("inter", 12), bg='#4A90E2', fg="#ffffff",selectcolor='#3772B5')         
right_frame_gender_radio_female.grid(row=0, column=2, padx=5, pady=5, sticky='e')
right_frame_gender_radio_male.grid(row=0, column=1, padx=10, pady=5, sticky='e')

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
right_frame_create_btn = tk.Button(right_frame, text="Create Profile", command=create_profile, background="#136FDA", font=("inter", 15, "bold"), fg="#000000",)
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
navigation_btn_profile = tk.Button(navigation_frame, text="Back to profiles", command=show_profile_screen, background="#006AE5", font=("inter", 16), fg="#000000", height=1, width=15)
navigation_btn_profile.grid(row=0, column=1, padx=15, pady=5 ,sticky='e')

# left stats_frame 
stats_frame = tk.Frame(statboard_screen, bg="#ffffff", width=(400-30), height=300,)
stats_frame.grid( row=1, column=0, padx=15, pady=15, sticky='wn')
stats_frame.grid_propagate(False)

steps_frame = tk.Frame(stats_frame, bg='#4A90E2', height=60, width=(400-20))
steps_frame.grid(row=0, column=0, pady=(0,20), sticky='we')
steps_frame.grid_propagate(False)
steps_frame.grid_columnconfigure(0, weight=1)
steps_label = tk.Label(steps_frame, text="Steps Today: 10,000 dfdf  dfd f  df", background="#4A90E2", font=("inter", 10), fg="#ffffff")
steps_label.grid(row=0, column=0, sticky='w', padx=5, pady=10)

sleep_frame = tk.Frame(stats_frame, bg='#4A90E2', height=60, width=(400-20))
sleep_frame.grid(row=1, column=0, pady=(0,20), sticky='we')
sleep_frame.grid_propagate(False)
sleep_frame.grid_columnconfigure(0, weight=1)
sleep_label = tk.Label(sleep_frame, text="Sleep Today: 10,000 dfdf  dfd f  df", background="#4A90E2", font=("inter", 10), fg="#ffffff")
sleep_label.grid(row=1, column=0, sticky='w', padx=5, pady=10)

mood_frame = tk.Frame(stats_frame, bg='#4A90E2', height=60, width=(400-20))
mood_frame.grid(row=3, column=0, pady=(0,20), sticky='we')
mood_frame.grid_propagate(False)
mood_frame.grid_columnconfigure(0, weight=1)
mood_label = tk.Label(mood_frame, text="feeling Today: 10,000 dfdf  dfd f  df", background="#4A90E2", font=("inter", 10), fg="#ffffff")
mood_label.grid(row=3, column=0, sticky='w', padx=5, pady=10)

weight_frame = tk.Frame(stats_frame, bg='#4A90E2', height=60, width=(400-20))
weight_frame.grid(row=4, column=0, sticky='we')
weight_frame.grid_propagate(False)
weight_frame.grid_columnconfigure(0, weight=1)
weight_label = tk.Label(weight_frame, text="Weight Today: 10,000 dfdf  dfd f  df", background="#4A90E2", font=("inter", 10), fg="#ffffff")
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
mood_input_radio_happy = tk.Radiobutton(mood_input_frame, text="Happy", variable=feeling, value="Happy", font=("inter", 12), bg='#4A90E2', fg="#ffffff", selectcolor='#3772B5')
mood_input_radio_happy.grid(row=0, column=1, padx=3, pady=5, sticky='e')
mood_input_radio_neutral = tk.Radiobutton(mood_input_frame, text="Neutral", variable=feeling, value="Neutral", font=("inter", 12), bg='#4A90E2', fg="#ffffff", selectcolor='#3772B5')
mood_input_radio_neutral.grid(row=0, column=2, padx=3, pady=5, sticky='e')
mood_input_radio_sad = tk.Radiobutton(mood_input_frame, text="Sad", value="Sad", variable=feeling, font=("inter", 12), bg='#4A90E2', fg="#ffffff", selectcolor='#3772B5')
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

date_stat_submit_btn = tk.Button(date_stat_frame, text="Submit Entry", command=adding_entry, background="#136FDA", font=("inter", 16, "bold"), fg="#000000", height=1)
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

### history screen ###

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
history_nav_btn_statboard = tk.Button(history_nav_frame, text="Back to Stats", command=show_statboard_screen, background="#006AE5", font=("inter", 16), fg="#000000", height=1, width=15)
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

### end of history screen ###

show_profile_screen()

root.mainloop()