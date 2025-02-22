
# Django E-commerce Platform

This project is a simple e-commerce platform built using Django, with a PostgreSQL database. It is dockerized for easy setup and deployment, and it includes a CI/CD pipeline using GitHub Actions to automate testing.

## Project Structure

- **`docker-compose.yml`**: Defines the services for the PostgreSQL database and Django application.
- **`.github/workflows/django-ci-pipeline.yml`**: Defines the GitHub Actions CI/CD pipeline for testing and building the project.
- **`requirements.txt`**: Contains all Python dependencies required to run the project.

## Features

- **Django-based e-commerce backend** with functionality for product, stock, and category management (CRUD operations).
- **PostgreSQL** database for data storage.
- **Docker** for containerizing the application and database for easy local development and deployment.
- **GitHub Actions** for Continuous Integration (CI) to automatically test code on every push to the `main` branch.

## Requirements

- Docker
- Docker Compose
- Python 3.10 or higher

## Getting Started

Follow the steps below to get the project up and running locally.

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Build and Start the Containers

This project uses Docker Compose to set up the Django app and PostgreSQL database. Run the following commands to build and start the containers:

```bash
docker-compose up --build
```

This will build the Docker images and start the containers for the Django app (`web`) and the PostgreSQL database (`db`).

### 3. Apply Migrations

Once the containers are up and running, run the following command to apply the database migrations:

```bash
docker-compose exec web python manage.py migrate
```

### 4. Create a Superuser

To access the Django admin interface, you'll need to create a superuser. Run the following command:

```bash
docker-compose exec web python manage.py createsuperuser
```

Follow the prompts to set the username, email, and password.

### 5. Access the Application

After everything is set up, you can access the application in your web browser:

- **Django app**: [http://localhost:8000](http://localhost:8000)
- **Django admin**: [http://localhost:8000/admin](http://localhost:8000/admin)

Log in using the superuser credentials you created earlier.

### 6. Stopping the Containers

When you're done working on the project, you can stop the containers by running:

```bash
docker-compose down
```

This will stop the running containers and remove them.

## CI/CD Pipeline

This project includes a CI pipeline that is triggered on every push to the `main` branch. The pipeline installs dependencies, runs tests, and performs other setup tasks.

### GitHub Actions Workflow

- The workflow file is located at `.github/workflows/django-ci-pipeline.yml`.
- It installs Docker, Docker Compose, and Python dependencies.
- It runs tests after the setup step to ensure that the project is working as expected.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
