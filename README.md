
# CS:GO Market Analytics Platform

This is a platform for analyzing CS:GO market data.

## Features

* Fetch CS:GO market item data via API
* Store data in a MySQL database
* Provide an API for querying item data

## Tech Stack

* **Backend**: FastAPI
* **Database**: MySQL
* **ORM**: SQLAlchemy
* **Data Validation**: Pydantic

## Installation and Usage

1. **Clone the repository**

   ```bash
   git clone https://github.com/XU1hEEE/CSGO.git
   cd CSGO
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**

   * Make sure you have created a database in MySQL (e.g., `csgo_market`).
   * Modify the `DATABASE_URL` in `app/db/session.py` with your database connection information.

4. **Run the application**

   ```bash
   uvicorn app.main:app --reload
   ```

   The application will be running at `http://127.0.0.1:8000`.

## API Usage

The root path for the API is `/api/v1`.

* **Create an item**: `POST /api/v1/items/`
* **Get a list of items**: `GET /api/v1/items/`
* **Get a single item**: `GET /api/v1/items/{item_id}`

You can find the complete API documentation at `http://127.0.0.1:8000/docs`.
