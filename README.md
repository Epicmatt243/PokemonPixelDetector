# PokemonPixelDetector

This script is used for automatically repeating a legendary pokemon encounter to eventually find a shiny version of it. 

Instructions:
1. The user is prompted to click on the emulator window and hover their mouse over the sprite of the legendary pokemon. After a countdown, the script will monitor the pixel color at that location.
2. If the detected color matches the standard non-shiny color, the script initiates a soft reset.
3. The process repeats until a shiny Pokémon is detected, at which point the script prints a message indicating the shiny encounter.
4. Additionally, the script includes an option to simulate player character movement toward a legendary Pokémon if needed
