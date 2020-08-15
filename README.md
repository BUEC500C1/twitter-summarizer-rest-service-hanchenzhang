# REST-API Service-hanchenzhang: Integration of Video Creation Module

This is the EC500 HW5 REST-API from Hanchen Zhang: Twitter Summarizer Rest-service

# Assignment Announcement:
Main Exercise:  Integrate hw4 module to become a RESTFUL system, Deploy your system to free AWS services

# Introduction to Hanchen's video generation package.
The file app.py is the main function file that construct a basic flask-Restful web system with two front end pages:

`./templates/main.html` is the root page which allow user to put the target twitter username to create the video
`./templates/result.html` is the reuslt page after the video successfully created.

The `./videos` directory contains a file "output_@BU_Tweets.mp4" is shown as example.

# The Queue:
The file videoqueue.py create a queue that works for a "brain" that control the running of functions in the videoHW4.py.
The size of the queue generated from the videoqueue.py is equal to the number of input user accounts.

This function set an arbitary number which is the maximum number that the threading could process. Currently this number is set to 2, Therefore if the threading already runs 2 functions. The new threads will put back to the queue and wait when there are extra space.

![](./running.png)

# Instruction of Running the package:
1. git clone the project
2. Apply twitter developer api key and substitute the key in the key file from the root directory
3. Go the directory and create the vitrtual environment, since python2 is no more useful, here is the python3 command:
```
$ python3 -m venv venv
$ . venv/bin/activate
```
4. pip install required dependency shown in the requirement.txt
5. running the flask app by following command:
```
$ export FLASK_APP=app.py
$ flask run
```
6. open an explorer and copy the link to run.
