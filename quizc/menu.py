from quizc.console.quiz_ui_handler import *


class Menu(object):
    MENU_PROMPT = "> "

    def __init__(self):
        # self.car = ""
        self.quiz = None
        self.quiz_answers = None

    def show_main_menu(self):
        print("""
Quizc - A command quiz utility
======================================
1. Create quiz
2. Fill quiz
3. Show quiz
4. Exit
======================================
        """)

    def process(self):
        self.show_main_menu()
        option = int(input(self.MENU_PROMPT))

        create = self.quiz = QuizUIHandler.create_quiz()
        fill = self.quiz_answers = QuizUIHandler.fill_quiz(self.quiz)
        show = QuizUIHandler.show_quiz(self.quiz_answers)
        exit_menu = True
        switcher = {
            1: create,
            2: fill,
            3: show,
            4: exit_menu
        }
        return switcher.get(option, "No option quiz available, try again")
