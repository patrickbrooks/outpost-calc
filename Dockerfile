#
# Outpost Calculator (outpostcalc)
#
# See Docker instructions in Dockerfile_README.md
#
FROM python:3-alpine

RUN apk add --no-cache bash bash-doc bash-completion
# util-linux coreutils findutils grep less groff

RUN mkdir -p /opt
WORKDIR /opt

# COPY requirements.txt /opt
# RUN pip install --no-cache-dir -r requirements.txt

# copy the scripts to /opt
COPY . /opt

CMD ["/bin/bash"]
