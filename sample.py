import streamlit as st
import random

# Song templates with placeholders
templates = [
    "{character} in the {place}, feeling {emotion},\nFound a {object}, its shine in slow motion.\nWith their {animal}, so loyal and true,\nThey decided to {action}, as brave heroes do.\nIn the end, they learned, {message} so grand,\nAnd sang their tale, throughout the land.",
    
    "In the heart of {place}, under the sun's rays,\n{character} and their {animal}, lost in a daze.\nA mysterious {object}, gleaming and bright,\nCalled them to {action}, with all their might.\nThrough challenges faced, they found {message} so clear,\nAnd their song of adventure, everyone wanted to hear.",
    
    "{place} echoed with a magical song,\nWhere {character} and their {animal} did belong.\nDiscovering a {object}, ancient and rare,\nThey chose to {action}, with courage to spare.\nEvery step taught them, {message} so profound,\nTheir song of bravery, spread all around."
]

# Possible values for the placeholders
places = ["castle's courtyard", "enchanted garden", "mystical forest"]
emotions = ["overwhelmed", "intrigued", "anxious"]
objects = ["golden goblet", "enchanted mirror", "mystical pendant"]
actions = ["seek its origin", "unlock its secrets", "find its rightful owner"]
animals = ["faithful dog", "whimsical cat", "gentle deer"]
messages = [
    "true value isn't in things, but in memories made",
    "every challenge is an opportunity in disguise",
    "the heart's courage is the most potent magic of all"
]

def generate_song(character_name, place, animal):
    template = random.choice(templates)
    song = template.format(
        character=character_name,
        place=place,
        emotion=random.choice(emotions),
        object=random.choice(objects),
        action=random.choice(actions),
        animal=animal,
        message=random.choice(messages)
    )
    return song

# Streamlit interface
st.title("Adventure Song Generator for Kids")
character_name = st.text_input("Enter the character's name:", "Lily")
place = st.selectbox("Choose a place for the adventure:", places)
animal = st.selectbox("Select the type of animal the character has:", animals)

if st.button("Generate a Song"):
    song = generate_song(character_name, place, animal)
    st.write(song)
