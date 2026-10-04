# Author: Ebony Cornett
# Date: September 30, 2026
# Description: Movie Collection Manager that stores, displays,sorts, and analyzes a personal collection of movies.
# Tier Level Attempted: Base Level

# Test Output:
# Added Movie 1:
# Rush Hour, 1998, Action / Comedy, Rating: 7.0
# Added Movie 2:
# The Godfather, 1972, Crime / Drama, Rating: 9.2
# Movies Sorted by Year:
# The Godfather - 1972 - 9.2
# The Five Heartbeats - 1991 - 7.5
# Rush Hour - 1998 - 7.0
# The Dressmaker - 2015 - 7.0
# The Greatest Showman - 2017 - 7.5
# Hamilton - 2020 - 8.3
# Wicked - 2024 - 7.5
# Top 3 Rated Movies:
# The Godfather - 9.2
# Hamilton - 8.3
# The Five Heartbeats - 7.5
# Collection average rating: 7.71

# Creates and returns a new movie dictionary
def create_movie(title, year, genres, rating):
    movie = {
        "title": title,
        "year": year,
        "genres": genres,
        "rating": rating
    }
    return movie

# Displays all movies in a formatted table
def display_movies(movies, heading):
    print(f"\n{heading}")
    print("-" * 70)
    if len(movies) == 0:
        print("No movies in this collection.")
        return
    for movie in movies:
        genres_text = " / ".join(movie["genres"])
        print(
            f'{movie["title"]:<25} '
            f'{movie["year"]:<6} '
            f'{genres_text:<25} '
            f'{movie["rating"]:.1f}'
        )

# Returns the top-rated movies without changing the original list
def find_top_rated(movies, n):
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True
    )
    return sorted_movies[:n]

# Calculates and returns the average rating of all movies
def get_average_rating(movies):
    if len(movies) == 0:
        return 0.0
    total_rating = 0.0
    for movie in movies:
        total_rating += movie["rating"]
    average_rating = total_rating / len(movies)
    return round(average_rating, 2)

# Starter movie collection
movies = [
    {
        "title": "The Five Heartbeats",
        "year": 1991,
        "genres": ["Drama", "Music"],
        "rating": 7.5
    },
    {
        "title": "Hamilton",
        "year": 2020,
        "genres": ["Biography", "Drama", "Musical"],
        "rating": 8.3
    },
    {
        "title": "The Greatest Showman",
        "year": 2017,
        "genres": ["Biography", "Drama", "Musical"],
        "rating": 7.5
    },
    {
        "title": "The Dressmaker",
        "year": 2015,
        "genres": ["Comedy", "Drama"],
        "rating": 7.0
    },
    {
        "title": "Wicked",
        "year": 2024,
        "genres": ["Fantasy", "Musical"],
        "rating": 7.4
    }
]

# Update a value in an existing movie dictionary
movies[4]["rating"] = 7.5

# Display the original movie collection
display_movies(movies, "Your Movie Collection")

# Ask the user to add two new movies
for movie_number in range(1, 3):
    print(f"\nEnter Movie {movie_number}")
    title = input("Title: ")
    year = int(input("Year: "))
    genres_input = input("Genres (separated by commas): ")
    rating = float(input("Rating: "))
    genres = [genre.strip() for genre in genres_input.split(",")]
    new_movie = create_movie(title, year, genres, rating)
    movies.append(new_movie)

# Sort the movies by year
movies.sort(key=lambda movie: movie["year"])

# Display the sorted movie collection
display_movies(movies, "All Movies Sorted by Year")    

# Find the top 3 rated movies
top_movies = find_top_rated(movies, 3)

# Display the top 3 rated movies
display_movies(top_movies, "Top 3 Rated Movies")

# Calculate and display the average rating
average_rating = get_average_rating(movies)
print(f"\nCollection average rating: {average_rating:.2f}")