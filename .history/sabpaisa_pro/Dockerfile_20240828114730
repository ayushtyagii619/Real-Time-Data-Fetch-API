# Use the official Python image from the Docker Hub
FROM python:3.12.3

# Set environment variables


# Set the working directory
WORKDIR /app

<<<<<<< HEAD:sabpaisa_pro/Dockerfile

=======
>>>>>>> 35a2e3697b3a3753cb397ed0de5398663575b417:Dockerfile
# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt



# Copy the project code into the container
<<<<<<< HEAD:sabpaisa_pro/Dockerfile
COPY . /app/



=======
COPY . .

>>>>>>> 35a2e3697b3a3753cb397ed0de5398663575b417:Dockerfile
# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .
CMD ["python", "sabpaisa_pro/manage.py", "runserver", "0.0.0.0:8000"]

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .
RUN ls
#RUN cd app/sabpaisa_pro
# Expose the port your app runs on
EXPOSE 8000

# Run migrations and collect static files
#RUN python manage.py migrate
#RUN python manage.py collectstatic --noinput

# Start the Django development server
<<<<<<< HEAD:sabpaisa_pro/Dockerfile


=======
CMD ["python", "sabpaisa_pro/manage.py", "runserver", "0.0.0.0:8000"]
>>>>>>> 35a2e3697b3a3753cb397ed0de5398663575b417:Dockerfile
