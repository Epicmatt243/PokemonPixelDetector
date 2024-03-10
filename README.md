# PokemonPixelDetector

This script is used for automatically repeating a legendary Pokemon encounter to eventually find a shiny version of it. 

## Instructions:
Before running the script: Position the character directly in front of the legendary Pokemon or as close as possible(The script includes an option to simulate player character movement toward a legendary Pokémon if needed), save the game, and then start the first encounter.

(Running the script)
1. The user is prompted to click on the emulator window and hover their mouse over the sprite of the legendary Pokemon. After a countdown, the script will monitor the pixel colour at that location.
2. If the detected colour matches the standard non-shiny colour, the script initiates a soft reset in the emulator.
3. The process repeats until a shiny Pokémon is detected, at which point the script prints a message indicating the shiny encounter.
