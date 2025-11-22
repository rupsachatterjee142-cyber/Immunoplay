# visualizer.py

import matplotlib.pyplot as plt

def plot_habit_impact(habit_data):
    """
    Plots a bar chart of user habits and their contribution to immunity score.
    """
    labels = list(habit_data.keys())
    values = []

    # Assign weights to each habit (same as gamify.py)
    for habit in labels:
        if habit == 'sleep_hours':
            values.append(habit_data[habit] * 2.5)
        elif habit == 'exercise_minutes':
            values.append(habit_data[habit] * 0.7)
        elif habit == 'junk_food_intake':
            values.append(10 - habit_data[habit] * 2)
        elif habit == 'hydration_liters':
            values.append(habit_data[habit] * 5)
        elif habit == 'stress_level':
            values.append(10 - habit_data[habit] * 2)

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color='skyblue')
    plt.title("Impact of Habits on Immunity Score")
    plt.ylabel("Score Contribution")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("assets/habit_impact.png")
    plt.close()
