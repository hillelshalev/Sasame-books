import streamlit as st
import random
import os

# ... [rest of the code remains unchanged]

# Function to display the background
def display_background(place, animal):
    # Assuming images are stored in 'images' directory
    place_image_path = os.path.join("images", "places", f"{place.replace(' ', '_').lower()}.jpg")
    animal_image_path = os.path.join("images", "animals", f"{animal.replace(' ', '_').lower()}.jpg")
    
    # Display the images
    st.image(place_image_path, caption=place, use_column_width=True)
    st.image(animal_image_path, caption=animal, use_column_width=True)

# Streamlit interface
st.title("Adventure Song Generator for Kids")
character_name = st.text_input("Enter the character's name:", "Lily")
place = st.text_input("Enter the place for the adventure:", "Mystical Meadow")
animal = st.text_input("Enter the type of animal the character has:", "Faithful Dog")
message = st.selectbox("Choose a positive message about healthy eating:", healthy_messages)

if st.button("Generate a Song"):
    display_background(place, animal)
    song = generate_song(character_name, place, animal, message)
    st.write(song)
