import pygal

from Ch15_Die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for i in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results (count each number):
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for i in range(2, max_result+1):
    freq = results.count(i)
    frequencies.append(freq)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of the result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
