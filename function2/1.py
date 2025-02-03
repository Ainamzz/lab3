# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def high_rated(movie):
    return movie["imdb"] > 5.5
def sublst_of_movie(movie_list):
    return [movie for movie in movie_list if high_rated(movie)]
def movie_category(movie_list, category):
    return [movie for movie in movie_list if movie["category"].lower() == category.lower()]
def average_imdb(movie_list):
    if not movie_list:
        return 0
    return sum(movie["imdb"] for movie in movie_list) / len(movie_list)
def average_category(movie_list, category):
    filtered_movies = movie_category(movie_list, category)
    return average_imdb(filtered_movies)
while True:
    print("\nChoose action: ")
    print("1 Check imdb of the movie")
    print("2. Output list of movies with high imdb")
    print("3. Output movies by categories")
    print("4. Calculate the average imdb of movies")
    print("5. Calculate average imdb by category")
    print("6. Quit")
    choise = input("\nEnter the action number")
    if choise =="1":
        movie_name = input("Enter movie name")
        movie = next((m for m in movies if m["name"].lower() == movie_name.lower()), None)
        if movie:
            print(f"Does movie '{movie['name']}' has high imdb?: ", high_rated(movie))
        else:
            print("Movie has not been found")
    elif choise == "2":
        print("\nMovies with high imdb:")
        for movie in high_rated(movies):
            print(movie["name"], "-", movie("imdb"))
    elif choise == "3":
        category = input("Enter category:")
        filtered_movies = movie_category(movies, category)
        if filtered_movies:
            print(f"\nMovies in category '{category}':")
            for movie in filtered_movies:
                print(movie["name"], "-", movie["imdb"])
        else:
            print("No such movie in this category")
    elif choise == "4":
        print("\nAverage imdb of all movies: ", average_imdb(movies))
    elif choise == "5":
        category = input("Enter category: ")
        avg_category = average_category(movies, category)
        print(f"Average imdb in '{category}'category :{avg_category}")
    elif choise == "6":
        print("Quitting the programm")
        break
    else: 
        print("Wrong comand.")