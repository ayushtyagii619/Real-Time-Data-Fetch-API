# Dockerfile

# Use the official MySQL image from the Docker Hub
FROM mysql:8.0

# Set environment variables
ENV MYSQL_ROOT_PASSWORD="Tyagi@2588"
ENV MYSQL_DATABASE="spreporportal"
ENV MYSQL_USER="root"
ENV MYSQL_PASSWORD="Tyagi@2588"

# Expose the MySQL port
EXPOSE 3306
