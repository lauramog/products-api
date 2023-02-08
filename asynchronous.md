# Asynchronous in Django

Before giving an example about asynchronous in django, is important to mention that channels replaces Django's 
request/response cycle with messages that are sent across channels. Allowing clients and servers communicate 
and exchange information across channels layers.


# Example 

 We are building en e-learning platform which contains several courses, each course has many students enrolled, 
 we want to provide a chat server for each course.
 For this functionality real-time communication between the server and the client is required. first the client 
 must be able to connect at the chat, receiving and sending data at any time. For this task asynchronous is
 required. 
 
#### Bibliography:
Django 3 by example (2020), Antonio Melé. 

