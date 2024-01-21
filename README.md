# Card verifier

To locally run this app you should has python 3.1x version.

Than you should install the requirements using command

pip3 install -r requirements.txt

Then execute next command in command line

uvicorn main:app --host 127.0.0.1

Site should be available on http://127.0.0.1:8000/ 


You can also download the prepared docker image using command
docker pull swatswatov/test-server:latest

and then execute next command in your terminal:

docker run -it -p 8000:80 test-server    

Site should be available on http://localhost:8000/ 