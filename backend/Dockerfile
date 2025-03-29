# Use official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy dependencies file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend code into the container
COPY . .

# Expose port 5000 for the backend API
EXPOSE 5000

# Run the backend server (adjust if using Flask)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
