# Movie Ratings Analyzer

# Function to calculate average rating
def calculate_average(ratings):
    return sum(ratings) / len(ratings) if ratings else 0

# Function to classify movie based on average rating
def classify_rating(avg):
    if avg >= 8.5:
        return "Excellent"
    elif avg >= 7.0:
        return "Good"
    elif avg >= 5.0:
        return "Average"
    else:
        return "Poor"

# Main function to process multiple movies
def analyze_movies():
    movie_data = {}  # Dictionary to store results

    num_movies = int(input("Enter number of movies to analyze: "))  # INPUT
    for i in range(num_movies):  # LOOP over movies
        title = input(f"\nEnter title of movie {i+1}: ")
        ratings = []

        num_ratings = int(input(f"How many ratings for '{title}'? "))
        for j in range(num_ratings):  # LOOP over ratings
            r = float(input(f"Enter rating {j+1} (0–10): "))
            if 0 <= r <= 10:  # CONDITIONAL to validate rating
                ratings.append(r)
            else:
                print("❌ Invalid rating ignored.")

        # Built-in functions: sum, len, max, min
        avg = calculate_average(ratings)
        highest = max(ratings) if ratings else None
        lowest = min(ratings) if ratings else None
        category = classify_rating(avg)

        # Store results using built-in dictionary
        movie_data[title] = {
            "Average": round(avg, 2),
            "Highest": highest,
            "Lowest": lowest,
            "Category": category
        }

    # Final output
    print("\n📊 Movie Ratings Summary:")
    for title, info in movie_data.items():  # LOOP to display results
        print(f"\n{title}:")
        for key, value in info.items():
            print(f"  {key}: {value}")

# Run the program
analyze_movies()
