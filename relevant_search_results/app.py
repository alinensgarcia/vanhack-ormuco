#!venv/bin/python3.6
from flask import Flask, jsonify, make_response, render_template
from results_extractor import ResultsExtractor

# Referencia
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This API returns the most relevant content from top 5 ' \
        'Google search results about some topic.'

@app.route('/relevant_results/<search_topic>', methods=['GET'])
def get_relevant_results(search_topic):
    if len(search_topic) == 0:
        abort(404)

    if search_topic != 'keystone - Circular reference found role inference':
        return 'Search topic not supported yet.'
    
    relevant_contents = ResultsExtractor(search_topic).get_relevant_contents()
    
    return render_template('template.html', relevant_contents=relevant_contents)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)