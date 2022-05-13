from flask_script import Manager
from apps.app import create_app

if __name__ == '__main__':
    app=create_app()
    manager=Manager(app)

    manager.run()
