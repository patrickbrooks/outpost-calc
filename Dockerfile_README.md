# Running outpost_calc.py script and outpost-calc-web.py flask application via Docker containers

These instructions create and run a Docker container that executes the outpost-calc-web.py flask application.

1. Install Docker on your system

1. Confirm that Docker is available at your command prompt
```
docker version
```

1. Build the Docker image
```
# In the Git/outpost-calc directory
docker build . -t outpost-calc:latest

# Alternately, use the Makefile
make image
```

1. Confirm the new image
```
docker images
```

1. Start a container from the image
```
docker run --name outpost-calc -d -p 8000:5000 --rm outpost-calc:latest

# Alternately, use the Makefile
make run

# The web application will be available on port 8000
http://localhost:8000
```

1. If you are developing, then use a virtual enviornment instead of a container. 
```
# in Powershell
venv\Scripts\Activate.ps1
$env:FLASK_ENV = "development" 
$env:FLASK_APP = "outpost-calc-web"
flask run

# in Bash
source venv/bin/activate
export FLASK_ENV=development
export FLASK_APP=outpost-calc-web
flask run

# then access the web app with 
http://localhost:5000

# or run the outpost_calc.py script directly
(flask) $ ./outpost-calc.py -h
```
