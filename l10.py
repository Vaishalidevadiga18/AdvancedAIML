'''import folium

# Create a map centered at Bangalore
mymap = folium.Map(location=[12.9716, 77.5946], zoom_start=12)

# Add a marker
folium.Marker(
    location=[12.9716, 77.5946],
    popup="Bangalore City",
    icon=folium.Icon(color="blue", icon="info-sign")
).add_to(mymap)

# Add another marker
folium.Marker(
    location=[13.0827, 80.2707],
    popup="Chennai City",
    icon=folium.Icon(color="green")
).add_to(mymap)

# Save the map as HTML
mymap.save("map.html")

print("✅ Map has been created! Open 'map.html' in your browser.")'''



import pyttsx3  

# Initialize the engine
engine = pyttsx3.init()

# Set voice properties
engine.setProperty("rate", 150)   # Speed of speech
engine.setProperty("volume", 0.9) # Volume (0.0 to 1.0)

# Text to speak
text = "Hello! Welcome to Python programming using libraries."

# Speak the text
engine.say(text)
engine.runAndWait()

print("✅ The text has been spoken successfully!")

