# Dashletter(Unmaintained)
This project was made for a friend. A basic django application including login for the users and maintaining a user database.

## How to use?
I will be explaining you how to use it locally on your machine(that too linux) so if you are a windows user than good luck to you cuz the below command may or may not work for you.
1. Open the Magic black window aka terminal. You will need python3 for this.
2. Make a python virtual enviroment `python3 -m venv <name-of-virtual-env>` if you got an error that venv not install then [install]  (https://docs.python.org/3/tutorial/venv.html) it.
3. Then fork and clone the repo if you don't have it already.
4. Navigate to the repo and install all the dependencies. Make sure you activate your venv. Install dependencies using `python -r requirements.txt`
5. You are done now run the server using `python manage.py runserver`.
6. If you want to use reset password feature you need to set your email and app password of gmail to your enviroment variables like `export EMAIL_USER=<your-email>` and `export EMAIL_PASS=<your-pass>` into the .bash_profile
7. for admin username is root and password is 123 in case you dont want to create a new superuser
