import os
import requests

# The list of books we want to access and download
DATASOURCE = {
    "memoirs_of_grant": "https://www.gutenberg.org/ebooks/4367.txt.utf-8",
    "frankenstein": "https://www.gutenberg.org/ebooks/84.txt.utf-8",
    "sleepy_hollow": "https://www.gutenberg.org/ebooks/41.txt.utf-8",
    "origin_of_species": "https://www.gutenberg.org/ebooks/2009.txt.utf-8",
    "makers_of_many_things": "https://www.gutenberg.org/ebooks/28569.txt.utf-8",
    "common_sense": "https://www.gutenberg.org/ebooks/147.txt.utf-8",
    "economic_peace": "https://www.gutenberg.org/ebooks/15776.txt.utf-8",
    "the_great_war_3": "https://www.gutenberg.org/ebooks/29265.txt.utf-8",
    "elements_of_style": "https://www.gutenberg.org/ebooks/37134.txt.utf-8",
    "problem_of_philosophy": "https://www.gutenberg.org/ebooks/5827.txt.utf-8",
    "nights_in_london": "https://www.gutenberg.org/ebooks/23605.txt.utf-8",
}
# Get the books from the urls  
for filename, url in DATASOURCE.items():
    if not os.path.exists(f"{filename}.txt"):
        response = requests.get(url)
        with open(f"{filename}.txt", "wb") as f:
            f.write(response.content)
            
# We now have pre-cleaned text thanks to Gutenberg. Now we need to extract the book contents and store them as a list of strings in python

# Read and preprocess the text
def preprocess_gutenberg(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        
        # Need to find the start and end of the text
        start = text.find("*** START OF THE PROJECT GUTENBERG EBOOK")
        start = text.find("\n", start) + 1
        end = text.find("*** END OF THE PROJECT GUTENBERG EBOOK")
        
        # Extracting the main content
        text = text[start:end].strip()
        
        # Basic preprocessing
        # Remove multiple newlines and spaces
        text = "\n".join(line.strip() for line in text.split("\n") if line.strip())
        return text
    
def get_dataset_text():
    all_text = []
    for filename in DATASOURCE:
        text = preprocess_gutenberg(f"{filename}.txt")
        all_text.append(text)
    return all_text

text = get_dataset_text()