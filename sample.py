import streamlit as st
import random

# Rhyming story templates with placeholders
templates = [
    "{hero} was in the {place}, feeling quite {emotion},\nWith their {animal}, they set things in motion.\nThey found a {object}, shining so bright,\nDecided to {action}, with all their might.\nThrough challenges and adventures, they did fare,\nAnd in the end, they learned about {message} with care.",
    
    "In the {place}, under the sun's glow,\n{hero} and their {animal}, put up a great show.\nA mysterious {object}, caught their keen eye,\nThey chose to {action}, reaching for the sky.\nWith every step, they grew more aware,\nThat the true treasure was the lesson on {message} they'd share.",
    
    "{place} held a secret, waiting to be found,\nWhere {hero} and their {animal} played around.\nDiscovering a {object}, they felt a rare thrill,\nAnd decided to {action}, testing their skill.\nTheir journey taught them, with every square,\nThe importance of {message}, beyond compare."
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

def generate_story(hero, place, animal, message_key):
    template = random.choice(templates)
    story = template.format(
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
hero = st.selectbox("Choose the protagonist:", heroes)
place = st.selectbox("Select a place for the adventure:", places)
animal = st.selectbox("Choose the type of animal the protagonist has:", animals)
message_key = st.selectbox("Choose the core message of the story:", list(messages.keys()))

if st.button("Generate a Story"):
    story = generate_story(hero, place, animal, message_key)
    st.write(story)
