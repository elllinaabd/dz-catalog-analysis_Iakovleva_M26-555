import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", 
                                                    "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]
def average_rating(movies):
    total_rating = sum(movie["rating"] for movie in movies)
    return round(total_rating / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]

    oldest_age = max(ages)
    newest_age = min(ages)
    average_age = math.ceil(sum(ages) / len(ages))

    return (oldest_age, newest_age, average_age)

def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60

    return f"{hours}ч {remaining_minutes}м"

def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"

def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"    

def count_long_movies(movies, threshold=120):
    count = 0

    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1

    return count

def normalize_title(title):
    words = title.split()
    normalized_words = []

    for word in words:
        normalized_word = word[0].upper() + word[1:]
        normalized_words.append(normalized_word)

    return " ".join(normalized_words)

def make_slug(title):
    return title.lower().replace(" ", "-") 

def format_report_line(movie):
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return (
        f'"{title}" ({movie["year"]}) — '
        f'{movie["rating"]}/10, {duration}, жанры: {genres}'
    )

def titles_sorted_by_rating(movies):
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True,
    )

    return [movie["title"] for movie in sorted_movies]

def top_n_by_rating(movies, n=3):
    sorted_movies = titles_sorted_by_rating(movies)
    top_movies = []

    for title in sorted_movies[:n]:
        for movie in movies:
            if movie["title"] == title:
                top_movies.append((title, movie["rating"]))
                break

    return top_movies

def count_by_genre(movies):
    d = {}

    for movie in movies:
        for genre in movie["genres"]:
            d[genre] = d.get(genre, 0) + 1

    return d

def actor_filmography(movies):
    filmography = {}

    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []

            filmography[actor].append(movie["title"])

    return filmography

def all_genres(movies):
    s = set()

    for movie in movies:
        for genre in movie["genres"]:
            s = s | movie ["genres"]
    return s 

def common_actors(movie1, movie2):
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])

    return actors1 & actors2

def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)

    return genres_a - genres_b

def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

def build_report(movies):
    print("ОТЧЕТ ПО КАТАЛОГУ")

    print("Средний рейтинг:", average_rating(movies))

    age_stats = catalog_age_stats(movies)
    print("Средний возраст фильмов:", age_stats[2], "лет")

    print("\nТоп-3 фильма:")

    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)

    for movie in sorted_movies[:3]:
        print("  " + format_report_line(movie))

    print("\nФильмов по жанрам:")

    genre_counts = count_by_genre(movies)

    sorted_genres = sorted(
        genre_counts,
        key=genre_counts.get,
        reverse=True,
    )

    for genre in sorted_genres:
        print(f"  {genre} — {genre_counts[genre]}")

    genres = sorted(all_genres(movies))
    print("\nВсе жанры каталога:", ", ".join(genres))

def main():
    print(build_report(movies))

if __name__ == "__main__":
    main()

    