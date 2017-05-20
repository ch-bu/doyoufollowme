# DoYouFollowMe

I am buildling a website that allows teachers to see how their students understand the lecture in real time. Students are able to indicate if they are lost and are able to add short questions about the current topic. Teachers will see the amount of student that are lost on the dashboard. By seeing this data in real time, teachers are able to adapt their lecture to specific difficult issues. 

# How to run locally

Clone the repository to your machine. You should have [Docker](https://docs.docker.com/engine/installation/) and [Docker Compose](https://docs.docker.com/compose/install/) installed. Make sure that you have ownership of all files:

```
sudo chown -R $USER:$USER .
```

Afterwards, fire up the application:

```
docker-compose up
```

Your application should be running on `localhost:8080`. 

In order to stop the application run

```
docker-compose stop
```
 