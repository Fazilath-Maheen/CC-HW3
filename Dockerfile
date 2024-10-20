# Use a slim Python image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /home/data

# Copy the text files and the Python script into the container
COPY IF.txt AlwaysRememberUsThisWay.txt /home/data/
COPY scripts.py /home/data/

# Set the script to run when the container starts
CMD ["python", "/home/data/scripts.py"]
