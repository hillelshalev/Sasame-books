import streamlit as st
import random

# Adjusted rhyming story templates with placeholders
templates = [
    "{name} was in the {place}, feeling quite {emotion}.\nWith their {animal}, adventure was set in motion.\nThey discovered a {object}, gleaming so bright.\nChose to {action}, with courage and might.\nJourneying far, facing challenges rare.\nThey learned about {message}, with wisdom to share.",
    
    "In the heart of {place}, as the sun began to glow,\n{name} and their {animal}, prepared for the show.\nA {object} they found, with mysteries to pry.\nThey decided to {action}, aiming for the sky.\nThrough twists and turns, their spirit did flare.\nWith the lesson of {message}, for all to be aware.",
    
    "{place} whispered tales, of treasures profound.\nWhere {name} and their {animal} were destiny-bound.\nAn {object} they spotted, ancient and still.\nWith determination, they chose to {action} with will.\nWith every challenge, their bond did prepare.\nThe essence of {message}, became their core prayer."
]

# Possible values for the placeholders
places = ["Mystical Meadow", "Enchanted Forest", "Whimsical Waterfall", "Serene Seashore", "Golden Grove"]
emotions = ["curious", "excited", "determined"]
objects = ["ancient map", "mysterious key", "enchanted stone", "old scroll", "magical pendant"]
actions = ["follow its path", "unlock its mystery", "decipher its runes"]
animals = ["playful cat", "loyal dog", "chirpy parrot", "gentle rabbit", "smart hamster"]
messages = {
    "healthy eating": "the joy of eating greens and fruits",
    "friendship": "the bond of true friendship",
    "exercise": "keeping active and fit",
    "courage to dare": "the courage to explore and dare",
    "respecting your elderly": "respecting and valuing the elderly"
}
heroes = ["hero", "heroine"]

def generate_story(name, hero, place, animal, message_key):
    template = random.choice(templates)
    story = template.format(
        name=name,
        hero=hero,
        place=place,
        emotion=random.choice(emotions),
        object=random.choice(objects),
        action=random.choice(actions),
        animal=animal,
        message=messages[message_key]
    )
    return story

# Streamlit interface
st.title("Rhyming Adventure Story Generator for Kids")
name = st.text_input("Enter the name of the protagonist:", "Alex")
hero = st.selectbox("Choose the protagonist's role:", heroes)
place = st.selectbox("Select a place for the adventure:", places)
animal = st.selectbox("Choose the type of animal the protagonist has:", animals)
message_key = st.selectbox("Choose the core message of the story:", list(messages.keys()))

if st.button("Generate a Story"):
    story = generate_story(name, hero, place, animal, message_key)
    # Bold the name of the hero
    story = story.replace(name, f"**{name}**")
    st.markdown(story)

