# Apple-to-Spotify

A Python script that migrates your Apple Music library to Spotify. This project lets you automatically create a Spotify playlist containing all your Apple Music songs.

---

## Features

* Authenticate with Spotify using OAuth.
* Read your Apple Music library from a CSV.
* Search for songs on Spotify and add them to a playlist.
* Handle large libraries efficiently with batching and rate limit management.
* Logs songs that couldn’t be found for manual review.
* Keeps your music safe locally for future migrations.

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/Apple-to-Spotify-converter.git
cd Apple-to-Spotify
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Setup

1. Create a Spotify developer app at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Copy your `Client ID`, `Client Secret`, and set a redirect URI.
3. Create a `.env` file based on `.env.example` and fill in your credentials:

```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
SPOTIFY_REDIRECT_URI=your_redirect_uri
```

---

## Usage

1. Prepare your combined CSV of Apple Music songs (or use `sample_library.csv` for testing).
2. Run the script:

```bash
python main.py
```

3. Watch as the script searches for each song and adds them to your Spotify playlist.
4. After completion, any songs not found will be saved in `not_found.txt`.

---

## Notes

* Only push **safe files** to GitHub: `apple_to_spotify.py`, `README.md`, `requirements.txt`, `.env.example`, `sample_library.csv`.
* Keep your `.env` file private — it contains sensitive credentials.

