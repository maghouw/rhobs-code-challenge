# RHOBS Data Engineering restitution

This is a restitution for RHOBS' code challenge for the "Data engineering / Infrastructure backend / Calcul statistique / Gestion de bases de données" internship position. It demonstrates the usage of MongoDB and Python.

## Requirements:

- Python 3.x
- Docker
- pymongo
- tqdm

## Setup

1. Clone the repository
2. Install the required packages using
~~~~
pip install -r requirements.txt
~~~~
3. Launch MongodB using the **setup_mongo.sh** file with the **mongo_credentials.json** credentials
~~~~python
{
"host": "localhost",
"port": 6001,
"username": "admin",""
"password": "mdp3"
}
~~~~

## Setting up MongoDB within a Docker container

The method used is detailed [here](https://medium.com/@szpytfire/setting-up-mongodb-within-a-docker-container-for-local-development-327e32a2b68d) (last accessed on the Second of February 2023)

Step 1: Install Docker on your local machine

Step 2: Set up a MongoDB Docker container

Pull down the pre-built mongo image from the Docker repository:

~~~~
docker pull mongo
~~~~

Start a Docker container:

~~~~
docker run
-d
--name YOUR_CONTAINER_NAME_HERE
-p YOUR_LOCALHOST_PORT_HERE:27017
-e MONGO_INITDB_ROOT_USERNAME=YOUR_USERNAME_HERE
-e MONGO_INITDB_ROOT_PASSWORD=YOUR_PASSWORD_HERE
mongo
~~~~