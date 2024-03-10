# PokemonPixelDetector

This script is used for automatically repeating a legendary Pokemon encounter to eventually find a shiny version of it. 

## Instructions:
#### Before running the script...
1. Position the character directly in front of the legendary Pokemon or as close as possible(The script includes an option to simulate player character movement toward a legendary Pokémon if needed),
2. Save the game
3. Start the first encounter.

#### Running the script...  
1. Run the script
2. The user will be prompted to click on the emulator window and hover their mouse over the sprite of the legendary Pokemon. After a countdown, the script will capture those specific coordinates and begin to automatically monitor the pixel colour at that location.
3. If the detected colour matches the standard non-shiny colour, the script initiates a soft reset in the emulator.
4. The script will then automatically rencounter the Pokemon and check what the colour of it is.
5. Steps 3 and 4 will repeat until a shiny Pokemon is detected.
6. When a shiny Pokémon is detected, the script prints a message indicating the shiny encounter.  The script will then finish.

Happy hunting!
