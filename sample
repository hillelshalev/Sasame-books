import streamlit as st
import random

# Story templates with placeholders
templates = [
    "{character} was feeling {emotion} in the {setting}. But after {action}, {character} felt so much better and learned that {message}.",
    "In the magical land of {setting}, {character} discovered a {object}. By {action}, they realized that {message}.",
    "{character} always wanted to {action}. One day, in the {setting}, they finally did! And they understood that {message}."
]

# Possible values for the placeholders
characters = ["Lily the Rabbit", "Tommy the Turtle", "Finn the Fox"]
emotions = ["sad", "lonely", "worried"]
settings = ["meadow", "forest", "beach"]
actions = ["meeting a new friend", "helping someone in need", "finding a hidden treasure"]
objects = ["shiny stone", "old book", "mysterious key"]
messages = [
    "it's always brighter after the storm",
    "kindness always comes back",
    "friendship is the real treasure"
]

def generate_story():
    template = random.choice(templates)
    story = template.format(
        character=random.choice(characters),
        emotion=random.choice(emotions),
        setting=random.choice(settings),
        action=random.choice(actions),
        object=random.choice(objects),
        message=random.choice(messages)
    )
    return story

# Streamlit interface
st.title("Kids Story Generator")
if st.button("Generate a Story"):
    story = generate_story()
    st.write(story)
