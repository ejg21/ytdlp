# Use the official Node.js image
FROM node:18

# Set the working directory inside the container
WORKDIR /app

# Copy package files and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the frontend code into the container
COPY . .

# Build the frontend
RUN npm run build

# Install `serve` for static file serving
RUN npm install -g serve

# Expose port 3000 for the frontend
EXPOSE 3000

# Serve the frontend build folder
CMD ["serve", "-s", "build", "-l", "3000"]
