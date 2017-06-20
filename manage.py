#!venv/bin/python3

from flask_script import Manager
from app import create_app

manager = Manager(create_app)
manager.add_option('-c', '--config', dest='config', required=False)
# manager.add_command('db', MigrateCommand)
# manager.add_command('test', PytestCommand)

if __name__ == '__main__':
    manager.run()
