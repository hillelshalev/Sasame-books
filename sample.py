import streamlit as st
import random

# Story templates with placeholders
templates = [
    "{character} was in a grand castle. They felt {emotion}. As they wandered the halls, they stumbled upon a {object}. Curious, {character} decided to {action}. Through this adventure, they met many friends and faced challenges. In the end, {character} realized that {message}. It was a day they'd never forget in the castle.",
    "In the heart of a majestic castle, {character} discovered a {object}. This wasn't any ordinary item; it had powers. Unsure of what to do, {character} decided to {action}. Along the way, they learned many lessons. The most important of all was that {message}. The castle always had its mysteries.",
    "The castle's towers touched the sky. Inside, {character} found a {object}. This discovery led them to {action}. The journey was filled with surprises. But with courage and heart, {character} understood that {message}. The castle's walls echoed with their laughter."
]

# Possible values for the placeholders
emotions = ["overwhelmed", "intrigued", "anxious"]
objects = ["golden goblet", "enchanted mirror", "mystical pendant"]
actions = ["seek its origin", "unlock its secrets", "find its rightful owner"]
messages = [
    "true value isn't in things, but in memories made",
    "every challenge is an opportunity in disguise",
    "the heart's courage is the most potent magic of all"
]

def generate_story(character_name):
    template = random.choice(templates)
    story = template.format(
        character=character_name,
        emotion=random.choice(emotions),
        object=random.choice(objects),
        action=random.choice(actions),
        message=random.choice(messages)
    )
    return story

# Streamlit interface
st.title("Castle Story Generator for Kids")
character_name = st.text_input("Enter the character's name:", "Lily")

if st.button("Generate a Story"):
    story = generate_story(character_name)
    st.write(story)
