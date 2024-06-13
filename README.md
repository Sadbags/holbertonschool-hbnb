# HBNB Evolution Project

This repository includes the first stage of Holberton School project that consist on creating a simple and limited version of the Airbnb website. A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

## Environment
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)


# Files

#### `models/` directory contains classes used for this project:
[basemodel.py](/models/basemodel.py) - The BaseModel class from which future classes will be derived


Classes inherited from Base Model:
* [amenity.py](/models/amenity.py)
* [city.py](/models/city.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [state.py](/models/state.py)
* [user.py](/models/user.py)


## Models file Structure

|File|Description|Recommendations
|---|---|---
|[amenity.py](./models/engine/amenity.py)|Amenity class| Inherits from BaseModel and contains specific public attributes
|[basemodel.py](./models/engine/base_model.py)| Base Model class|  Defines all common attributes/methods for other classes sach as id, datetime
|[city.py](./models/engine/city.py)|City Class| Inherits from BaseModel and contains specific public attributes
|[place.py](./models/engine/place.py)|Place Class| Inherits from BaseModel and contains specific public attributes
|[review.py](./models/engine/review.py)|Review Class| Inherits from BaseModel and contains specific public attributes
|[country.py](./models/engine/country.py)|Country Class| Inherits from BaseModel and contains specific public attributes
|[user.py](./models/engine/user.py)|User Class| Inherits from BaseModel and contains specific public attributes

# Importance of Testing Files
Testing files are crucial because they operate with:

## Unit Tests:

- They verify that each component functions in isolation.
- They detect errors in the logic of individual methods and functions.
- They facilitate development by providing immediate feedback on code correctness.

## Integration Tests:

- They verify that multiple components work together.
- They detect issues in the interaction between modules, such as errors in handling HTTP requests.
- They ensure that the application responds correctly to user interactions and that API endpoints function as expected.

Both types of tests are essential to ensure the quality and reliability of the application, allowing developers to identify and fix errors before the code reaches production.



# Test Files
* [test_amenety.py](/models/test/test_amenety.py)
* [test_city.py](/models/test/test_city.py)
* [test_place.py](/models/test/test_place.py)
* [test_review.py](/models/test/test_review.py)
* [test_state.py](/models/test/test_state.py)
* [test_user.py](/models/test/test_user.py)


## Run Tests
To run the model and API tests, use the following commands:

```
python3 -m unittest Model.tests.test_place
```
* 
## Dockerization

### `Dockerfile`
```
# Use an Alpine Linux base image with Python
FROM python:3.9-alpine

# Set environment variables
ENV PORT 8000

# Create and set the working directory
WORKDIR /app

# Install system dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Copy the requirements file
COPY requirements.txt /app/
```

## Build the Docker Image
```
docker build -t flask-app .
```

## Run the Docker Container
```
docker run -d -p 8000:8000 --name myapp_container -v /Users/glorisabelriverarodriguez/Desktop/myapp_data:/app/
data myapp:latest
```

## Access the Application
Accede a la aplicación en http://localhost:8000.

## Configure Environment Variables
To override the port when running the container:
```
docker run -d -p 8000:8000 -v $(pwd)/data:/app/data -e PORT=8000 --name flask-app-container flask-app
```

## Authors
Glorisabel Rivera - [Github](https://github.com/glorisabelriv)   
Bryan Garcia - [Github](https://github.com/Sadbags)

## License
Public Domain. No copy write protection.
