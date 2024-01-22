# BIN verifier

## Description

This service checks information of bank by BIN number. If there is no information<br> for requested BIN
or request was invalid, user will see an error on UI.


## Launch
To launch this app locally you should has python 3.1x version.

Then you should install the requirements using command

    pip3 install -r requirements.txt

After that execute next command in command line

    uvicorn main:app --host 127.0.0.1

Site should be available on **http://127.0.0.1:8000/**


OR you can download the prepared docker image using command

    docker pull swatswatov/test-server:latest

And then execute next command in your terminal:

    docker run -it -p 8000:80 swatswatov/test-server:latest  

Site should be available on **http://localhost:8000/**
