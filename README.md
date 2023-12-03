
# Data Science Product

  

This project demonstrates how to set up a development environment using Docker Compose with Jupyter Lab and FastAPI. The solution for the task is developed into a python module and available in the folder `/tasks`. 
The solution for the task is available in `notebooks/01_task_solution.ipynb` and as API endpoints `/points/closest` and `/tree/train`.
The project has used:
- Docker for containerization
- JupyterLab for analysis
- FastAPI for API development
- Pytest for testing application
- make utility for running tasks
- Github actions for CI/CD automation 

  

## Prerequisites

  

Before proceeding, ensure you have installed the following:

  

- Docker

- Docker Compose

- make

  

## Setting Up the Environment

  

1. Clone the project repository:

```bash

git clone git@github.com:mauryas/data_science_product.git

```

  

2. Navigate into the project directory:

```bash

cd data_science_product

```

  

3. Build and start the Docker services using Docker Compose:

```bash

make all

```

  

This will create and run the Docker containers for FastAPI, and Jupyter Lab.

  


## Makefile Commands and Descriptions

  

The Makefile provides convenient commands for managing the Docker services and executing other projects like clean code, Pytest, etc. Here's a summary of the commands and their descriptions:

  

-  `make all`: Builds the Docker images and starts the Docker containers.

 

- `make build`: Builds the Docker images and starts the Docker containers.

  

-  `make run`: Starts the Docker containers if they are not already running.

  

-  `make stop`: Stops the Docker containers.

  

-  `make start-api`: Starts the Docker container for the FastAPI service.

  

-  `make stop-api`: Stops the Docker container for the FastAPI service.

  

-  `make start-jupyter`: Starts the Docker container for the Jupyter Lab service.

  

-  `make stop-jupyter`: Stops the Docker container for the Jupyter Lab service.

  

-  `make clean`: Stops the Docker containers and removes the volumes.

  

-  `make run-tests`: Executes Pytest within the Docker container for the API service.

  
  

## Accessing Jupyter Lab

  

Once the Docker services are running, you can access Jupyter Lab by opening your web browser and navigating to the following URL:

  

```

http://localhost:8889

```

  

The solutions for the tasks are available in a notebook named `notebook/01_task_solution.ipynb`. 
  

## Accessing API

  

Once the Docker services are running, you can access API by opening your web browser and navigating to the following URL:

  

```

http://localhost:8888/docs

```

  

To find the closes distance, you can access the api endpoint  `points/closest` and `tree/train` for accessing accuracy of the trained decision tree model. 
  

## Additional Information

  

- The FastAPI application is running on port `8888`. You can interact with the API using swagger UI `http://localhost:8888/docs#/` , curl or other HTTP clients.

  

- For more detailed information on using Jupyter Lab and FastAPI, refer to their respective documentation.
