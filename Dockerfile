FROM python:3.9.1

# Make a directory for our application
WORKDIR /parserapp
# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy our source code
COPY parser.py .

# Run the application
CMD ["python", "parser.py"]
