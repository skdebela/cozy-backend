# cozy

## Peer-to-peer marketplace for short term rentals and lodging

## About

Cozy is a platform where users can browse, search, and book accommodations hosted by others.
This repository contains the **backend** implementation of the project, built with Django REST Framework (DRF).

---

## Features

- **User Authentication**: Sign up, log in, and manage accounts.

---

## Technologies

- **Backend**:
  - Django REST Framework (DRF): For building the API.
  - PostgreSQL: Database for managing application data.
- **Development Tools**:
  - `uv`: For dependency management.
  - Docker: For containerized development and deployment.

---

## Getting Started

### Prerequisites

1. **Install Python** (refer `.python-version` for version information).
2. **Install uv**

---

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/samuelmideksa/cozy-backend.git
   cd cozy-backend
   ```

1. **Install Dependencies**:

   ```bash
   uv sync
   ```

1. **Install Pre-Commit Hook** *(for contributors)*:

   To ensure code quality and consistency, install the pre-commit hook for `ruff` checks by running:

   ```bash
   pre-commit install
   ```

1. **Configure Environment Variables**:
   Create a `.env` file in the project root to set environment variables, you can follow the provided template `.env_template`:

1. **Run Migrations**:

   ```bash
   uv run python manage.py migrate
   ```

1. **Start the Development Server**:

   ```bash
   uv run python manage.py runserver
   ```

1. **Access the API**:
   Visit [http://localhost:8000/](http://localhost:8000/) in your browser or API client.

---

## Usage

---

## Future Work

---

## Credits

This project was developed by **Samuel M. Debela**.

---
