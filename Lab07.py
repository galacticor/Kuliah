from flask import Flask, render_template_string

app = Flask(__name__)

def recrev(st):
	if(len(st)==0):
		return ""
	a = st[-1]
	st = st[:-1]
	return a+recrev(st)

@app.route("/<word>")
def main(word='fasilkom'):
	page = '''
<html>
	<head> <title>Lab 07 Page</title> <head>
	<body>
		<h1 style="color: red">Lab 07 Dasar-Dasar Pemorgraman 1</h1>
		<p>The reverse of <i style="color: green">{{kata}}</i> is
		<b style="color: blue">{{kebalik}}</b>.
	</body>
</html>
'''
	return render_template_string(page,kata=word,kebalik=recrev(word))
    
if __name__ == "__main__":
    app.run(debug=True)
