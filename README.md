# Django-Management

To run this Project following bellow

### 1. Clone this repo
```git clone https://github.com/mahiuddin-dev/Django-Management.git```

### 2. Make a virtualenv
after clone this project. Go to project directory. For command line type `cd .\Django-Management`
Then create a virtualenv calls (venv,env) as you wish.
`virtualenv venv` run this command for create a virtualenv. After active venv.

For windows run `cd .\venv\Scripts\activate`

On linux run `source/venv/bin/activate`

### 3. Install all Requirements Packages
Run ```pip install -r requirements.txt```

### 4. Run makemigrations, migrate and then group_permissions command

```
python manage.py makemigrations
python manage.py migrate
python manage.py group_permissions
```
### 5. Change user Group
Create a superuser ```python manage.py createsuperuser```

If a user sign up default user role is just view project. If you want to change user role got to http://127.0.0.1:8000/admin/ and login admin user. Then go to User section and choose  a user and clink on username. After that you can see group box. Select group name and add. Save those change.