import pandas as pd
import os

# Step 1: Load or Create the Dataset
def load_dataset(file_path=None):
    """
    Load the dataset from a given file path. Supports CSV or JSON formats.
    Cleans and normalizes the data to handle real-world challenges.
    """
    if file_path:
        try:
            if file_path.endswith('.json'):
                df = pd.read_json(file_path)
            elif file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            else:
                print("Unsupported file format. Please use a .csv or .json file.")
                return pd.DataFrame()

            # Normalize column names
            df.columns = df.columns.str.strip().str.lower()

            # Handle messy data
            if 'year' in df.columns:
                df.rename(columns={'year': 'release year'}, inplace=True)
            if 'runtime' in df.columns:
                # Convert runtime to numeric (e.g., "90 minutes" -> 90)
                df['runtime'] = pd.to_numeric(df['runtime'].str.extract(r'(\d+)')[0], errors='coerce')

            # Drop irrelevant columns like 'BoxOffice' if they exist
            irrelevant_columns = set(df.columns) - {"title", "genre", "release year", "rating", "actors", "runtime"}
            if irrelevant_columns:
                df.drop(columns=irrelevant_columns, inplace=True)

            # Handle missing or inconsistent values
            df["release year"] = pd.to_numeric(df["release year"], errors='coerce')
            df["rating"] = pd.to_numeric(df["rating"], errors='coerce')
            df.dropna(subset=["title", "genre", "release year", "rating"], inplace=True)

            # Remove duplicates
            df.drop_duplicates(inplace=True)

            print("Dataset loaded and cleaned.")
            return df
        except Exception as e:
            print(f"Error reading the dataset: {e}")
            return pd.DataFrame()
    else:
        # Create a default dataset if no file is provided
        print("No file provided. Creating a sample dataset.")
        data = {
            "Title": ["Inception", "Titanic", "The Dark Knight", "Interstellar", "The Matrix"],
            "Genre": ["Action", "Drama", "Action", "Sci-Fi", "Sci-Fi"],
            "Release Year": [2010, 1997, 2008, 2014, 1999],
            "Rating": [8.8, 7.8, 9.0, 8.6, 8.7],
            "Actors": ["Leonardo DiCaprio", "Kate Winslet", "Christian Bale", "Matthew McConaughey", "Keanu Reeves"],
        }
        return pd.DataFrame(data)

# Step 2: Get User Preferences
def get_user_preferences():
    print("\nWelcome to the Movie Recommendation System!")
    genre = input("Enter a genre (e.g., Action, Drama, Comedy): ").strip()
    try:
        min_rating = float(input("Enter a minimum rating (e.g., 7.5): ").strip())
    except ValueError:
        print("Invalid rating. Defaulting to 0.")
        min_rating = 0
    while True:
        try:
            min_year = int(input("Enter a minimum release year (e.g., 2000): ").strip())
            break  # Exit the loop once a valid year is entered
        except ValueError:
            print("Invalid year. Please enter a valid numeric year.")
    return genre, min_rating, min_year

# Step 3: Filter Movies
# Step 3: Filter Movies
def filter_movies(df, genre, min_rating, min_year):
    """
    Filter movies based on the user preferences:
    - Genre: Matches movies containing the input genre (case-insensitive).
    - Minimum Rating: Includes movies with a rating >= min_rating.
    - Minimum Release Year: Includes movies released during or after the specified year.
    """
    print(f"\nFiltering movies for genre: {genre}, min_rating: {min_rating}, min_year: {min_year}")
    
    filtered = df[
        (df["genre"].str.contains(genre, case=False, na=False)) &  # Matches genre
        (df["rating"] >= min_rating) &                             # Matches rating
        (df["release year"] >= min_year)                           # Matches release year
    ]

    if filtered.empty:
        print("No movies found matching the criteria.")
    else:
        print(f"Found {len(filtered)} movies matching the criteria.")
    
    return filtered

# Step 4: Add a New Movie
def add_new_movie(df, filename):
    print("\nAdd a New Movie to the Dataset")
    title = input("Enter the movie title: ").strip()
    genre = input("Enter the genre: ").strip()
    try:
        release_year = int(input("Enter the release year: ").strip())
    except ValueError:
        print("Invalid year. Skipping addition.")
        return df
    try:
        rating = float(input("Enter the rating (e.g., 8.5): ").strip())
    except ValueError:
        print("Invalid rating. Skipping addition.")
        return df
    actors = input("Enter the main actors (comma-separated): ").strip()

    new_movie = pd.DataFrame({
        "Title": [title],
        "Genre": [genre],
        "Release Year": [release_year],
        "Rating": [rating],
        "Actors": [actors]
    })

    df = pd.concat([df, new_movie], ignore_index=True)
    df.to_csv(filename, index=False)
    print("Movie added successfully!")
    return df

# Main Program Loop
def main():
    print("Welcome to the Movie Recommendation System!")
    file_path = input("Enter the file path for the dataset (or press Enter to use the default): ").strip()
    
    movies_df = load_dataset(file_path)
    
    if movies_df.empty:
        print("No data loaded. Exiting.")
        return

    while True:
        print("\nWhat would you like to do?")
        print("1. Get movie recommendations")
        print("2. Add a new movie")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            genre, min_rating, min_year = get_user_preferences()
            recommendations = filter_movies(movies_df, genre, min_rating, min_year)
            if recommendations.empty:
                print("\nNo movies found matching your criteria.")
            else:
                print("\nRecommended Movies:")
                print(recommendations)
        elif choice == "2":
            movies_df = add_new_movie(movies_df, file_path)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
