"""
                            /$$$$$$  /$$$$$$                                                                                                                 
                            |_  $$_/ /$$__  $$                                                                                                                
                            | $$  | $$  \ $$                                                                                                                
                            | $$  | $$  | $$                                                                                                                
                            | $$  | $$  | $$                                                                                                                
                            | $$  | $$  | $$                                                                                                                
                            /$$$$$$|  $$$$$$/                                                                                                                
                            |______/ \______/                                                                                                                 
                                                                      
 _____                  _         __  _____       _               _   
|_   _|                | |       / / |  _  |     | |             | |  
  | | _ __  _ __  _   _| |_     / /  | | | |_   _| |_ _ __  _   _| |_ 
  | || '_ \| '_ \| | | | __|   / /   | | | | | | | __| '_ \| | | | __|
 _| || | | | |_) | |_| | |_   / /    \ \_/ / |_| | |_| |_) | |_| | |_ 
 \___/_| |_| .__/ \__,_|\__| /_/      \___/ \__,_|\__| .__/ \__,_|\__|
           | |                                       | |              
           |_|                                       |_|              


IO examples.

Using file IO, from the docs:
    "The first argument is a string containing the filename. The second
    argument is another string containing a few characters describing 
    the way in which the file will be used. mode can be: 
        'r' when the file will only be read, 
        'w' for only writing (an existing file with the same name will be erased),
        'a' opens the file for appending; any data written to the file is automatically added to the end. 
        'r+' opens the file for both reading and writing. 
    The mode argument is optional; 'r' will be assumed if it's omitted."

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""


import json


def be_cool(name):
    """Just print, not actually doing any IO."""
    print(name + " is cool")


be_cool("Ben")


def be_cool_for_ever(name, file_path):
    """Save a message about being cool for ever."""
    mode = "w"  # from the docs
    history_book = open(file_path, mode)
    history_book.write(name + " is cool")
    history_book.close()


# look up what '..' means
be_cool_for_ever("Ben", "../ben_is_cool.txt")
be_cool_for_ever("Ben", "ben_is_cool.lol_UR_joking")


def be_cool_and_safe_for_ever(name, file_path):
    """Save a message about being cool for ever.

    This does the same thing as be_cool_for_ever, but it uses a with block.
    The with block manages the file's lifecycle so it's much harder to leave it
    open by accident.
    """
    mode = "w"  # from the docs
    with open(file_path, mode, encoding="utf-8") as history_book:
        history_book.write(f"{name} is cool and safe 🙃 ✔️ 🐼 ⨀ ½ ∞ ∴")


# look up what '..' means
be_cool_and_safe_for_ever("Ben", "../ben_is_cool.txt")
be_cool_and_safe_for_ever("Ben", "ben_is_cool.lol_UR_joking")


# See where each file was saved


def who_is_cool(file_path):
    """Read a file and print what it says."""
    mode = "r"  # from the docs
    with open(file_path, mode, encoding="utf-8") as history_book:
        response = history_book.read()

    print(f"historians have recorded that:\n\t{response}")


who_is_cool("../ben_is_cool.txt")
# who_is_cool("Set4/lazyduck.json")


# some JSON examples:


def bury_time_capsule(something_for_your_kids_to_find, file_path):
    """Save some json to a file.

    Args:
        something_for_your_kids_to_find (dict): A dictionary of facts.
        file_path (str): The path to where you want to save the json.
    """
    try:
        dumped = json.dumps(something_for_your_kids_to_find)
        mode = "w"  # from the docs
        with open(file_path, mode, encoding="utf-8") as time_capsule:
            time_capsule.write(dumped)
        return True
    except Exception as e:
        print(e)
        return False


message_for_capsule = {
    "name": "Ben",
    "Year": 2021,
    "Location": "Sydney",
    "Greeting": "Yo whatup now and give a brother room",
    "Fact": (
        "It would take 1,200,000 mosquitoes, each "
        "sucking once, to completely drain the "
        "average human of blood"
    ),
    "Alphabet Inc Class A": "1106.50USD",
    "fruit": ["apple", "apricot", "avocado", "abiu"],
}

bury_time_capsule(message_for_capsule, "under_the_patio.json")


def dig_up_capsule(file_path):
    """Read some json from a file.

    Does some defensive programming as an example of how you'd do such a thing.
    Args:
        file_path (str): The path to where you saved the json.
    """
    try:
        mode = "r"  # from the docs
        with open(file_path, mode, encoding="utf-8") as time_capsule:
            contents = json.load(time_capsule)

        keys_needed = ["Greeting", "Year", "Fact"]
        if all(key in contents for key in keys_needed):
            template = """{Greeting},\nDid you know that in {Year},\n\t"{Fact}"\n was still true!"""
            print(template.format(**contents))
            return True
        else:
            print("Your dictionary is missing some keys.", contents, keys_needed)
            return False
    except Exception as e:
        print(e)
        return False


dig_up_capsule("under_the_patio.json")
