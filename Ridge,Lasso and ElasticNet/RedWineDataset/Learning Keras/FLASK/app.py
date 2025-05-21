from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'hello {name}'
    return render_template('form.html')

### Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "pass"    
    else:
        res = "fail"    
    return render_template('success.html',result=res)



if __name__ == '__main__':
    app.run(debug=True)