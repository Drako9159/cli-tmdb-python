CLI TMDB

## Description
This is a command line interface application that allows users to search for movies and TV shows using the TMDB API. Users can search for movies and TV shows by title, genre, and year. Users can also view details about a specific movie or TV show, such as the cast, crew, and plot summary.

## Installation

1. Clone the repository
2. Install the required dependencies using the following command:
```
pip install -r requirements.txt
```

## Usage

To run the application, use the following command:
```
python cli_tmdb.py
```

## API KEY

To use the TMDB API, you will need to obtain an API key from the TMDB website. You can sign up for a free account and obtain an API key [here](https://www.themoviedb.org/documentation/api).

Set your API key as an environment variable with the following command (replace `your_api_key` with your actual API key):
```
export TMDB_API_KEY=your_api_key
```
Windows users can set the environment variable using the following command:
```
set TMDB_API_KEY=your_api_key
```
The application will prompt you to enter a search query. You can search for movies and TV shows by title, genre, and year. You can also view details about a specific movie or TV show by entering its ID.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
