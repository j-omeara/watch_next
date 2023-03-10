# import spacy, assign nlp
import spacy
nlp = spacy.load('en_core_web_md')

# define function
def watch_next(description):

    # add movies from source file to list
    with open('movies.txt', 'r') as f:
        movies = [line.strip() for line in f.readlines()]

    # create variables
    max_score = 0
    max_title = ""
    max_desc = ""

# assign variables
target_desc =  "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
