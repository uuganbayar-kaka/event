### Installation

**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First

```
$  pip install virtualenv
```

Create Virtual Environment

For Windows

```
 python -m venv venv
```

For Mac

```
python3 -m venv venv
```

Activate Virtual Environment

For Windows

```
source venv/scripts/activate
```

For Mac

```
source venv/bin/activate
```

**3. Install Requirements from 'requirements.txt'**

```
pip install -r requirements.txt
```

**4. make database migrations**

```python
python manage.py migrate
```

**5. Login Credentials**

Create Super User (HOD)

```
$  python manage.py createsuperuser
```

Then Add Email, Username and Password

**6. Now Run Server**

Command for Windows:

```python
$ python manage.py runserver
```

Command for Mac:

```python
$ python3 manage.py runserver
```
