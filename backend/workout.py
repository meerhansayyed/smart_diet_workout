def recommend_workout(level, goal):
    workouts = {
        "Beginner": ["Push-ups", "Squats", "Plank", "Jumping Jacks"],
        "Intermediate": ["Bench Press", "Deadlift", "Pull-ups", "Lunges"],
        "Advanced": ["Heavy Squats", "Snatch", "Muscle-ups", "Sprints"]
    }
    return workouts[level]
