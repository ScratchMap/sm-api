#!venv/bin/python3

from flask_script import Manager
from flask_migrate import MigrateCommand
from app import create_app
from flask import current_app

manager = Manager(create_app)
manager.add_option('-c', '--config', dest='config', required=False)
manager.add_command('db', MigrateCommand)
# manager.add_command('test', PytestCommand)

if __name__ == '__main__':
    print(current_app)
    manager.run()
