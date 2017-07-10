#!venv/bin/python3

from flask_script import Manager
from flask_script import Server, Manager
from flask_migrate import MigrateCommand
from app import create_app
import os

manager = Manager(create_app)
manager.add_option('-c', '--config', dest='config', required=False)
manager.add_command('runserver', Server(port=os.environ.get('PORT', 5000)))
manager.add_command('db', MigrateCommand)
# manager.add_command('test', PytestCommand)

if __name__ == '__main__':
    manager.run()
