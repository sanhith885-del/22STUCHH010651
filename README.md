# URL Shortener Microservice

This project is a robust HTTP URL Shortener Microservice built using FastAPI. It provides core URL shortening functionality along with basic analytical capabilities for the shortened links. The service is designed to be efficient, scalable, and easy to use.

## Features

- Shorten long URLs into compact, shareable links.
- Redirect users from shortened URLs to the original URLs.
- Track analytics for shortened links, including the number of clicks.
- Integrates logging middleware for monitoring requests and responses.

## Project Structure

```
url-shortener-microservice
├── src
│   ├── main.py               # Entry point of the FastAPI application
│   ├── api
│   │   └── routes.py         # API endpoints for URL shortening and analytics
│   ├── models
│   │   └── url.py            # Data model for URLs
│   ├── services
│   │   └── shortener.py      # Core logic for URL shortening
│   ├── middleware
│   │   └── logging.py        # Logging middleware
│   └── analytics
│       └── stats.py          # Analytical capabilities for shortened links
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── .env                       # Environment variables
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd url-shortener-microservice
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables in the `.env` file as needed.

## Usage

To run the FastAPI application, execute the following command:

```
uvicorn src.main:app --reload
```

You can access the API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

- `POST /shorten`: Create a shortened URL.
- `GET /{shortcode}`: Redirect to the original URL.
- `GET /analytics/{shortcode}`: Retrieve analytics for a shortened link.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.