from flask import Flask, render_template, request

app = Flask(__name__,template_folder='template')

#index
@app.route('/')
def home(): 
    return render_template ("home.html")

#home (juan esteban)
@app.route('/registro')
def login():
    return render_template ("registro.html")
#el login (julian)


@app.route('/tc')
def tc():
    return render_template ("termycond.html")
#terminos y condiciones (juan pablo)

@app.route('/perfilcliente')
def perfilcliente():
    return render_template ("perfilcliente.html")
# (harold)

if __name__ == "__main__":
    app.run(debug=True)