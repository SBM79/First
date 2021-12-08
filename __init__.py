from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello world():
    return 'hello,world'
    
if __name__=="__main__":
	app.run(debug=True)