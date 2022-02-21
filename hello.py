from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

#@app.route('/')
#def home():
   #return 'Hello World'
   
@app.route('/hello')   
def hello_world():
   return 'hello world'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name
   
@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python' 

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))   
      
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

      
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('name')
      return redirect(url_for('success',name = user))
      
#@app.route('/')
#def index():
   #return '<html><body><h1>Hello World</h1></body></html>'
   
#@app.route('/')
#def index():
   #return render_template('hello.html')
   
@app.route('/hello/<user>')
def hello_name1(user):
   return render_template('hello.html', name = user)

@app.route('/hello/<int:score>')
def hello_name2(score):
   return render_template('hello1.html', marks = score)

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)
   
@app.route("/")
def index():
   return render_template("index.html")

  
   
if __name__ == '__main__':
   app.run(debug = True)
   
