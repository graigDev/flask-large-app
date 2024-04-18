from flask import Flask, render_template
from config import Config
from src.extensions import db, migrate, mail


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    #   Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    #   Register blueprints here
    from src.app import bp as src_bp
    app.register_blueprint(src_bp)

    from src.features.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    #   App default routes
    @app.route('/test')
    def test_page():
        return "Testing the Flask application pattern."

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

    #   App cli command to run tests
    @app.cli.command()
    def test():
        """Run the unit tests."""
        import unittest
        tests = unittest.TestLoader().discover('tests')
        unittest.TextTestRunner(verbosity=2).run(tests)

    return app
