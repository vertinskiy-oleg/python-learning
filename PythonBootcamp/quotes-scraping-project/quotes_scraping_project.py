import requests as req
from bs4 import BeautifulSoup as bs
from random import choice
from csv import DictReader, DictWriter

#Start Parsing
domain = "http://quotes.toscrape.com"
quotes_data = []

def parse_quotes_data(url):
    """Parsing quotes data"""
    res = req.get(domain + url)
    data = res.text

    soup = bs(data, 'html.parser')
    quotes = soup.select(".quote")

    #parsing quotes data
    for quote in quotes:
        quote_text = quote.find(class_ = "text").get_text()   
        author = quote.find(class_ = "author").get_text()
        bio_url = quote.find(class_ = "author").find_next_sibling()["href"]

        #saving quotes data
        quotes_data.append({
            "quote" : quote_text,
            "author" : author,
            "url" : bio_url
        })

    #parsing next url and recursively calling this function while next url exist
    next_url = soup.select(".next > a")
    if len(next_url):
        parse_quotes_data(next_url[0]["href"])

def parse_author_bio(url):
    """Parsing author bio url data"""
    res = req.get(domain + url)
    data = res.text

    soup = bs(data, 'html.parser')
    born_date = soup.find(class_="author-born-date").get_text()
    born_location = soup.find(class_="author-born-location").get_text()

    return f"The author was born in {born_date} in {born_location}"
#End Parsing

#Start Writing/Reading to csv file
def write_to_csv():
    """Writing parsed data to csv file"""
    with open('quotes.csv', 'w') as file:
        headers = ["quote", "author", "url"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes_data:
            csv_writer.writerow({
                "quote": quote["quote"],
                "author": quote["author"],
                "url": quote["url"]
            })

def read_from_csv():
    """Reading parsed data from csv file"""
    global quotes_data
    with open('quotes.csv') as file:
        csv_reader = DictReader(file)
        quotes_data = list(csv_reader)
#End Writing/Reading to csv file

#Start Game logic
def game():
    """Main game function"""
    guesses = 4
    rand_quote = ''
    user_guess = ''
    
    def print_rand_quote():
        """Printing random function from quotes_data"""
        nonlocal rand_quote
        rand_quote = choice(quotes_data)
        print("Here's a quote:")
        print(rand_quote["quote"])

    def user_guess_input():
        """Asking user for input and managing guesses"""
        nonlocal user_guess, guesses
        user_guess = input(f"Who said this? Guesses remaining: {guesses}. >> ")
        guesses -= 1

    def repeat_game():
        """Asking user and repeating game"""
        repeat_game = input("Do you want to play more?(y/n)>> ")
        if repeat_game == "y":
            game()
        else:
            print("Good luck!")
    
    print_rand_quote()
    user_guess_input()

    while True:
        if user_guess != rand_quote["author"]:
            if guesses == 3:
                print("Here's a hint: ", parse_author_bio(rand_quote["url"]))
                user_guess_input()
            elif guesses == 2:
                print(f"Here's a hint: the first letter of the author's first name is: {rand_quote['author'][0]}")
                user_guess_input()
            elif guesses == 1:
                print(f"Here's a last hint: the first letter of the author's last name is: {rand_quote['author'].split()[1][0]}")
                user_guess_input()
            else:
                print("You LOSE! You have no more guesses")
                break
        elif user_guess == rand_quote["author"]:
            print("You guessed correctly! Congratulations!")
            break
            
    print(f"Correct answer is: {rand_quote['author']}")
    print(f"Your answer is: {user_guess}")

    repeat_game()
# End Game Logic

# parse_quotes_data("/")
# write_to_csv()
read_from_csv()
game()
