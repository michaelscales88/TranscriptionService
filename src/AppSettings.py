from configobj import ConfigObj
from os.path import join, dirname
from functools import reduce


class AppSettings(ConfigObj):

    def __init__(self, app=None, settings_file=None):
        if app or settings_file:
            self._my_app = app
            super().__init__(settings_file if settings_file else self.settings_file,
                             create_empty=True)
        else:
            raise SystemError('No application for AppSettings')

    @property
    def settings_file(self):
        return join(self.settings_directory, '{f_name}.ini'.format(f_name=self._my_app.__class__.__name__))

    @property
    def settings_directory(self):
        return join(dirname(dirname(__file__)), 'settings')

    def setting(self, *keys):
        try:
            return reduce(dict.__getitem__, keys, self)
        except (KeyError, TypeError):
            print('Could not find settings: {settings}'.format(settings=keys))

    def settings_w_formatting(self):
        # this should return a list of settings with formatting if applicable
        # E.g. req_src_files with {} filled
        pass

