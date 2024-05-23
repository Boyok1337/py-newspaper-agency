![Logo](https://arc.york.ac.uk/wp-content/uploads/2020/08/IJESPORTS-logo.png)


# Newspaper

This project was created specifically for a newspaper company. It makes it easy to add posts. Editing and deleting won't be a problem either. The site also has topics for quick filtering of news.
### ⚡ Live DEMO: [NewspaperAgency](https://newspaper-agency-ihdo.onrender.com/)
- You can use following superuser (or create another one by yourself):
    - Login: ```qwe```
    - Password: ```qwe```


## 👩‍💻 _Installation & Run_
### 🧠 Set up the environment 


 On Windows:
```python
python -m venv venv 
venv\Scripts\activate
 ```

 On UNIX or macOS:
```python
python3 -m venv venv 
source venv/bin/activate
 ```

### 👯 Install requirements 
```python
pip install -r requirements.txt
```


### 🗃️ Database setup

```python
python manage.py migrate
```

### 📫 Install database fixture
```python
python manage.py loaddata my_fixture.json
```
_You can upload ready-made data to see what the project looks like in its entirety and in action._
_You can also delete this file if you are not going to use the already prepared data_


### 👥 Create a superuser (optional)
If you want to perform all available features, create a superuser account:
```python
python manage.py createsuperuser
```

### 📝 Set enviroment variable
- Copy and rename the **.env.sample** file to **.env** 
- Open the .env file and edit the environment variables 
- Save the .env file securely 
- Add the .env file to .gitignore 

### 🚀 Run the project
```python
python manage.py runserver
```
### 😄 Go to site [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## 📰 Usage
After running the newspaper site, you can perform CRUD (Create, Read, Update, Delete) operations on the news.
- **Create:** Create a new piece of news by providing a title, text, and an image (optional).
- **Read:** View a list of all news or a selected news item.
- **Update:** Update an existing news item by changing the title, text, or image.
- **Delete:** Delete an existing news item.


## 🛡️ Testing
You can run tests for the Django project using the following command:
```python
python manage.py test
```


## 📝 Contributing
If you want to contribute to the project, please follow these steps:
    1. Fork the repository.
    2. Create a new branch for your feature or bug fix.
    3. Make the necessary changes and commit them.
    4. Submit a pull request.

## 🔗 Links
Additional links:
- Django documentation: https://docs.djangoproject.com/en/3.2/
- Django tutorial: https://docs.djangoproject.com/en/3.2/intro/tutorial01/
- SQLite documentation: https://www.sqlite.org/docs.html

## 😋 _Enjoy it!_