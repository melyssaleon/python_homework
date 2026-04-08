#assigment1.py
# task 1: Hello!
def hello():
    return "Hello!"

#task 2: greet with a formatted string
def greet(name):

    return f"Hello, {name}!"

# task 3: calculate


def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b
        elif operation == "modulo":
            return a % b
        elif operation == "int_divide":
            return a // b
        elif operation == "power":
            return a ** b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
# task 4: data type conversion


def data_type_conversion(value, target_type):
    try:
        if target_type == "int":
            return int(value)
        elif target_type == "float":
            return float(value)
        elif target_type == "str":
            return str(value)
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {target_type}."

# Task 5: Grading System, Using *args


def grade(*args):
    try:
       avg = sum(args) / len(args)
       if avg >= 90:
           return "A"
       elif avg >= 80:
           return "B"
       elif avg >= 70:
           return "C"
       elif avg >= 60:
           return "D"
       else:
           return "F"
    except:
        return "Invalid data was provided."
# Task 6: Use a For Loop with a Range
#def test_repeat():
 #   assert a1.repeat("up,", 4) == "up,up,up,up,"

def repeat(string,count):
    result = ""
    for _ in range(count):
        result += string
    return result
#Task 7: Student Scores, Using **kwargs

def student_scores(mode, **kwargs):
    if mode == "mean":
        return sum(kwargs.values()) / len(kwargs)
    elif mode == "best":
        return max(kwargs, key=kwargs.get)
    
#Task 8: Titleize, with String and List Operations
#def test_titleize():
 #   assert a1.titleize("war and peace") == "War and Peace"
  #  assert a1.titleize("a separate peace") == "A Separate Peace"
#    assert a1.titleize("after on") == "After On"

def titleize(text):
    small_words = ["a", "on", "the", "of", "and", "is", "in"]
    words = text.split()
    result = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        elif word in small_words:
            result.append(word)
        else:
            result.append(word.capitalize())
            return " ".join(result)
# Task 9: Hangman, with more String Operations
#def test_hangman():
#   assert a1.hangman("difficulty","ic") == "_i__ic____"
def hangman(secret, guess):
    result = ""
    for char in secret:
        if char in guess:
            result += char
        else:
            result += "_"
    return result

# Task 10: Pig Latin, Another String Manipulation Exercise


def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    result = []

    for word in words:
        if word[0].lower() in vowels:
            result.append(word + "ay")
        else:
            i = 0
            while i < len(word) and word[i].lower() not in vowels:
               if word[i:i+2].lower() == "qu":
                    i += 2
                    break
               else:
                   i += 1
            result.append(word[i:] + word[:i] + "ay")
    return " ".join(result)