import random

# 1. Create subjects
subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
]

# 2. Create actions
actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

# 3. Create places or things
places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

# 4. Start headline generator
while True:

    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place}"

    print("\n" + headline)

    user_input = input(
        "\nDo you want another headline? (yes/no): "
    ).strip().lower()

    if user_input in ["no", "n"]:
        break

# 5. Goodbye message (outside the loop)
print("\nThanks for using the Fake News Headline Generator. Have a fun!")