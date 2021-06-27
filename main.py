from app import create_app
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin
from flask_script import Manager
import config
import unittest
import coverage

app = create_app()
cors = CORS(app)
jwt = JWTManager(app)
manager = Manager(app)

@manager.command
def test():
    cov = coverage.Coverage()
    cov.start()
    
    tests = unittest.TestLoader().discover('app', pattern='*.py')
    unittest.TextTestRunner(verbosity=1).run(tests)
    cov.stop()
    cov.save()
    cov.html_report()

@manager.command
def runserver():
    app.run(host='0.0.0.0', port=str(config.Config.PORT), debug=True)
    
if __name__ == '__main__':
    manager.run()
