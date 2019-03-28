
# Environment preparing

This application uses python 3.6 and Flask.

Create and activate virtualenv:
PS.: If you're not on Ubuntu, you must run the Docker container (TO-DO)
```
virtualenv env
source env/bin/activate
```
To install requirements, run:

```pip3 install -r requirements.txt```

# Run the app

```
chmod a+x app.py
./app.py
```

# Access via browser

```http://127.0.0.1:5000/```

# Tests

Tests (unit and integrated):
``` python -m unittest discover```

# Next steps...

- TO-DO