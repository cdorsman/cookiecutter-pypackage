from os.path import dirname, join, abspath 
from argparse import ArgumentParser


class Parser(object):
    def __init__(self):
        self.app_root = dirname(dirname(
                abspath(__file__)))
        self.app_name = "template"
        self.version = "0.1"
        self.default_conf = join(self.app_root,
          'conf/{}.conf').format(self.app_name)
        self.default_logconf = join(self.app_root,
          'conf/logging.ini')
        self.default_logfile = join(self.app_root,
          'logs/{}.log').format(self.app_name)
        self.config_file = ""

        for key, value in vars(self.create_parser()).items():
            if key == 'config_file':
                self.config_file = value

    def create_parser(self):
        """
        This ArgsParse function is where you can add
        all your needed options
        """
        parser = ArgumentParser()

        # version option
        parser.add_argument(
           '--version',
            action='version',
            version=self.app_name + " (version {version})"
            .format(version=self.version)
        )

        # config option
        parser.add_argument(
            '-c',
            '--config',
            dest='config_file',
            default=self.default_conf,
            help='Location of the configuration file'
        )
        return parser.parse_args()
