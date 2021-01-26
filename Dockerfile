FROM python:3.7-alpine

RUN mkdir /app

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file in the work directory
COPY requirements.txt /app

# copy all the content of this directory to working directory
COPY . . 

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Pass green unicorn the name of the entry point
CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:80", "app:app"]
