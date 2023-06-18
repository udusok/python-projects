import random
from typing import Dict, List

from resources.questions import QUESTIONS_LIST


class Question:
    """This class represents a question in the quiz game."""

    def __init__(self, question: str, options: Dict, correct_answer: str):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def display_options(self) -> None:
        """This function displays the options for the question."""
        ...

    def check_answer(self, user_answer: str) -> bool:
        """This function checks if the user's answer is correct or not.

        Args:
            user_answer (int): The user's answer

        Returns:
            bool: True if the user's answer is correct, False otherwise
        """
        ...

    def __str__(self) -> str:
        """This function returns a string representation of the question.

        Returns:
            str: The string representation of the question
        """
        ...


class Quiz:
    def __init__(self) -> None:
        self.questions: List[Question] = []
        self.score = 0

    def generate_questions(self) -> None:
        """This function generates the questions for the quiz."""
        questions = QUESTIONS_LIST
        random.shuffle(questions)
        self.questions = [Question(*question) for question in questions]
        return None

    def start_quiz(self) -> None:
        """This function starts the quiz."""
        ...

    def display_score(self) -> None:
        print(f"Total Score: {self.score}")


def main():
    welcome()  # Welcome the user to the Game
    instructions()  # Display the instructions on how to play the game
    quiz = Quiz()  # Create a new Quiz
    quiz.start_quiz()  # Start the quiz
    quiz.display_score()  # Display the user's score
    return True


def welcome() -> None:
    """This function welcomes the user to the game."""
    ...


def instructions() -> None:
    """This function displays the instructions on how to play the game."""
    ...


if __name__ == "__main__":
    main()
