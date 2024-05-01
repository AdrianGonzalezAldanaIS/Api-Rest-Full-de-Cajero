from flask import Flask
from config import config

# Rutas
from routes import PagosServiciosTelefonoRoutes, TarjetasRoutes

app = Flask(__name__)
def page_not_found(error):
    return "<h1> Pagina no encontrada</h1>", 404
  
if __name__ == '__main__':
    
    app.config.from_object(config['development'])
    # Blueprints
    app.register_blueprint(TarjetasRoutes.main, url_prefix='/api/tarjetas')
    app.register_blueprint(PagosServiciosTelefonoRoutes.main, url_prefix='/pago')
    #app.add_url_rule()
    app.register_error_handler(404, page_not_found)
    app.run()
