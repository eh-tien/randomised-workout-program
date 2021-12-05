# Import necessary libraries
import pandas as pd
import numpy as np
from twilio.rest import Client

# Create lists of exercises, sets, reps
reps = [8,10,12]

sets = [3,4,5]

# Create lists of all exercises 
leg_exercises = ['Leg press', 
                 'Romanian deadlifts',
                 'Trap bar deadlifts',
                 'Squats',
                 'Hamstring curls',
                 'Calf raises',
                 'Seated leg curl',
                 'Lunges',
                 'Hamstring raise machine',
                 'Squat machine']

chest_exercises = ['Flat bench',
                   'Incline bench',
                   'Dumbell press (Flat)',
                   'Dumbell press (Incline)',
                   'Chest flys (Upper)',
                   'Chest flys (Lower)',
                   'Pushups']

tricep_exercises = ['Tricep pushdowns (Rope)',
                    'Tricep pushdowns (Bar)',
                    'Seated shoulder press',
                    'Tricep dips',
                    'Seated shoulder raises']

bicep_exercises = ['Standing barbell curls',
                   'One hand seated curls',
                   'Hammer curls',
                   'Preacher curls']

back_exercises = ['Seated rows',
                  'Lat pulldown',
                  'Rear delt flys',
                  'Bent over rows',
                  'Shrugs',
                  'One hand lat pulldowns',
                  'Rear delt flys (cable)',
                  'Standing barbell raises']

extra_exercises = ['Oblique raises',
                'Crunches',
                'Seated crunches',
                'Swinging leg raises',
                'Running']


# Create function that chooses random values from lists
def create_reps_sets(array):
    
    randomised_reps_sets = np.random.choice(array, 6)
    
    return randomised_reps_sets

# Create push and pull exercise routines
def create_exercises(main_exercise1, main_exercise2, extra_exercises = extra_exercises):
    
    _ = np.random.choice(main_exercise1, 3, replace = False)
    randomised_exercises1 = np.append(_ , np.random.choice(main_exercise2, 2, replace= False))
    randomised_exercises2 = np.append(randomised_exercises1, np.random.choice(extra_exercises))
    
    return randomised_exercises2

# Create leg exercise routine 
def create_leg_exercises(main_exercise1, extra_exercises = extra_exercises):
    
    _ = np.random.choice(main_exercise1, 5, replace = False)
    randomised_exercises2 = np.append(_, np.random.choice(extra_exercises))
    
    return randomised_exercises2


# Ask user what type of exercise they want to do that day 
exercises = input('What do you want to work today? (Push / Pull / Legs): ').lower()

# Depending on what type of exercise the user wants, the appropriate plan will be made for them here
if exercises == 'legs':
     daily_exercises = create_leg_exercises(leg_exercises)
elif exercises == 'push':
    daily_exercises = create_exercises(chest_exercises, tricep_exercises)
elif exercises == 'pull':
    daily_exercises = create_exercises(back_exercises, bicep_exercises)
        
# Creating dataframe and converting to numpy array 
daily_sets = create_reps_sets(sets)
daily_reps = create_reps_sets(reps)
dataframe = pd.DataFrame(daily_exercises)
dataframe['Sets'] = daily_sets
dataframe['Reps'] = daily_reps
array = np.array(dataframe)

# Creating string out of array to be able to send using the Twilio API
master_str = []

for i in array:
    master_str.append(f'{i[0]}, Sets: {i[1]}, Reps: {i[2]} ######################')

# Adding Sven presses to on average, half of all chest workouts
rand_int = 10*np.random.random()

if exercises == 'push' and rand_int > 0.4:
    master_str.append('Sven presses, Sets: 4, Reps: 8 (Between sets)')

# Use Twilio API to send workout program to phone
client = Client('USERNAME', 'PASSWORD' )
message = client.messages.create(
                              body= str(master_str),
                              from_='YOUR TWILIO NUMBER',
                              to='PHONE NUMBER YOU WANT TO SEND PROGRAM TO')

# Print text to terminal to let user know message has been sent
print('Workout program has been sent to phone')