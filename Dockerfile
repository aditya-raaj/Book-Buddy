# Use the official Python image from Docker Hub
FROM python:3.10-slim



# Set working directory inside container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the rest of your app's code
COPY . /app/

# Expose port 5000 (Flask runs here by default)
EXPOSE 5000

# Run the app using gunicorn (production-grade WSGI server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
