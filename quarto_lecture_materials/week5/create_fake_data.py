import csv
import random

# Lists of names and diets
names = ["Michael Jordan", "Tom Hanks", "Arya Stark", "Goku", "Scarlett Johansson", 
         "Mickey Mouse", "Hermione Granger", "Naruto", "Serena Williams", "Oprah Winfrey",
         "Leonardo DiCaprio", "Mario", "Taylor Swift", "Darth Vader", "James Bond",
         "Usain Bolt", "Tony Stark", "Bugs Bunny", "The Rock", "Walter White",
         "Sheldon Cooper", "Mulan", "Elsa", "Sherlock Holmes", "Jack Sparrow",
         "Luffy", "Luke Skywalker", "Marilyn Monroe", "Freddie Mercury", "Lady Gaga",
         "Superman", "Wonder Woman", "Neo", "Beyonce", "Ash Ketchum",
         "Lara Croft", "Elvis Presley", "Kermit the Frog", "Spider-Man", "Hannibal Lecter",
         "Indiana Jones", "Simba", "Rihanna", "Dexter Morgan", "Morpheus",
         "Wolverine", "Cinderella", "Captain America", "Thor", "Katniss Everdeen"]

movies_by_genre = {
    "Drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather", "Titanic", "Fight Club"],
    "Action": ["The Dark Knight", "Avengers: Endgame", "Pulp Fiction", "Jurassic Park", "Lord of the Rings: The Fellowship of the Ring"],
    "Sci-Fi": ["Inception", "The Matrix", "Back to the Future", "Star Wars: Episode IV", "Blade Runner"],
    "Animation": ["The Lion King", "Toy Story", "Frozen", "Finding Nemo", "Shrek"],
    "Classic": ["Casablanca", "Jaws", "Gone with the Wind", "Psycho", "Citizen Kane"]
}

parties = ["very left wing", "left wing", "right wing", "very right wing"]

diets = ["plant-heavy", "meat-heavy", "fruit-heavy", "balanced", "dairy-heavy"]

# Generate 50 records
records = [["name", "favorite_movie", "second_favorite_movie", "preferred_political_party", "ideal_diet"]]
for _ in range(500):
    name = random.choice(names)
    genre = random.choice(list(movies_by_genre.keys()))
    movie = random.choice(movies_by_genre[genre])
    movie2 = random.choice(movies_by_genre[genre])
    party = random.choice(parties)
    diet = random.choice(diets)
    records.append([name, movie, movie2, party, diet])

# Write to a CSV file
with open("fake_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(records)

# Display the first few rows
for row in records[:5]:
    print(", ".join(row))
