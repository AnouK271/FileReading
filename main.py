# Description: Culminating
# Author: Anousha Khan
# Date of last edit: January 9, 2023

from myData import data

# Custom function
# calculate_total_reps(lst) -> int
# returns total number of reps across all pairs
def calculate_total_reps(rep_pairs):
  return sum(rp[0] for rp in rep_pairs)

# print(data)

# Q1
# to_kg(int) -> float
# converts an integer from pounds to kg
def to_kg(x):
  return x*0.453592

# Tests
assert to_kg(100) == 45.3592
assert to_kg(50) == 22.6796
assert to_kg(25) == 11.3398

# Q2
# get_names(dictionary) -> list
#  Return a list of all the names that have recorded a workout
def get_names(lst):
  names = []
  for i in lst:
    # Appending the 'name' value of each dictionary to the names list
    names.append(i['name'])
  return names

print(get_names(data))

# Tests
assert get_names(data) == ['Bob Anderson', 'Tim Timothy', 'Alice Johnson', 'John Smith', 'Emily Davis', 'Chris Brown', 'Emma White', 'David Green', 'Olivia Miller', 'Ryan Taylor']

# Q3
# get_excercises(list of dictionaries, str, str) -> list of str
# Return a list of all the exercise names performed by name on date
def get_exercises(lst, name, date):
  exercises = []
  for person in lst:
    # Checking if the 'name' value of the dictionary matches the provided name
    if person['name'] == name:
      for work in person['workouts']:
        # Checking if the 'date' value of the workout matches the provided date
        if work['date'] == date:
          # Appending the 'exercise' value of the workout to the exercises list
          exercises.append(work['exercise'])
  return exercises

print(get_exercises(data, "Tim Timothy", "10-12-2010"))
print(get_exercises(data, 'Olivia Miller', '04-05-2017'))
print(get_exercises(data, 'David Green', '09-20-2016'))

# Tests
assert get_exercises(data, "Tim Timothy", "10-12-2010") == ['Squats']
assert get_exercises(data, 'Olivia Miller', '04-05-2017') == ['Planks']
assert get_exercises(data, 'David Green', '09-20-2016') == ['Bench Press']

# Q4
# get_excercise_set(list of dictionaries, str, str, str) -> list of dictionaries
# Returns a list representing the sets of exercise_name performed by name on date
def get_exercise_set(lst, name, date, exercise_name):
  sets = []
  for person in lst:
    if person['name'] == name:
      for work in person['workouts']:
# Checking if the 'date' value of the workout matches the provided date and the 'exercise' value matches the provided exercise_name
        if work['date'] == date and work['exercise'] == exercise_name:
          for rp in work['repPairs']:
            # Appending a dictionary to the sets list with 'weight' and 'rep' keys
            sets.append({'weight': float(rp[1][:-2]), 'rep': int(rp[0])})
  return sets

print(get_exercise_set(data, "Alice Johnson", "05-20-2011", "Deadlifts"))
print(get_exercise_set(data, 'Emma White', '06-12-2015', 'Pull ups'))
print(get_exercise_set(data, 'David Green', '09-20-2016', 'Bench Press'))

# Tests
assert get_exercise_set(data, "Alice Johnson", "05-20-2011", "Deadlifts") == [{'weight': 0.0, 'rep': 8}, {'weight': 30.0, 'rep': 8}, {'weight': 60.0, 'rep': 8}]
assert get_exercise_set(data, 'Emma White', '06-12-2015', 'Pull ups') == [{'weight': 0.0, 'rep': 10}, {'weight': 0.0, 'rep': 10}, {'weight': 0.0, 'rep': 10}]
assert get_exercise_set(data, 'David Green', '09-20-2016', 'Bench Press') == [{'weight': 0.0, 'rep': 10}, {'weight': 30.0, 'rep': 10}, {'weight': 60.0, 'rep': 10}]

# Q5
# get_workout(list of dictionaries,str, str) -> list of str
# Returns a representation of the workout performed by name on date
def get_workout(lst, name, date):
 workouts = []
 for i in lst:
  if i['name'] == name:
    for w in i['workouts']:
      if w['date'] == date:
        total_reps = calculate_total_reps(w['repPairs'])
        # Creating a string that represents the workout
        work_get = f"On {w['date']}, {name} did {total_reps} reps of {w['exercise']}"
        # Appending the workout string to the workouts list
        workouts.append(work_get)
 return workouts


print(get_workout(data, "Alice Johnson", "05-20-2011"))
print(get_workout(data, "Emma White", '06-12-2015'))
print(get_workout(data, 'Chris Brown', '12-01-2014'))

# Tests
assert get_workout(data, "Alice Johnson", "05-20-2011") == ['On 05-20-2011, Alice Johnson did 24 reps of Deadlifts']
assert get_workout(data, "Emma White", '06-12-2015') == ['On 06-12-2015, Emma White did 30 reps of Pull ups']
assert get_workout(data, 'Chris Brown', '12-01-2014') == ['On 12-01-2014, Chris Brown did 36 reps of Bicep Curls']

# Q6
# max_weight_set(list of dictionaries,str) -> dictionary
# Return the name and date of person with highest exercise weight single set
# of exercise_name, and exercise weight of the set
def max_weight_set(lst, exercise_name):
  max_weight = 0
  max_set = None
  for i in lst:
    for w in i['workouts']:
      if w['exercise'] == exercise_name:
        for rp in w['repPairs']: 
          weight = int(rp[1][:-2]) # Extract the weight from the repPair
          if weight > max_weight:
            max_weight = weight # Update the maximum weight
            max_set = {'name': i['name'], 'date': w['date'], 'weight': weight} # Update the max set
  return max_set

print(max_weight_set(data,"Lunges"))
print(max_weight_set(data, "Planks"))
print(max_weight_set(data, "Deadlifts"))

# Tests
assert max_weight_set(data,"Lunges") == {'name': 'David Green', 'date': '09-22-2016', 'weight': 40}
assert max_weight_set(data, "Planks") == None
assert max_weight_set(data, "Deadlifts") == {'name': 'Chris Brown', 'date': '12-05-2014', 'weight': 80}

#Q7
# total_weight(list of dictionaries, str, str) -> float
# Return the total weight across all days where name did excercise_name
def total_weight(lst, name, exercise_name):
 total_weight = 0 # Initialize the total weight to 0
 for person in lst:
  if person['name'] == name:
    for workout in person['workouts']:
      if workout['exercise'] == exercise_name:
        for rep_pair in workout['repPairs']:
          weight, reps = float(rep_pair[1][:-2]), rep_pair[0]
          total_weight += weight * reps # Add the product of weight and reps to total weight
 return total_weight

print(total_weight(data,"Ryan Taylor","Dumbbell Curls"))
print(total_weight(data,'Emily Davis', 'Planks'))
print(total_weight(data, 'Alice Johnson', 'Bench Press'))

# Tests
assert total_weight(data,"Ryan Taylor","Dumbbell Curls") == 360
assert total_weight(data,'Emily Davis', 'Planks') == 0
assert total_weight(data, 'Alice Johnson', 'Bench Press') == 600

#Q8
# number_of_total_reps(list of dictionaries, str) -> int
# Return the total number of reps done across all exercises done by name
def number_of_total_reps(lst, name):
  total_reps = 0 # Initialize the total number of reps to 0
  for person in lst:
   if person['name'] == name:
    for workout in person['workouts']:
      total_reps += calculate_total_reps(workout['repPairs']) # Add the total reps in each workout to the total number of reps
  return total_reps

print(number_of_total_reps(data, "Olivia Miller"))
print(number_of_total_reps(data, "Ryan Taylor"))
print(number_of_total_reps(data, 'Bob Anderson'))

# Tests
assert number_of_total_reps(data, "Olivia Miller") == 30
assert number_of_total_reps(data, "Ryan Taylor") == 96
assert number_of_total_reps(data, 'Bob Anderson') == 48

#Q9
# rep_over_weight (list of dictionaries, str, float) -> list of str
# Returns list of names,each of which lifted excercise_name for at least 1 rep at weight
def rep_over_weight(lst, exercise_name, weight):
  names = []
  for i in lst:
    for w in i['workouts']:
      if w['exercise'] == exercise_name:
        for rp in w['repPairs']:
          if int(rp[1][:-2]) >= weight and i['name'] not in names: # If the weight is greater than or equal to the given weight and the name is not already in the list of names
            names.append(i['name']) # Add the name to the list of names
  return names

print(rep_over_weight(data, "Pull ups", 0))
print(rep_over_weight(data, 'Squats', 20))
print(rep_over_weight(data, 'Deadlifts', 30))

# Tests
assert rep_over_weight(data, "Pull ups", 0) == ['Bob Anderson', 'Tim Timothy', 'Emma White']
assert rep_over_weight(data, 'Squats', 20) == ['Bob Anderson', 'Tim Timothy', 'Emma White']
assert rep_over_weight(data, 'Deadlifts', 30) == ['Alice Johnson', 'Chris Brown']

#Q10
# workout_counts(list of dictionaries) -> {‘name’: int}
# Returns a list of dictionaries,with a name and int showing the number of workouts done
def workout_counts(lst):
  counts = {}
  for i in lst:
      counts[i['name']] = len(i['workouts']) # Add an entry to the dictionary with the name as the key and the number of workouts as the value
  return counts

print(workout_counts(data))

# Test
assert workout_counts(data) == {'Bob Anderson': 2, 'Tim Timothy': 2, 'Alice Johnson': 2, 'John Smith': 2, 'Emily Davis': 2, 'Chris Brown': 2, 'Emma White': 2, 'David Green': 2, 'Olivia Miller': 2, 'Ryan Taylor': 2}

#Q11
# get_heaviest_and_lightest: (list of dictionaries, str) -> 
# {‘heaviest’:float,’lightest’:float}
# Returns a dictionary with the heaviest and lightest weights of people whose workouts 
# are in lb or kg
def get_heaviest_and_lightest(lst, unit):
  result = {}
  for person in lst:
      person_name = person['name']
      person_weight = int(person['weight'][:-2])
      if unit == 'lb':
          person_weight = to_kg(person_weight)
      weights = []
      for workout in person['workouts']:
          for repPair in workout['repPairs']:
              weights.append(float(repPair[1][:-2])) # Add the weight to the weights list
      heaviest_weight = max(weights) # Find the maximum weight in the weights list
      lightest_weight = min(weights) # Find the minimum weight in the weights list
      result[person_name] = {'heaviest': heaviest_weight, 'lightest': lightest_weight} # Add an entry to the result dictionary with the name as the key and the heaviest and lightest weights as the value
  return result

print(get_heaviest_and_lightest(data, "kg"))

# Test
assert get_heaviest_and_lightest(data, "kg") == {'Bob Anderson': {'heaviest': 40, 'lightest': 0}, 'Tim Timothy': {'heaviest': 20, 'lightest': 0}, 'Alice Johnson': {'heaviest': 60, 'lightest': 0}, 'John Smith': {'heaviest': 30, 'lightest': 0}, 'Emily Davis': {'heaviest': 10, 'lightest': 0}, 'Chris Brown': {'heaviest': 80, 'lightest': 0}, 'Emma White': {'heaviest': 50, 'lightest': 0}, 'David Green': {'heaviest': 60, 'lightest': 0}, 'Olivia Miller': {'heaviest': 30, 'lightest': 0}, 'Ryan Taylor': {'heaviest': 20, 'lightest': 0}}


