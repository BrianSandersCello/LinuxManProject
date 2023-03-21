#!/usr/bin/env python3
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def download_nltk_data_if_needed():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')

download_nltk_data_if_needed()



def read_commands(file_name):
    with open(file_name, 'r') as f:
        contents = f.read()

    entries = contents.split('\n\n')
    commands = []

    for entry in entries:
        lines = entry.split('\n')
        commands.append((lines[:2], entry))

    return commands


def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [word.lower() for word in tokens if word.isalnum()]
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    return ' '.join(tokens)

def read_command_words(file_name):
    with open(file_name, 'r') as f:
        command_words = f.read().splitlines()

    return command_words

def search_commands(query, commands, num_results=3):
    query_preprocessed = preprocess_text(query)
    command_lines = [' '.join(command[0]) for command in commands]
    command_entries = [command[1] for command in commands]
    command_lines_preprocessed = [preprocess_text(line) for line in command_lines]
 # make sure to allow for useful special characters   
def custom_tokenizer(text):
    pattern = r'(?u)\b\w\w+\b|[$>|<#]'
    tokens = re.findall(pattern, text)
    return tokens    
 # check if the query matches a command name exactly
    exact_match_indices = [i for i, line in enumerate(command_lines) if query.lower() == line.lower()]

    if exact_match_indices:
        exact_match_entries = [command_entries[i] for i in exact_match_indices]
        return exact_match_entries[:num_results]

    # read command words from file
    command_words = read_command_words('commands2.txt')

    # check if the query matches a command word
    query_words = query_preprocessed.split()
    matching_words = set(query_words) & set(command_words)
    if matching_words:
        indices = [i for i, line in enumerate(command_lines_preprocessed) if any(word in line.split() for word in matching_words)]
        entries = [command_entries[i] for i in indices]
        return entries[:num_results]
    # perform the original search if there was no exact match or command word match
    vectorizer = TfidfVectorizer(tokenizer=custom_tokenizer, stop_words=stopwords.words('english'))
    command_matrix = vectorizer.fit_transform(command_lines_preprocessed)
    query_vector = vectorizer.transform([query_preprocessed])

    similarities = cosine_similarity(query_vector, command_matrix)
    sorted_indices = similarities.argsort()[0][::-1]

    return [command_entries[i] for i in sorted_indices[:num_results]]


def main():
    print("Hello, I am your Linux searchbot. Please enter a command to search for it by name, or ask a question, such as 'How do I make a file?' Or, 'How do I check file ownership?'")
    commands = read_commands('commands.txt')

    query = input('Enter your search query: ').strip()

    results = search_commands(query, commands)

    if not results:
        print('No matching commands found.')
    else:
        print('Top 3 most relevant commands:')
        for i, result in enumerate(results, start=1):
            print(f'{i}. {result}\n')


if __name__ == '__main__':
    main()

