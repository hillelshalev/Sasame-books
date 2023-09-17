import streamlit as st
import random

# Rhyming story templates with placeholders
templates = [
    "In the heart of {place}, where wonders never cease,\nLived {name} and their {animal}, in perfect peace.\nOne day, a {object} appeared, mysterious and grand,\nPrompting {name} and their parent to explore the land.\n\nThey faced many challenges, some big, some small,\nBut with courage and wit, they overcame them all.\nWith every twist and turn, their bond did grow,\nLearning lessons about {message}, more than they'd ever know.\n\nReturning home, with stories to tell,\n{name}, their {animal}, and parent, in their hearts, the lessons did dwell.",
    
    "{name}, in {place}, started their day with glee,\nWith their {animal} and parent, as happy as can be.\nBut a {object} they found, set them on a quest,\nTo discover its secrets, they'd give their best.\n\nJourneying far, facing challenges untold,\nThe trio's determination was a sight to behold.\nThrough every adventure, their spirits never did sway,\nFor they learned about {message}, in a profound way.\n\nAs the stars shone bright, signaling the journey's end,\n{name} realized the value of family and friend.",
    
    "In the serene surroundings of {place}, under the blue sky,\n{name} and their {animal} heard a mysterious cry.\nWith their parent by their side, they decided to explore,\nFinding a {object}, they'd never seen before.\n\nThe journey was long, with many a twist,\nBut with love and perseverance, nothing was amiss.\nTogether, they discovered the magic so rare,\nAnd the importance of {message}, beyond compare.\n\nReturning to {place}, their hearts full of glee,\n{name}, their {animal}, and parent, forever a story to be."
]

# Possible values for the placeholders
places = ["Mystical Meadow", "Enchanted Forest", "Whimsical Waterfall", "Serene Seashore", "Golden Grove"]
objects = ["ancient map", "mysterious key", "enchanted stone", "old scroll", "magical pendant"]
animals = ["playful cat", "loyal dog", "chirpy parrot", "gentle rabbit", "smart hamster"]
messages = {
    "healthy eating": "eating healthy and staying fit",
    "friendship": "the bond of true friendship",
    "exercise": "the joys of staying active",
    "courage to dare": "having the courage to dare and dream",
    "respecting your elderly": "the wisdom of respecting the elderly"
}
heroes = ["hero", "heroine"]

def generate_story(name, hero, place, animal, message_key):
    while True:  # Keep generating until the story is within the desired word count
        template = random.choice(templates)
        story = template.format(
            name=name,
            hero=hero,
            place=place,
            object=random.choice(objects),
            animal=animal,
            message=messages[message_key]
        )
        word_count = len(story.split())
        if 450 <= word_count <= 550:
            break
    return story

# Streamlit interface
st.title("Adventure Story Generator for Kids")
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
