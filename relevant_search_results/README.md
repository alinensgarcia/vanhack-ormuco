# Project Overview 
Description of components:
- `results_extractor.py`: In this package, class `ResultsExtractor` is responsible for control the flow of the main functionality of the API.
- `crawler.py`: In this package there are 2 classes: `GoogleCrawler` which is responsible for crawling Google results page and `SiteCrawler` which is responsible for crawl and extract source content from top 5 pages.
- `content_analyzer.py`: In this package, class `ResultsExtractor` is responsible for analyze the pages source codes and extract the most relevants contents. For now, only a naive approach is implemented. In an eventual future, more complex approaches could be implemented, such as Machine Learning algorithms, for example Natural Language Processing, in order to extract the most relevant contents.
**PS:** Using NLP in this case is not trivial because the subject of this Case is very specific, it refers to a software development topic. We could use TD-IDF technique to identify the most relevant paragraphs or phrases, and when appropriate, select the code snippets releated to. In order to build an generical content extractor, the algorithm should be even more robust and complex, being capable of identifying the subject of the search and dealing with it in appropriate manner.
- `app.py`: The API, a Flask application.

# Environment preparing
This application uses python 3.6 and Flask.
Create and activate virtualenv:
```
virtualenv python=python3.6 venv
source venv/bin/activate
```
To install requirements, run:
```
pip install -r requirements.txt
```

# Run the app

```
chmod a+x app.py
./app.py
```

# Using the API

```
http://127.0.0.1:5000/relevant_results/keystone - Circular reference found role inference
```
**PS:** For now, only the Case example search topic ("keystone - Circular reference found role inference") is supported.

# Automated Tests

```
python -m unittest discover tests -p "*_test.py"
```

# Improvements to do

  - Topic generalization. Not an easy task because the type of results vary a lot accordingly to theme. The search phrase of this example is about software development, so the results were mainly code snippets and forum messages. More details were discussed on `Project Overview` section.
  - Implement logging.
  - Use Dockerfile instead virtualenv, because it'll run no matter the OS.
  - Improve Docs. (Unfortunately, due to a time constraint, other things were prioritized).
