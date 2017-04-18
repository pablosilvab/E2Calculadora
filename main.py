import webapp2
from google.appengine.api import users

class MainPage(webapp2.RequestHandler):
    def get(self):
    	user = users.get_current_user()
    	if user:
    		nickname = user.nickname()
    		logout_url = users.create_logout_url('/')
    		greeting = 'Bienvenido, {}! (<a href="{}">Sing Out</a>)'.format(
    			nickname, logout_url)

    		self.redirect("/calculadora")

    	else:
    		login_url = users.create_login_url('/')
    		greeting = '<a href="{}">Inicia sesion</a>'.format(login_url)

    	self.response.write(
    		'<html><body>{}</body></html>'.format(greeting))

class Calculadora(webapp2.RequestHandler):
    def get(self):        
    	user = users.get_current_user()
    	if user:
    		nickname = user.nickname()
    		logout_url = users.create_logout_url('/')
    		greeting = 'Bienvenido, {}! (<a href="{}">Sing Out</a>)'.format(
    			nickname, logout_url)


    	else:
    		login_url = users.create_login_url('/')
    		greeting = '<a href="{}">Inicia sesion</a>'.format(login_url)

    	self.response.write(
    		'<html><body>{}</body></html>'.format(greeting))
        self.response.out.write('''
            <html>
                <body>
                   <form method="POST">
                     <p>Calculadora con Python </p>
                     <label>Primer numero: </label>
                     <input type="text" name="numero1" />
                     <br/>
                     <label>Segundo numero: </label>
                     <input type:"text" name="numero2" />
                     <br/>
                     <label>Operacion: </label>
                     <select id="operacion" name="operacion">
                     	<option value="" selected="selected">- Selecciona operacion -</option>
                     	<option value="1">Adicion</option>
                     	<option value="2">Sustraccion</option>
                     	<option value="3">Multiplicacion</option>
                     	<option value="4">Division</option>
					 </select>
					 <br/>
					 <br/>
                     <input type="submit" />
                   </form>
                 </body>
            </html>
        ''')
    def post(self):
        numero1 = int(self.request.get("numero1"))
        numero2 = int(self.request.get("numero2"))

        operacion = self.request.get("operacion")
        if (operacion=="1"):
	        resultado = numero1+numero2
        if (operacion=="2"):
	        resultado = numero1-numero2
        if (operacion=="3"):
	        resultado = numero1*numero2
        if (operacion=="4"):
        	if (numero2 == 0):
        		self.response.write('No existe division por cero. Intenta con otro numero.');
        		resultado = "No existe"
        	else :
        		resultado = numero1/numero2

        self.response.write('El resultado de la operacion es: '+ str(resultado));

        user = users.get_current_user()
    	if user:
    		nickname = user.nickname()
    		logout_url = users.create_logout_url('/')
    		greeting = '\nBienvenido, {}! (<a href="{}">Sing Out</a>)'.format(
    			nickname, logout_url)


    	else:
    		login_url = users.create_login_url('/')
    		greeting = '<a href="{}">Inicia sesion</a>'.format(login_url)

    	self.response.write(
    		'<html><body>{}</body></html>'.format(greeting))

        self.response.out.write('''
            <html>
                <body>
                   <form method="POST">
                     <p>Calculadora con Python </p>
                     <label>Primer numero: </label>
                     <input type="text" name="numero1" />
                     <br/>
                     <label>Segundo numero: </label>
                     <input type:"text" name="numero2" />
                     <br/>
                     <label>Operacion: </label>
                     <select id="operacion" name="operacion">
                     	<option value="" selected="selected">- Selecciona operacion -</option>
                     	<option value="1">Adicion</option>
                     	<option value="2">Sustraccion</option>
                     	<option value="3">Multiplicacion</option>
                     	<option value="4">Division</option>
					 </select>
					 <br/>
					 <br/>
                     <input type="submit" />
                     <br/>
                   </form>
                 </body>
            </html>
        ''')




app = webapp2.WSGIApplication([
    ('/',MainPage),
    ('/calculadora',Calculadora),
], debug=True)