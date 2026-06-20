movies = {
    "Action": ["Salaar", "KGF", "Pushpa"],
    "Comedy": ["Jathi Ratnalu", "MAD", "F2"],
    "Drama": ["Jersey", "Hi Nanna", "Maharshi"],
    "Thriller": ["Hit", "Drushyam", "Agent Sai Srinivasa Athreya"]
}

print("Available genres:")
for genre in movies:
    print("-", genre)

choice = input("\nEnter your favorite genre: ").title()

if choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[choice]:
        print(movie)
else:
    print("Genre not found.")