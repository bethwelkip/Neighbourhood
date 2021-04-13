## Neighbourhood

## Author
 [Bethwel Kiplimo](https://github.com/bethwelkip)


## Link to live site
https://neighbourhuud.herokuapp.com/ 

## Link to Figma


## Description
This is a website that lets you explore the businesses  and amenities in your neighbourhood. Each neighbourhood has an admin and a neighbourhood member can make posts and view posts made by other users in the neighbourhood. The user can also view the businesses in their locality besides creating their own profile.

# Live Site 
If you are only interested in viewing the deployed web app, click on the link below:
**[Neighbourhuud](https://neighbourhuud.herokuapp.com/ )**


## Installation Requirements
  If you would like to look at or toy around further with the source code, follow the following steps:
  * Clone this repository and navigate to the folder: git clone https://github.com/bethwelkip/neighbourhood.git 

  Once in the folder, open your terminal and run the following commands to set up your working environment:-
  * sudo pip install python3.7
  * python3.7 -m venv virtual
  * conda deactivate -- deactivates conda if one is running
  * source virtual/bin/activate
  * pip install -r requirements.txt (installs all necessary dependencies)
  * configure your database by navigation to settings.py and find the database settings and then rename the "Name" and "Password" and "Host" to those of your local machine. 
   The application is now ready to be served.
   Run the following in your terminal  to serve the application
* python manage.py runserver

 
## User Stories
  * A user can create his/her/their profile
  * A user can create posts and see posts made by themselves and others
  * A user can switch to a different neighbourhood when they want to move
  * An admin can kick people out of their neighbourhood, add contacts to emergency services eg hospitals etc

## Technologies Used
  * Python3.7
  * HTML5
  * Bootstrap4
  * Django
  * PostgreSQL
  * Heroku

## Known Bugs
No known bugs so far but if any is found, please let me know at bkiplimo@princeton.edu

## LICENSE
Licenced under [MIT LICENSE](LICENSE)
