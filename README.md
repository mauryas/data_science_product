
  

  

# Data Science Product

  

  

  
A sample project to demonstrate the use of different tools for development of production ready data science project. The solution for the task is developed as a python package and its use is demonstrated in a containerized Jupyter Lab notebook and a sample RESTful API based on FastAPI.

The solution for the task is developed into a python module and available in the folder `/tasks`. Further examples can be found in `notebooks/01_task_solution.ipynb` and as API endpoints `/points/closest` and `/tree/train`. 

  

  

The template is developed keeping data scientist/analyst and backend/frontend developers in mind. The template contains:  

  

- python package: A custom package is created which can be used to develop an application.

  

- JupyterLab notebooks: The package can be used in the notebooks for interactive examples and analysis by data scientst/ analysts.

  

- API: The API can be used by backend or froentend developers within or outside the organisation to use the custom package with abstraction technical details of the code.

  

  

The project has used the following tools and methods:

  

- Docker and docker compose 

  

Docker provides a standardized environment for applications, reducing the likelihood of deployment issues and ensuring consistent performance across different environments. This translates to faster development cycles and quicker time-to-market for products. Docker Compose simplifies the orchestration of multi-container applications, allowing developers to define and manage complex application stacks effortlessly.

  

- JupyterLab

  

JupyterLab is used for its interactive nature, ease of use, documentation features, and integration with the broader data science ecosystem. It provides an ideal environment for samples of usage of package in an interactive and visually engaging manner.

  

- FastAPI for RESTful API 

  

While JupyterLab provides an analysis and prototyping use of package, Fast API provides possibility to serve a data science solution in a scalable and production ready solution with documentation.

  

- Pytest

  

Pytest is a powerful testing framework for Python. It provides possibility to create automated test for reliability and bug free product.

  

- Makefile

  

Makefiles are like handy instruction manuals for your software projects. They contain a list of tasks that need to be done, and helps to manage the task easier. For example, a Makefile, you can define commands for repetitive task with just a simple command like "make build" or "make test".

  

- Github actions for CI/CD 

  

GitHub Actions can be configure for CI/CD in a project. It automates the repetitive checks for bug free a product and deploy the code. It makes your development and delivery process smoother and less error-prone.

  

  

  

## Prerequisites

  

  

  

Before proceeding, ensure you have installed the following:

  

  

  

- [Docker](https://docs.docker.com/engine/install/)

  

  

- [Docker Compose](https://docs.docker.com/compose/install/)

  

  

- [make](https://www.gnu.org/software/make/)

  

  

  

## Setting Up the Environment

  

  

  

1. Clone the project repository:

  

  

```bash

  

  

git  clone  git@github.com:mauryas/data_science_product.git

  

  

```

  

  

  

2. Navigate into the project directory:

  

  

```bash

  

  

cd  data_science_product

  

  

```

  

  

  

3. Build and start the Docker services using Docker Compose:

  

  

```bash

  

  

make  all

  

  

```

  

  

  

This will create and run the Docker containers for FastAPI, and Jupyter Lab.

  

  

## Makefile Commands and Descriptions

  

  

  

The Makefile provides convenient commands for managing the Docker services and executing other projects like clean code, Pytest, etc. Here's a summary of the commands and their descriptions:

  

  

  

-  `make all`: Builds the Docker images and starts the Docker containers.

  

  

  

-  `make build`: Builds the Docker images and starts the Docker containers.

  

  

  

-  `make run`: Starts the Docker containers if they are not already running.

  

  

  

-  `make stop`: Stops the Docker containers.

  

  

  

-  `make start-api`: Starts the Docker container for the FastAPI service.

  

  

  

-  `make stop-api`: Stops the Docker container for the FastAPI service.

  

  

  

-  `make start-jupyter`: Starts the Docker container for the Jupyter Lab service.

  

  

  

-  `make stop-jupyter`: Stops the Docker container for the Jupyter Lab service.

  

  

  

-  `make clean`: Stops the Docker containers and removes the volumes.

  

  

  

-  `make run-tests`: Executes Pytest within the Docker container for the API service.

  
  
  
  
  

## Installing package

  
  
  

The package can be installed with command:

  
  
  

```
pip install git+https://github.com/mauryas/data_science_product.git

```

  

  

  

## Task Example


The code sample for usage of the custom package:

#### Find closest city

  
  
  

```
import pandas as pd

from data_science_product.tasks.nearest_point import PointMap, Point #module to calculte euclidian distance.

df = pd.read_csv('data/raw_data/sample_distance.csv') # load sample file

points_obj = PointMap()

points_obj.parse_dataframe(df)

points_obj.print_points()

  

closest_point = points_obj.calculate_closest_point(Point('City 2', 17, 11))

closest_point.print_point()
```

#### Extract classification rules

```
import pandas as pd

  

from data_science_product.tasks.decision_tree import DecisionTreeTrainer, FeatureEnginerring

from data_science_product.tasks.constants import DECISION_TREE_TARGET

  

df = pd.read_csv('data/raw_data/buy_computer.csv', dtype=str)

  
  

decision_tree_trainer = DecisionTreeTrainer() # Instantiate DecisionTreeTrainer

  

X = decision_tree_trainer.preprocessing(df) # Preprocessing

y = df[DECISION_TREE_TARGET]

  

decision_tree_trainer.print_rules(X, y) # print the rules

  

# Train decision tree with cross-validation

accuracy = decision_tree_trainer.train_with_cross_validation(X, y)

print(f'Mean accuracy across all folds {round(accuracy, 4)}')

```

  

  

## Accessing Jupyter Lab

  

  

  

Once the Docker services are running, you can access Jupyter Lab by opening your web browser and navigating to the following URL:

  

  

  

```
http://localhost:8889
```

  

  

  

The solutions for the tasks are available in a notebook named `notebook/01_task_solution.ipynb`.

  

  

## Accessing API

  

  

  
The API can be accesed by running the `make start-api`, open the web browser and navigating to the following URL:

  

  

  

```
http://localhost:8888/docs
```

  

  

  

To find the closes distance, you can access the api endpoint `points/closest` and `tree/train` for accessing accuracy of the trained decision tree model.

  

  

## Additional Information

  

  

  

- The FastAPI application is running on port `8888`. You can interact with the API using swagger UI `http://localhost:8888/docs#/` , curl or other HTTP clients.

  

  

  

- For more detailed information on using Jupyter Lab and FastAPI, refer to their respective documentation.
