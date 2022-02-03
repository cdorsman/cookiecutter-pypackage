from os.path import exists, isfile
from sys import exit
from logging import getLogger
from configparser import RawConfigParser, ParsingError, NoOptionError, NoSectionError


class config:
    """
    Class for reading global configuration file

    methods:
    - Read      : Reading for configuration file
    - Getoption : Getting and setting options.
    """

    def __init__(self, configFile):
        self.log = getLogger(__name__)
        self.cfg = RawConfigParser()
        self.conf = configFile

        if self.Read() is False:
            print('Cannot read configuration file')
            exit(1)

        # Howto add new option:
        # There are four arguments that needs attention when
        # implementing a new option:
        # - section
        # - option name
        # - content of var
        # - default content var
        # - Required option

        # Example option for main with default value which isn't required
        # self.main_first_arg = self.Getoption(
        #                    'main',
        #                    'option1',
        #                    None,
        #                    '',
        #                    False)

        # Example option for main with default value which is required
        self.main_sec_opt = self.Getoption(
            'main',
            'option2',
            None,
            'argument1',
            True
        )

    def Read(self):
        """Open config file and try to parse"""
        try:
            conf = self.conf
            if conf.endswith('.conf') is True:
                if exists(self.conf) is True and\
                        isfile(conf) is True:
                    self.cfg.read(conf)
            else:
                self.log.error("Cannot open file %s", conf, exc_info=True)
                return False
        except IOError:
            self.log.debug("Cannot open file %s", conf, exc_info=True)
            return False
        except ParsingError as parse_err:
            self.log.debug("Parsing error %s", parse_err, exc_info=True)
            return False
        return True

    def Getoption(self, section, option, var, default, required):
        """
        Get from defined sections all the defined options
        if option is not defined set default value.
        """
        try:
            try:
                var = self.cfg.get(section, option)
                # If option is not set then the default setting
                # will be replace the empty variable
                if not var and not default and not required:
                    self.log.warn('Skipping non required option [%s] \
in section [%s] defined without default', option, section)
                elif not var and default and required:
                    var = self.cfg.set(section, option, default)
                    self.log.debug('Option [%s] in section [%s]\
                                to: %s (default)', option, section, default)
                elif not var and not default and required:
                    self.log.error('Required option [%s] in section [%s] \
                                is undefined and \
                                missing defined default', option, section)
                else:
                    self.log.debug('Setting option [%s] \
in section [%s] to: %s', option, section, var)
            except NoOptionError:
                self.log.error('Failed to find option [%s]',
                               option, exc_info=True)
        except NoSectionError:
            self.log.error('Failed to find section [%s]',
                           section, exc_info=True)
        return var
