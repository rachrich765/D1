from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


#Task 2 : Dynamic URLS
    #edit the view function to display 'Welcome to <course_name>' on localhost:5000/course/<course>
@app.route('/course/<course_name>')
def courseView(course_name):
    return "Welcome to " + course_name


#Task 3.1 Basic HTML Form
    #Set the method and action of the HTML form, such that form data is sent to /result using POST method
    #The form should have a text field in which you can enter an ingredient (milk, eggs, etc)
@app.route('/form')
def formView():
    html_form = '''
    <html>
    <body>
    <form action = "/result" method = "POST">
        <label for= "i"> Enter an ingredient: </label>
        <br>
        <input type = "text" name = "ingredient" id = "i"></input>
        <input type = "submit" name = "Submit">
    </form>
    </body>
    </html>
    '''
    return html_form

#Task 3.2 : Processing Form Data
@app.route('/result', methods = ['GET', 'POST'])
def resultView():
    # Make an API request to Recipe API for the ingredient entered in the form and display the recipe results
    #Step 1 : Receive the ingredient from the form if request type is POST
    if request.method == "POST":
        ingredient = request.form.get("ingredient","Did not get anything")
        print(ingredient)
    #Step 2 : Create paramaters JSON with the ingredient received in step 1 in the form required by http://www.recipepuppy.com/about/api/
        params = {}
        params['i'] = ingredient
        base_url = 'http://www.recipepuppy.com/api/'
    #Step 3 : Make an API request to Recipe API and parameters in Step 2
        response = requests.get(base_url, params = params)
    #Step 4 : Parse the response from API request in JSON
        response_json = json.loads(response.text)
    #Step 5 : Display the response in browser (remember : HTML takes only strings)
    response_str = str(response_json)
    return response_str


if __name__ == '__main__':
    app.run(debug=True)
