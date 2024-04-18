from app import app, db
from models import Question

def populate_questions():
    with app.app_context():
        # Clear existing questions
        Question.query.delete()
        
        # Easy level questions
        question1 = Question(
            question_text="What is the output of the following code?\nprint(2 + 3 * 4)",
            option_a="14",
            option_b="20",
            option_c="12",
            option_d="5",
            correct_answer="A",
            level=1
        )

        question2 = Question(
            question_text="Which of the following data types is not a built-in data type in Python?",
            option_a="List",
            option_b="Tuple",
            option_c="Integer",
            option_d="Array",
            correct_answer="D",
            level=1
        )

        question3 = Question(
            question_text="What is the output of the following code?\nprint(\"Python\"[1:4])",
            option_a="Pyt",
            option_b="yth",
            option_c="tho",
            option_d="ytho",
            correct_answer="B",
            level=1
        )

        # Medium level questions
        question4 = Question(
            question_text="What will be the output of the following code?\nfruits = [\"apple\", \"banana\", \"cherry\"]\nfruits.append(\"orange\")\nprint(fruits)",
            option_a="['apple', 'banana', 'cherry']",
            option_b="['orange', 'apple', 'banana', 'cherry']",
            option_c="['apple', 'banana', 'cherry', 'orange']",
            option_d="Error",
            correct_answer="C",
            level=2
        )

        question5 = Question(
            question_text="What will be the output of the following code?\nnumber = 10\ndef multiply_by_two(num):\n    return num * 2\nresult = multiply_by_two(number)\nprint(result)",
            option_a="10",
            option_b="20",
            option_c="None",
            option_d="Error",
            correct_answer="B",
            level=2
        )

        question6 = Question(
            question_text="What is the output of the following code?\nmy_list = [1, 2, 3, 4, 5]\nprint(my_list[1:4])",
            option_a="[2, 3, 4]",
            option_b="[1, 2, 3, 4, 5]",
            option_c="[2, 4]",
            option_d="[2, 3]",
            correct_answer="A",
            level=2
        )

        # Hard level questions
        question7 = Question(
            question_text="What is a lambda function in Python?",
            option_a="A named function",
            option_b="An anonymous function",
            option_c="A type of data structure",
            option_d="A type of loop",
            correct_answer="B",
            level=3
        )

        question8 = Question(
            question_text="Which of the following is the correct syntax for creating a generator function?",
            option_a="def my_generator():\n    yield 1\n    yield 2\n    yield 3",
            option_b="def my_generator():\n    return 1\n    return 2\n    return 3",
            option_c="generator my_generator():\n    yield 1\n    yield 2\n    yield 3",
            option_d="def my_generator():\n    raise 1\n    raise 2\n    raise 3",
            correct_answer="A",
            level=3
        )

        question9 = Question(
            question_text="What is the purpose of the `with` statement in Python?",
            option_a="To handle exceptions",
            option_b="To create a new scope",
            option_c="To manage resources (e.g., files)",
            option_d="To declare functions",
            correct_answer="C",
            level=3
        )

        question10 = Question(
            question_text="Which of the following is the correct syntax for creating a decorator function?",
            option_a="@function_name\ndef my_decorator():",
            option_b="@decorator\ndef my_function():",
            option_c="@my_decorator\n@my_function()",
            option_d="@my_decorator\ndef my_function():",
            correct_answer="D",
            level=3
        )

        # Add all questions to the database
        db.session.add_all([question1, question2, question3, question4, question5, question6, question7, question8, question9, question10])
        
        # Commit changes to the database
        db.session.commit()

if __name__ == "__main__":
    populate_questions()
