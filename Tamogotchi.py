# Check out Old Skool Tamagotchi: https://www.youtube.com/watch?v=U9at2BCLFhY and the new ones coming out: https://www.bandai.com/tamagotchi/


class Tamagotchi:
  def __init__(self, the_name):
    self.name = the_name
    self.health = 5
    self.happiness = 5
    self.potty_trained = False
    self.food = 5
    self.exercise = 5
    print("Tamagotchi created!")
    
    #1.
    # Write a __repr__ method that allows us to print a a Tamagotchi
    
    
    
        
    # 2. 
    # Define a method that determines if the Tamagotchi is hungry.
    # A Tamagotchi is full if its food level is 5.
    # A Tamagotchi is satisfied if its food level is 3 or 4
    # A Tamagotchi is hungry if its food level is less than 2 or 1
    # A Tamagotchi is starving if its foold level is zero
    
    
    
    
    # 3.
    # Define a method that "feeds" the Tamagotchi
    # Increase the food level of the Tamagotchi
    # Print a statement something like this "<Tanagotchi name> ate <food>.  New hunger level: <hunger level>" (Format it however you would like.)
    
    
    
    ## PLAYTIME ##
    #Get creative.  Add some functionaloty to your Tamagotchi
    # Some ideas: 
    # Tamagotchi's health and happiness decrease over time.  Define 
    # a "time_passed()" method that changes the variables each time you call it.
    #                                     OR
    # Create a method that increases happiness level.  For example "play()"
    #                                     OR
    # Tamadochi do poop on the floor if they are not potty trained.  Create a 
    # "potty_training()" method.
    