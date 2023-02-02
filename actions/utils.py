dict_genres = {
        'azione': 'Action',
        'avventura': 'Adventure',
        'animazione': 'Animation',
        'commedia': 'Comedy',
        'comico': 'Comedy',
        'comica': 'Comedy',
        'crime': 'Crime',
        'giallo': 'Crime',
        'documentario': 'Documentary',
        'drammatico': 'Drama',
        'drammatica': 'Drama',
        'family': 'Family',
        'fantasy': 'Fantasy',
        'noire': 'Film-Noir',
        'storico': 'History',
        'storica': 'History',
        'horror': 'Horror',
        'musical': 'Musical',
        'mistero': 'Mistery',
        'romantico': 'Romance',
        'romantica': 'Romance',
        'fantasy': 'Sci-fi',
        'fantascienza': 'Sci-fi',
        'sportivo': 'Sport',
        'sportiva': 'Sport',
        'sport': 'Sport',
        'thriller': 'Thriller',
        'guerra': 'War',
        'western': 'Western',
    }

def trad_genere_ita_eng(genre_it):
    lower = genre_it.lower()
    print(lower)

    return dict_genres[lower] if lower in dict_genres else ''