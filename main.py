import sys
from stats import wordcount
from stats import charactercount
from stats import charcountreport

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text



def main():
    if len(sys.argv) != 2:
        print("Error, incorrect number of arguments.")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookLoc = sys.argv[1]
    text = get_book_text(bookLoc)
    print("====== BOOKBOT ======")
    print("Analyzing book found at " +str(bookLoc) + "...")
    print("---------- Word Count ----------")
    print("Found " + str(wordcount(text)) + " total words")        
    print("------- Character Count --------")
    dt = charcountreport(charactercount(text))
    for item in dt:
        char = item["char"]
        count = item["count"]
        print(f"{char}: {count}")
        

main()