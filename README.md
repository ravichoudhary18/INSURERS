# Run Project

This guide will help you set up and run the project. Make sure to follow each step carefully.

## Configuration

- `.env.dev`, `sqlite3`, and `frontend/.env` files are included for testing purposes.
- **Username:** `admin`
- **Password:** `admin`

## Change Configuration

Before running the project, you need to make changes to the configuration files:

1. Open the `frontend/.env` file.
2. Replace `my ip` with your system IP address.

## Running the Project on Linux

To build and run the project, use Docker Compose:

```bash
sudo docker-compose up --build
