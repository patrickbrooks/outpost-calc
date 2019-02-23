# Running outpost-calc.py script via Docker container

These instructions create and run a Docker container that has all dependencies required to execute the outpost-calc.py script.

1. Install Docker on your system

1. Confirm that Docker is available at your command prompt
```
docker version
```

1. Check if the outpost-calc image is available on your machine. If you see 'outpost-calc' under the REPOSITORY column, then skip the 'docker build' command in the next step.
```
docker images
```

1. If needed, build the Docker image
```
# In the Git/outpost-calc directory
docker build . -t outpost-calc:latest
```

1. Confirm the new image
```
docker images
```

1. Start a container from the image. Mounting your home directory will make it easy to edit the code and re-execute it ... if you don't need this, then skip the --mount argument

```
# This command will start a bash shell inside the container
docker run -it --mount type=bind,source="c:\Users\pbrooks",target=/root outpost-calc
or
docker run -it --mount type=bind,source="/Users/pb",target=/root outpost-calc
```

1. Use the command line within the container to run the script. See README.md for more information.
```
./outpost-calc.py -h
```

1. When ready, exit the container's command line with 'exit'


# For outpost-calc.py development

At the container's bash prompt, cd to your Git/outpost-calc directory under your home directory (ex. cd /root/Git/outpost-calc). From the container's bash prompt, execute the outpost-calc.py script, then edit the script in your favorite editor outside the container, and then re-execute the script at the container's bash prompt to see your new changes. This saves you from rebuilding the Docker image after every script edit just to test your changes.
