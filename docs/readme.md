**

## SQLAlchemy

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper (ORM) that gives application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

[# SQLAlchemy and Django](https://engineering.betterworks.com/2015/09/03/sqlalchemy-and-django/)

[# SQLAlchemy](https://www.fullstackpython.com/sqlalchemy.html)


**

## Model-View-Controller



Model View Controller is the most commonly used design pattern. Developers find it easy to implement this design pattern.
![MVC](https://www.tutorialsteacher.com/Content/images/mvc/mvc-architecture.png)

**Model**
It consists of pure application logic, which interacts with the database. It includes all the information to represent data to the end user.

**Controller**
 It acts as an intermediary between view and model. It listens to the events triggered by view and queries model for the same.
 
**View** 
It displays all the records fetched within the model. View never interacts with model; controller does this work (communicating with model and view).
![Request/Response in MVC Architecture](https://www.tutorialsteacher.com/Content/images/mvc/request-handling-in-mvc.png)


[# MVC](https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/)




## Django MTV:



Django follows MVC pattern very closely but it uses slightly different terminology. Django is essentially an MTV (Model-Template-View) framework. Django uses the term Templates for Views and Views for Controller. In other words, in Django views are called templates and controllers are called views. Hence our HTML code will be in templates and Python code will be in views and models. Django’s architecture consists of three major parts:

Part 1 is a set of tools that make working with data and databases much easier Part 2 is a plain-text templating system that can be used by non-programmers; and Part 3 is a framework that handles communication between the user and the database and automates many of the painful parts of managing a complex website
![MVT](https://www.tutorialspoint.com/django/images/django_mvc_mvt_pattern.jpg)

The following diagram illustrates how each of the components of the MVT pattern interacts with each other to serve a user request .
The developer provides the Model, the view and the template then just maps it to a URL and Django does the magic to serve it to the user.
[MVC-Django](https://overiq.com/django-1-10/mvc-pattern-and-django/)
[MVT](https://www.tutorialspoint.com/django/django_overview.htm)




