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
    
    # use for loop to compare each movie and store the most similar
    for movie in movies:
        # isolate the title and description using the ':' in the source file
        title, desc = movie.split(':')
        # compare similarity of movie descriptions and store the data if it is the highes score so far
        desc_doc = nlp(desc)
        score = desc_doc.similarity(nlp(description))
        if score > max_score:
            max_score = score
            max_title = title.strip()
            max_desc = desc.strip()
    # display the result        
    print (f"The most similar movie is {max_title} with a score of {max_score}")
    print(f'''The synopsis of {max_title} is:
{max_desc}''')

# assign variables
target_desc =  "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

watch_next(target_desc)