import streamlit as st
import random

# Song templates with placeholders
templates = [
    "{character} in the {place}, feeling {emotion},\nFound a {object}, its shine in slow motion.\nWith their {animal}, so loyal and true,\nThey decided to {action}, as brave heroes do.\nThrough valleys and mountains, they journeyed so far,\nLearning that {message}, is the best by par.\nIn the end, they sang, with voices so grand,\nOf adventures and tales, throughout the land.",
    
    "In the heart of {place}, under the sun's rays,\n{character} and their {animal}, lost in a daze.\nA mysterious {object}, gleaming and bright,\nCalled them to {action}, with all their might.\nThrough challenges faced, they found {message} so clear,\nTheir song of health and joy, everyone wanted to hear.\nWith steps so light, and hearts so free,\nThey celebrated the magic, of being healthy.",
    
    "{place} echoed with a magical song,\nWhere {character} and their {animal} did belong.\nDiscovering a {object}, ancient and rare,\nThey chose to {action}, with courage to spare.\nEvery step taught them, {message} so profound,\nTheir song of bravery and health, spread all around.\nWith tales of fruits, veggies, and water so clear,\nThey sang of the secrets, everyone should hear."
]

# Possible values for the placeholders
emotions = ["overwhelmed", "intrigued", "anxious"]
objects = ["golden goblet", "enchanted mirror", "mystical pendant"]
actions = ["seek its origin", "unlock its secrets", "find its rightful owner"]
healthy_messages = [
    "eating fruits and veggies makes us strong",
    "a balanced meal is where we belong",
    "drink water to stay refreshed and bright",
    "healthy foods give us energy and might",
    "eating well is the key to feel great",
    "choose whole foods, it's never too late",
    "a colorful plate is a joy to eat",
    "good nutrition is truly a treat",
    "healthy habits start with every bite",
    "eat well, sleep well, and you'll feel light",
    "fruits and veggies are nature's candy",
    "eating whole grains makes us feel dandy",
    "a healthy snack is a powerful tool",
    "nutrition is the best kind of fuel",
    "eat a rainbow, feel the glow",
    "with good food, our health will show",
    "healthy choices make us feel proud",
    "shout your love for veggies loud",
    "good nutrition is a lifelong quest",
    "eating well truly is the best"
]

def generate_song(character_name, place, animal, message):
    template = random.choice(templates)
    song = template.format(
        character=character_name,
        place=place,
        emotion=random.choice(emotions),
        object=random.choice(objects),
        action=random.choice(actions),
        animal=animal,
        message=message
    )
    return song

# Streamlit interface
st.title("Adventure Song Generator for Kids")
character_name = st.text_input("Enter the character's name:", "Lily")
place = st.text_input("Enter the place for the adventure:", "Mystical Meadow")
animal = st.text_input("Enter the type of animal the character has:", "Faithful Dog")
message = st.selectbox("Choose a positive message about healthy eating:", healthy_messages)

if st.button("Generate a Song"):
    song = generate_song(character_name, place, animal, message)
    st.write(song)
