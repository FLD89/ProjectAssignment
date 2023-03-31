 ________  ________  ________        ___  _______   ________ _________                                    
|\   __  \|\   __  \|\   __  \      |\  \|\  ___ \ |\   ____\\___   ___\                                  
\ \  \|\  \ \  \|\  \ \  \|\  \     \ \  \ \   __/|\ \  \___\|___ \  \_|                                  
 \ \   ____\ \   _  _\ \  \\\  \  __ \ \  \ \  \_|/_\ \  \       \ \  \                                   
  \ \  \___|\ \  \\  \\ \  \\\  \|\  \\_\  \ \  \_|\ \ \  \____   \ \  \                                  
   \ \__\    \ \__\\ _\\ \_______\ \________\ \_______\ \_______\  \ \__\                                 
    \|__|     \|__|\|__|\|_______|\|________|\|_______|\|_______|   \|__|                                 
                                                                                                          
                                                                                                          
                                                                                                          
 ________  ________   ________  ___  ________  ________   _____ ______   _______   ________   _________   
|\   __  \|\   ____\ |\   ____\|\  \|\   ____\|\   ___  \|\   _ \  _   \|\  ___ \ |\   ___  \|\___   ___\ 
\ \  \|\  \ \  \___|_\ \  \___|\ \  \ \  \___|\ \  \\ \  \ \  \\\__\ \  \ \   __/|\ \  \\ \  \|___ \  \_| 
 \ \   __  \ \_____  \\ \_____  \ \  \ \  \  __\ \  \\ \  \ \  \\|__| \  \ \  \_|/_\ \  \\ \  \   \ \  \  
  \ \  \ \  \|____|\  \\|____|\  \ \  \ \  \|\  \ \  \\ \  \ \  \    \ \  \ \  \_|\ \ \  \\ \  \   \ \  \ 
   \ \__\ \__\____\_\  \ ____\_\  \ \__\ \_______\ \__\\ \__\ \__\    \ \__\ \_______\ \__\\ \__\   \ \__\
    \|__|\|__|\_________\\_________\|__|\|_______|\|__| \|__|\|__|     \|__|\|_______|\|__| \|__|    \|__|
             \|_________\|_________|                                                                      
                                                                                                          
                                                                                                          
PROJECT ASSIGNMENT
__________________



DEPENDENCIES:

Please ensure that you have the following installed:

- Django 4.1.5
- Python 3.11.1
- SQLite 3.40.1



RUN ON LOCAL SERVER:

If you wish to run the application on a local server, please open up the relevant directory in PowerShell (if you are using a Windows OS)and enter, for example:

"cd C:\User\USERNAME\Desktop\ProjectAssignment\main"

This will navigate to the "main" subfolder of the supplied "ProjectAssignment" directory. Next, enter the following command:

"python manage.py runserver"

NB: This may differ if not using a Windows OS
You then will need to open the following URL in a web browser, shown in PowerShell if it launches successfully:

"http://127.0.0.1:8000/"



ADMIN CREDENTIALS AND ACCESS:

These will be required for admin users to delete records from the database. With the application running on a local server, open the following URL:

"http://127.0.0.1:8000/admin"

Admin username: Admin
Admin password: Assignment

This is Django's pre-supplied administration system, and will allow you to select Project engineer lookups / Projects / Software engineers / Software trainings

Here, you will be able to delete records in a way that regular users cannot.

You can also create new admin users with the following command:

"python manage.py createsuperuser"

NB: you will need to navigate to the correct directory first, for example:
cd Users\SomeUsername\Desktop\ProjectAssignment\main



DATABASE:

If, for some reason, you wish to undo all changes and restore the database to the original pre-populated test data, first delete the following file:

"ProjectAssignment\main\db"

And then run the following commands which will create a new, blank database:

"python manage.py makemigrations"
"python manage.py migrate"

For the next stage, you will need DB Browser for SQLite (which can be downloaded from https://sqlitebrowser.org/) or similar

Within DB Browser, execute the SQL script from the following file:

"ProjectAssignment\SQLite DB Browser - Populate Test Data"



AUTOMATED TESTS:

Tests are saved in:
ProjectAssignment\main\tests

These can be run by entering the following command in Powershell, after navigating to the correct directory:
"python manage.py test"
