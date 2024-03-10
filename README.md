# PokemonPixelDetector

This script is used for automatically repeating a legendary Pokemon encounter to eventually find a shiny version of it. 

## Instructions:
1. Before running the script: Position the character directly in front of the legendary Pokemon or as close as possible(The script includes an option to simulate player character movement toward a legendary Pokémon if needed), save the game, and then start the first encounter.
2. Run the script
3. The user is prompted to click on the emulator window and hover their mouse over the sprite of the legendary Pokemon. After a countdown, the script will monitor the pixel colour at that location.
4. If the detected colour matches the standard non-shiny colour, the script initiates a soft reset in the emulator.
5. The script will then automatically rencounter the Pokemon and check what the colour of it is.
6. Steps 4 and 5 will repeat until a shiny Pokemon is detected.
7. When a shiny Pokémon is detected, the script prints a message indicating the shiny encounter.  The script will then finish.

Happy hunting!
