import requests
import random

# Lists to show what items are on the menu today for savoury or sweet options:
savoury_menu = ["Korean chicken wings", "Roast chicken"]
sweet_menu = ["Orange cheesecake", "Vanilla Cheesecake"]

print("Welcome! This app helps you choose a bar snack and Brew Dog beer that go well together.")
user_choice = input("What snack are you in the mood for? Please specify - savoury or sweet?: ")

""" As some of the beer descriptions are very long, I have created the wrap_text function below to avoid 
the descriptions being printed in one long line.  
The function parameters are the 'text' from the description which needs to be wrapped and the 'max width' 
for each line which below is set at 120. 
"""
def wrap_text(text, max_width):
#split() is used to split the text into a list of words
    words = text.split()
#Variables - lines stores the wrapped lines.
#Current_line is a string that represtent current line being constructed
    lines = []
    current_line = ""
#for word in words - this function loops through each word in list of words
    for word in words:
#len(current_line) calculates the length of the current line.
# len(word) calculates the length of the current word.
# + 1 accounts for the space between words.
        if len(current_line) + len(word) + 1 <= max_width:
            if current_line:
                current_line += " "
            current_line += word
# If adding the current word to the current line would exceed the maximum width, the current line
# is added to the lines list, and a new line is started with the current word.
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines
#All this to avoid words being split over different lines (so appearing to be cut off).

if user_choice == "savoury":
    print("Great, you feel like something savoury, this is today's menu: ")
    print(savoury_menu)
    input_savoury = input('Press enter to see your pairing: ')

    # A parameter has been entered within the API URL. Use the food parameter with the string 'chicken'.
    # This filters out beers that have chicken in their food_pairing information.
    chicken = 'https://api.punkapi.com/v2/beers?food=chicken'
    response = requests.get(chicken)
    chicken_data = response.json()
    # Using the import random module, a random beer will be selected from the filtered list of beers.
    random_beer = random.choice(chicken_data)
    print('This beer goes perfectly with chicken:')
    print("Name: " + random_beer["name"])
    print("Description:")
    description = random_beer["description"]
    max_width = 120
    lines = wrap_text(description, max_width)
    for line in lines:
        print(line)

elif user_choice == "sweet":
    print("You fancy something sweet? Great, it's all about cheesecakes today!: ")
    print(sweet_menu)
    input_sweet = input('Press enter to see your pairing: ')

    # Again, the parameter is within the URL (?food=cheesecake).
    cheesecake = 'https://api.punkapi.com/v2/beers?food=cheesecake'
    response = requests.get(cheesecake)
    cheesecake_data = response.json()
    random_beer = random.choice(cheesecake_data)
    # As above, import random is utilized to select a random beer from the filtered list.
    print('This beer perfectly pairs with cheesecake:')
    print("Beer Name: " + random_beer["name"])
    print("Description:")
    description = random_beer["description"]
    max_width = 120
    lines = wrap_text(description, max_width)
    for line in lines:
        print(line)
