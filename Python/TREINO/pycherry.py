import cherrypy

class Pagina_One():
    def index(self):
        return "Pagina Um !"
    
    index.exposed=True
    
class Hello_World(object):
    onepage = Pagina_One()
    
    def index(self):
        return"""<form action="doLogin" method="post">
        <p>NOME</p>
        <input type="text" name="username" value=""
        size="15" maxlenght="40"/>
        <p>Senha</p>
        <input type="password" name="password" value=""
        size="10" maxlenght="40"/>
        <p><input type ="Submit" value="Login"/></p>
        <p><input type ="reset" value="Clear"/></p>
        </form>"""
        
    index.exposed=True
    def foo(self):
        return "tolo"
    
    foo.exposed = True
    
    
    def doLogin(self,username=None,password=None):
        return'Ola'+username+''+password
    doLogin.exposed = True

cherrypy.quickstart(Hello_World())    
        
    