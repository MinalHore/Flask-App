#using the python image from the docker hub
FROM python:3.12-alpine

#set the working directory in the container
WORKDIR /app

#copy all the current directory contents into the container at /app 
COPY . /app

#installing any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

#make port available to the world outside the container
EXPOSE 5005 5007 5008

#run app.py when the container launch
#CMD python app.py

# CMD python jinja_temp.py