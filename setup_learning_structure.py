import os

# Define your main learning folder (current directory)
base_folder = os.getcwd()

# Folder structure
folders = {
    "01_basics": [
        "hello_world.py",
        "variables.py",
        "input_output.py",
        "calculator.py"
    ],
    "02_conditions": [
        "if_statements.py",
        "grade_calculator.py",
        "even_odd_checker.py"
    ],
    "03_loops": [
        "for_loops.py",
        "while_loops.py",
        "multiplication_table.py"
    ],
    "04_data_structures": [
        "lists.py",
        "dictionaries.py",
        "student_scores.py"
    ],
    "05_functions": [
        "functions_basics.py",
        "word_counter.py"
    ],
    "06_files_errors_modules": [
        "file_handling.py",
        "try_except.py",
        "random_game.py"
    ],
    "07_oop": [
        "student_class.py",
        "bank_account.py"
    ],
    "08_testing": [
        "calculator.py",
        "test_calculator.py"
    ],
    "09_projects": [
        "password_validator.py",
        "cash_register.py",
        "roman_numeral_converter.py",
        "quiz_game.py"
    ]
}

# Create folders and files
for folder, files in folders.items():
    folder_path = os.path.join(base_folder, folder)
    os.makedirs(folder_path, exist_ok=True)
    for file in files:
        file_path = os.path.join(folder_path, file)
        # Only create the file if it doesn't already exist
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("# " + file.replace(".py", "").replace("_", " ").title() + "\n\n")
            print(f"Created: {file_path}")

# Create a README file
readme_path = os.path.join(base_folder, "README.md")
if not os.path.exists(readme_path):
    with open(readme_path, "w") as f:
        f.write("# Python Solo Learning\n\nWelcome to your Python learning journey!\n")
    print(f"Created: {readme_path}")

print("\n✅ Folder structure created successfully!")
