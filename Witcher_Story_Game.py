import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


# I chose a "choose your own story" game for my project. It is based on The Witcher with the player as Geralt.
# The game goes through scenes and actions as he would.
# I love the Witcher TV Show, but I am not good at most video games on the computer or XBox.
# I wanted to created something for beginners.
def start_story() -> str:
    """
    Starts the game with a welcome message and introduces the player to their character, Geralt.
    """
    logging.info(
        "Welcome to The Witcher: Into the Shadows adventure game! You are Geralt of Rivia, "
        "a renowned monster hunter known as a Witcher, killing monsters for coin. "
        "You find yourself at a crossroads. Which path will you choose?"
    )
    return "crossroads"


# This function starts the game with a welcome message and introduces the player to their character, Geralt.
# It prints out the introductory messages and prompts the player to choose a path.


def crossroads() -> str:
    """
    Presents the player with a choice between two paths: forest or city.
    """
    logging.info(
        "To your left lies a dark forest, and to your right is a bustling city. Which path will you take?"
    )
    choice = input("Type 'forest' or 'city': ").lower()
    if choice == "forest":
        return "dark_forest"
    if choice == "city":
        return "novigrad"
    logging.warning("Invalid choice! Try again.")
    return "crossroads"


# If the player chooses to enter the dark forest, this function presents the player with decisions to interact with monsters.
# Depending on the player's choice, they may encounter enemies or decide to turn back.
# Returns the next scene based on the player's actions.


class Sword:
    __slots__ = ("name", "attack_power")

    def __init__(self, name: str, attack_power: int) -> None:
        self.name = name
        self.attack_power = attack_power


class Geralt:
    __slots__ = ("name", "sword")

    def __init__(self, name: str, sword: Sword) -> None:
        self.name = name
        self.sword = sword

    def attack(self, target: str) -> int:
        logging.info(f"{self.name} attacks {target}!")
        return self.sword.attack_power


# Instantiate Sword for Geralt
geralt = Geralt("Geralt", Sword("Silver Sword", 20))


def dark_forest() -> str:
    """
    Presents the player with decisions to interact with monsters in the dark forest.
    """
    logging.info(
        "You have entered the dark forest. As you venture deeper, \
                you hear growls and rustling in the bushes. Do you want to investigate?"
    )
    choice = input("Type 'yes' or 'no': ").lower()
    if choice == "yes":
        logging.info(
            "You encounter a group of bloodthirsty nekkers! Will you fight or flee?"
        )
        action = input("Type 'fight' or 'flee': ").lower()
        if action == "fight":
            damage_dealt = geralt.attack("Nekkers")
            logging.info(f"{geralt.name} dealt {damage_dealt} damage to the nekkers!")
            logging.info(
                "You successfully defeat the nekkers and continue your journey."
            )
            return "crossroads"
        elif action == "flee":
            logging.info(
                "You flee and hide. The nekkers take you by surprise and eat you."
            )
            return "quit"

    logging.info("You decide not to investigate and turn back.")
    return "crossroads"


# If the player chooses to go to Novigrad (the city), this function presents the player with options to explore Novigrad.
# Each option leads to a different outcome.
# Returns the next scene based on the player's choice.


def novigrad() -> str:
    """
    Presents the player with options to explore Novigrad.
    """
    logging.info(
        "You have arrived at the city of Novigrad. It is bustling with merchants, \
                guards, and townsfolk. What will you do in Novigrad?"
    )
    logging.info("1. Visit the tavern.")
    logging.info("2. Seek contracts at the notice board.")
    logging.info("3. Explore the city streets.")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        logging.info("You enter the tavern and share stories with fellow travelers.")
        return "quit"
    elif choice == "2":
        logging.info(
            "You visit the notice board and accept a contract to hunt down a griffin."
        )
        return "crossroads"
    elif choice == "3":
        logging.info("You explore the city streets and stumble upon a hidden treasure!")
        return "quit"

    logging.warning("Invalid choice! Try again.")
    return "novigrad"


scenes = {
    "start": start_story,
    "crossroads": crossroads,
    "dark_forest": dark_forest,
    "novigrad": novigrad,
}


# Controls the flow of the game by continuously looping through scenes until the player decides to quit.
# It starts at the "start" scene and continues until the player reaches the end of the game or decides to quit.
# Calls the respective scene functions based on the current scene and updates the current scene accordingly.


def play_game() -> None:
    """
    Controls the flow of the game.
    """
    current_scene = "start"
    while True:
        scene_function = scenes[current_scene]
        next_scene = scene_function()
        if next_scene == "quit":
            logging.info("Thanks for playing! Do you want to play again?")
            choice = input("Type 'yes' to restart or anything else to quit: ").lower()
            if choice == "yes":
                logging.info("You return to the crossroads")
                next_scene = "crossroads"
            else:
                logging.info("THE END")
                break
        current_scene = next_scene


if __name__ == "__main__":
    # Start the game
    play_game()
