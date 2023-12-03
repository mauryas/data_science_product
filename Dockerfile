# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /src

# Install any needed packages specified in requirements.txt
COPY requirements.txt /src
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Jupyter Lab will run on
EXPOSE 8889

# Expose the port that FastAPI will run on
EXPOSE 8888

COPY . /src
ENV PYTHONPATH=/src

# Start Jupyter Lab and FastAPI
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8889", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
CMD ["uvicorn", "your_fastapi_app:app", "--host", "0.0.0.0", "--port", "8888"]
