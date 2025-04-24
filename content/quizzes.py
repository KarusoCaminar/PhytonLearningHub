# Python quizzes content
quizzes = [
    {
        'title': 'Python Fundamentals Quiz',
        'description': 'Test your knowledge of Python basics and syntax.',
        'questions': [
            {
                'type': 'mcq',
                'question': 'What is the correct file extension for Python files?',
                'options': ['.py', '.pt', '.pyth', '.p'],
                'correct_answer': '.py',
                'explanation': 'Python files use the .py extension.'
            },
            {
                'type': 'mcq',
                'question': 'Which of the following is NOT a valid variable name in Python?',
                'options': ['my_var', '_var', '2var', 'var_name'],
                'correct_answer': '2var',
                'explanation': 'Variable names cannot start with a number in Python.'
            },
            {
                'type': 'true_false',
                'question': 'Python is a case-sensitive language.',
                'correct_answer': 'True',
                'explanation': 'Python is case-sensitive, meaning "Variable" and "variable" are considered different identifiers.'
            },
            {
                'type': 'mcq',
                'question': 'Which of these data types is mutable in Python?',
                'options': ['String', 'Tuple', 'List', 'Number'],
                'correct_answer': 'List',
                'explanation': 'Lists are mutable, meaning they can be changed after creation. Strings, tuples, and numbers are immutable.'
            },
            {
                'type': 'mcq',
                'question': 'What will be the output of: print(2 ** 3)?',
                'options': ['6', '8', '5', 'Error'],
                'correct_answer': '8',
                'explanation': 'The ** operator performs exponentiation. 2 ** 3 means 2 raised to the power of 3, which is 8.'
            }
        ]
    },
    {
        'title': 'Data Types and Operations',
        'description': 'Test your knowledge of Python data types, operations, and manipulations.',
        'questions': [
            {
                'type': 'mcq',
                'question': 'What is the result of: 3 + 2 * 2?',
                'options': ['10', '7', '5', 'Error'],
                'correct_answer': '7',
                'explanation': 'Python follows order of operations. Multiplication happens before addition, so 2 * 2 = 4, then 3 + 4 = 7.'
            },
            {
                'type': 'mcq',
                'question': 'Which function converts a string to an integer in Python?',
                'options': ['int()', 'string()', 'convert()', 'integer()'],
                'correct_answer': 'int()',
                'explanation': 'The int() function is used to convert a value to an integer.'
            },
            {
                'type': 'mcq',
                'question': 'What will "Hello"[1] return?',
                'options': ['H', 'e', 'He', 'l'],
                'correct_answer': 'e',
                'explanation': 'String indexing starts at 0, so "Hello"[1] returns the second character, which is "e".'
            },
            {
                'type': 'mcq',
                'question': 'What is the data type of the result: 10 / 2?',
                'options': ['int', 'float', 'double', 'number'],
                'correct_answer': 'float',
                'explanation': 'In Python 3, the / operator always returns a float, even if the result is a whole number. So 10 / 2 returns 5.0, which is a float.'
            },
            {
                'type': 'true_false',
                'question': 'The len() function can be used on both strings and lists.',
                'correct_answer': 'True',
                'explanation': 'The len() function returns the number of items in a sequence, which works for strings, lists, tuples, and other sequence types.'
            }
        ]
    },
    {
        'title': 'Control Flow and Functions',
        'description': 'Test your knowledge of Python control structures and functions.',
        'questions': [
            {
                'type': 'mcq',
                'question': 'Which statement is used to exit a loop prematurely in Python?',
                'options': ['exit', 'break', 'continue', 'return'],
                'correct_answer': 'break',
                'explanation': 'The break statement is used to exit a loop before the normal completion.'
            },
            {
                'type': 'mcq',
                'question': 'What happens when a return statement is executed in a function?',
                'options': [
                    'The function pauses and can be resumed later',
                    'The function ends and returns the specified value',
                    'The program terminates',
                    'A syntax error occurs if no value is specified'
                ],
                'correct_answer': 'The function ends and returns the specified value',
                'explanation': 'When a return statement is executed, the function terminates and passes the specified value back to the caller.'
            },
            {
                'type': 'true_false',
                'question': 'In Python, indentation is used to define a block of code.',
                'correct_answer': 'True',
                'explanation': 'Python uses indentation (whitespace at the beginning of a line) to define blocks of code, unlike many other programming languages that use braces {}.'
            },
            {
                'type': 'mcq',
                'question': 'Which of the following is NOT a valid loop in Python?',
                'options': ['for loop', 'while loop', 'do-while loop', 'nested loop'],
                'correct_answer': 'do-while loop',
                'explanation': 'Python does not have a built-in do-while loop. It only has for and while loops, though you can simulate a do-while loop using a while loop with a break statement.'
            },
            {
                'type': 'short_answer',
                'question': 'What keyword is used to define a function in Python?',
                'correct_answer': 'def',
                'explanation': 'The def keyword is used to define a function in Python. For example: def my_function():'
            }
        ]
    },
    {
        'title': 'Data Structures: Lists and Dictionaries',
        'description': 'Test your knowledge of Python collections like lists and dictionaries.',
        'questions': [
            {
                'type': 'mcq',
                'question': 'How do you add an element to the end of a list?',
                'options': ['list.add(element)', 'list.append(element)', 'list.insert(element)', 'list.end(element)'],
                'correct_answer': 'list.append(element)',
                'explanation': 'The append() method adds an element to the end of a list.'
            },
            {
                'type': 'mcq',
                'question': 'What will be the result of: [1, 2, 3] + [4, 5]?',
                'options': ['[1, 2, 3, 4, 5]', '[5, 7, 8]', 'Error', '[1, 2, 3, [4, 5]]'],
                'correct_answer': '[1, 2, 3, 4, 5]',
                'explanation': 'The + operator concatenates lists, creating a new list with all elements from both original lists.'
            },
            {
                'type': 'mcq',
                'question': 'How do you access the value for key "name" in a dictionary?',
                'options': ['dict[name]', 'dict.name', 'dict["name"]', 'dict.get("name")'],
                'correct_answer': 'dict["name"]',
                'explanation': 'You can access dictionary values using square bracket notation with the key. dict.get("name") would also work but has different behavior if the key doesn\'t exist.'
            },
            {
                'type': 'mcq',
                'question': 'Which Python data structure is an ordered collection of elements?',
                'options': ['Dictionary', 'Set', 'List', 'None of the above'],
                'correct_answer': 'List',
                'explanation': 'Lists are ordered collections, meaning the order of elements is preserved. Dictionaries and sets don\'t guarantee order (though in Python 3.7+, dictionaries do preserve insertion order).'
            },
            {
                'type': 'true_false',
                'question': 'Dictionaries can have lists as keys.',
                'correct_answer': 'False',
                'explanation': 'Dictionary keys must be of hashable types. Lists are mutable and therefore not hashable, so they cannot be used as dictionary keys. However, tuples (which are immutable) can be used as keys.'
            }
        ]
    },
    {
        'title': 'Error Handling and File Operations',
        'description': 'Test your knowledge of Python exceptions, error handling, and file operations.',
        'questions': [
            {
                'type': 'mcq',
                'question': 'Which statement is used to handle exceptions in Python?',
                'options': ['catch', 'try', 'except', 'handle'],
                'correct_answer': 'try',
                'explanation': 'The try statement is used to catch and handle exceptions. It is typically paired with except blocks to catch specific exceptions.'
            },
            {
                'type': 'true_false',
                'question': 'The finally block in a try-except statement will always execute, whether an exception is raised or not.',
                'correct_answer': 'True',
                'explanation': 'The finally block always executes when the try block exits, regardless of whether an exception was raised or caught.'
            },
            {
                'type': 'mcq',
                'question': 'Which mode is used to open a file for writing, creating a new file if it doesn\'t exist and overwriting if it does?',
                'options': ['r', 'w', 'a', 'x'],
                'correct_answer': 'w',
                'explanation': 'The "w" mode opens a file for writing. It creates a new file if it doesn\'t exist or truncates (overwrites) the file if it does.'
            },
            {
                'type': 'mcq',
                'question': 'What is the best practice for opening files in Python?',
                'options': [
                    'Use open() and remember to call close() later',
                    'Use with open() as file: which automatically handles closing',
                    'Use file = File(filename) constructor',
                    'Use import file'
                ],
                'correct_answer': 'Use with open() as file: which automatically handles closing',
                'explanation': 'The with statement creates a context manager that automatically closes the file when the block is exited, even if an exception is raised.'
            },
            {
                'type': 'mcq',
                'question': 'Which exception is raised when you try to access an index that doesn\'t exist in a list?',
                'options': ['ValueError', 'KeyError', 'IndexError', 'TypeError'],
                'correct_answer': 'IndexError',
                'explanation': 'IndexError is raised when you try to access an index that is out of range for a sequence like a list or string.'
            }
        ]
    }
]
