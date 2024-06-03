#!/bin/bash

# Setting up the development server CRF-Only Images

#http://localhost:8070/ is the server this is hosted on 
docker pull lfoppiano/grobid:0.8.0

docker run --rm --init --ulimit core=0 -p 8070:8070 lfoppiano/grobid:0.8.0
