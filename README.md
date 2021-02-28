# Pur Beurre

Pur Beurre is a web application developed with [Django](https://www.djangoproject.com/) framework.  
By using this program, you will be able to search for a substitute for your every day aliments. You can create an 
account to save your favorites aliments.

### Installation 

* If you're on MacOS, you can install Pipenv easily with Homebrew:

    `$ brew install pipenv`

Otherwise, refer to [Pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv) documentation for instructions.

* Once you installed pipenv, clone project repository and install from Pipfile:

    `$ pipenv install`


* Next, activate the Pipenv shell:

    `$ pipenv shell`
    
    This will spawn a new shell subprocess, which can be deactivated by using `exit`.  



* Read the [Django documentation](https://docs.djangoproject.com/en/3.1/) to initiate your Django project

* To initiate the Postgresql database with [OpenFoodFacts](https://world.openfoodfacts.org/) data, run `python manage.py init_db add_data`


### Usage

_From localhost:_

* From project source directory, run `python manage.py runserver`

* Go to your browser and enter your localhost url

_Deploying on Heroku server:_

* Create an account on [Heroku](https://id.heroku.com/login) and read the [documentation](https://devcenter.heroku.com/articles/getting-started-with-python)  
You can help with several tutorials on how to deploy a Django project on Heroku, like this one from MDN : 
  [Django Deployment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)

### **You are now ready to find your first substitute !**