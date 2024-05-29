from flask import Flask
from config import config
from database.postgres_db import PostgresDB

# Rutas
from routes import PagosServiciosTelefonoRoutes, TarjetasRoutes


def page_not_found(error):
    return "<h1> Pagina no encontrada</h1>", 404
def create_app():
    app = Flask(__name__)
    app.register_blueprint(TarjetasRoutes.main, url_prefix='/api/tarjetas')
    app.register_blueprint(PagosServiciosTelefonoRoutes.main, url_prefix='/pago')
    return app
    
app = create_app()
pgdb = PostgresDB()
pgdb.init_app(app)

if __name__ == '__main__':
    
    app.config.from_object(config['development'])
    # Blueprints
    #app.register_blueprint(TarjetasRoutes.main, url_prefix='/api/tarjetas')
    #app.register_blueprint(PagosServiciosTelefonoRoutes.main, url_prefix='/pago')
    #app.add_url_rule()
    app.register_error_handler(404, page_not_found)
    app.run(port = 4000)
