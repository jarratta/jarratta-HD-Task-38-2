"""
Author: Alistair Jarratt
Student ID: AJ22110004854
Task: T40
Introduction to natural language processing
"""
# Import the spacy module then the complex "md" language model

import spacy
nlp = spacy.load("en_core_web_md")

# Function to read the movies text file and create a dictionary from the data
def import_movies():
    movie_dictionary = {}
    with open("movies.txt",'r',encoding="utf-8") as file:
        for line in file:
            key, value = line.split(':')
            movie_dictionary[key] = value.strip()
            return (movie_dictionary)

# Function to compare the model text, then find the text with the highest similarity score
def check_movie_similarity (movie_dictionary, comparison_text):

# Create tokens for the words in the text
    model_text = nlp(comparison_text)

    highest_similarity_score = 0
    most_similar_movie = ""

# For loop to compare each movie text with the model text
    for movie_name, movie_desc in movie_dictionary.items():
            similarity = nlp(movie_desc).similarity(model_text)

            if similarity > highest_similarity_score:
                highest_similarity_score = similarity
                most_similar_movie = movie_name
                return most_similar_movie, highest_similarity_score

# Function to run the import and compare the movie text with the model
def main():
    movie_dictionary = import_movies()
    text = """Will he save their world or destroy it?
When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk 
into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into 
slavery and trained as a gladiator."""
    most_similar_moview, highest_similarity_score = check_movie_similarity(movie_dictionary, text )
    print (f'The most simialr movie is {most_similar_moview}, with a score of {highest_similarity_score}')

# Run the main function
main()