def main():
    welcome()  # Welcome the user to the Game
    generate_number()  # Generate a random number for the user to guess
    ans = get_input()  # Get the user's number guess
    display_answer(answer=ans)  # Display the user's answer whether it is correct or not
    return True


def welcome() -> None:
    """This function welcomes the user to the game."""
    pass


def generate_number() -> int:
    """This function generates a random number and returns it.

    Returns:
        int: the randomly generated number
    """
    pass


def get_input() -> str:
    """This function gets the user's input and returns it.

    Returns:
        str: The user's number guess
    """
    pass


def display_answer(answer: str) -> None:
    """This function displays the user's answer.

    Args:
        answer (str): The user's number guess
    """
    pass


if __name__ == "__main__":
    main()
