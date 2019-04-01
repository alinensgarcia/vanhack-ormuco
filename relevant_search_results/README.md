- Project Overview
  - Description
  - App, Extractor, Crawler, Content Analyzer (desenhar um diagrama simples)
    - Explicar com mais detalhes o que cada caixinha faz.
  - Modelagem de entidades visou desacoplamento e organização lógica, facilitando a manutenção e evolução do código.


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


```python -m unittest discover tests -p "*_test.py"```

# Next steps...
Functionalities:
    - Topic generalization. Not an easy task because the type of results vary a lot accordingly to theme. The search phrase of this example is about software development, so the results were mainly code snippets and forum messages.

    - Dockerfile