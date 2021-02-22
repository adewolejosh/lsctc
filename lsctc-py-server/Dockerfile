# Use an official Python runtime as a parent image
FROM python:3.6

# Adding backend directory to make absolute filepaths consistent across services
WORKDIR /lsctc-py-server

# Install Python dependencies
COPY requirements.txt /lsctc-py-server
RUN pip3 install --upgrade pip -r requirements.txt

# Add the rest of the code
COPY . /lsctc-py-server

# Make port 8000 available for the app
EXPOSE 8000

# Be sure to use 0.0.0.0 for the host within the Docker container,
# otherwise the browser won't be able to find it
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]