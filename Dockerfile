# Use the latest PHP image with Apache as the base image
FROM php:latest-apache

# Install PHP extensions (e.g., mysqli for MySQL support, zip, etc.)
RUN docker-php-ext-install mysqli pdo pdo_mysql zip


# Set the working directory in the container
WORKDIR /var/www/html

# Copy the PHP application files into the container
COPY projCert  /var/www/html/

# Expose port 80 to allow traffic to the Apache server
EXPOSE 80

# Define the command to run the Apache server
CMD ["apache2-foreground"]

