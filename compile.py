import os

from gears.environment import Environment
from gears.finders import FileSystemFinder
from gears_stylus import StylusCompiler


env = Environment('static')
env.register_defaults()
env.finders.register(FileSystemFinder(directories=[os.path.abspath('assets')]))
env.compilers.register('.styl', StylusCompiler.as_handler())


if __name__ == '__main__':
    env.save()
