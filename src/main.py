from colorama import init, Fore, Style

# List of all the applications/ games
APP_LIST = [1, 2, 3, 4, 5, 6]


def main():
    welcome()  # Welcome the user to the Python Projects Repository
    display_projects()  # Display the List of Projects the user can activate
    app = handle_input()  # Get the user's input and start the appropriate project
    start_app(app)  # Start the project


def welcome() -> None:
    print(Fore.CYAN + "Welcome to the Python Projects Repository!" + Fore.RESET)


def display_projects():
    # Initialize colorama
    init()

    # Define the projects dictionary
    projects = {
        "Games": [
            "Number Guessing Game",  # number 1
            "Tic-Tac-Toe",  # number 2
            "Rock Paper Scissors",  # number 3
            "Quiz Game",  # number 4
        ],
        "Applications": [
            "Weather App",  # number 5
            "File Organizer",  # number 6
            "Currency Converter",  # number 7
            "URL Shortener",  # number 8
        ],
    }

    # Display the projects with appropriate coloring and headers
    print(Fore.CYAN + "Projects:")
    print(Fore.YELLOW + "Games:")
    for i, game in enumerate(projects["Games"], start=1):
        print(f"{Fore.GREEN}{i}. {game}")
    print(Fore.YELLOW + "Applications:")
    for i, app in enumerate(projects["Applications"], start=5):
        print(f"{Fore.BLUE}{i}. {app}")
    print(Fore.RED + "9. Exit")

    # Reset color
    print(Style.RESET_ALL)


def handle_input() -> int:
    while True:
        try:
            answer = int(
                input(Fore.GREEN + "Which Project Number do you want to start? ")
            )
            if answer in APP_LIST or answer == 5:
                return answer
            else:
                print(
                    Fore.RED + "Invalid project number. Please try again." + Fore.RESET
                )
        except ValueError:
            print(
                Fore.RED
                + "Invalid input. Please enter a valid project number."
                + Fore.RESET
            )


def start_app(app: int) -> bool:
    apps = {
        1: ("games.number_guessing_game", "main"),
        2: ("games.rock_paper_scissors", "main"),
        3: ("games.tik_tac_toe", "main"),
        4: ("games.quiz_game", "main"),
        5: ("applications.weather_app", "main"),
        6: ("applications.file_organizer", "main"),
        7: ("applications.currency_converter", "main"),
        8: ("applications.url_shortener", "main"),
    }

    if app in apps:
        module_name, function_name = apps[app]
        module = __import__(module_name, fromlist=[function_name])
        getattr(module, function_name)()  # Call the function
        return True

    return False


if __name__ == "__main__":
    main()
