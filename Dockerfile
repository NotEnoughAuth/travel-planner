# FROM python
# RUN pip install flask
# COPY ./static /home/myapp/static/
# COPY ./templates /home/myapp/templates/
# COPY sample_app.py /home/myapp/
# EXPOSE 8080
# CMD python3 /home/myapp/sample_app.py

# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Run app.py when the container launches
CMD ["python", "main.py"]