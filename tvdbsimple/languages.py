# -*- coding: utf-8 -*-

"""
This module implements the Language functionality of TheTVDb API.
Allows to retrieve the languages list and info.

See [Languages API section](https://api.thetvdb.com/swagger#!/Languages)
"""
from .base import TVDB


class Languages(TVDB):
    """
    Languages class to retrieve the languages list and info.
    """
    _BASE_PATH = 'languages'
    _URLS = {
        'all': '',
        'language': '/{lid}'
    }
    LANGUAGES = {}
    _ALL_PARSED = False

    def __init__(self):
        super(Languages, self).__init__()
        self.all()

    def all(self):
        """
        Get the full languages list and set it to all attribute.

        Returns a list of languages with their info.
        """
        if not self._ALL_PARSED:
            self._get_languages()

        return self.LANGUAGES.values()

    def _get_languages(self):
        path = self._get_path('all')

        response = self._GET(path)
        for lang in response:
            if 'id' in lang:
                self.LANGUAGES[lang['id']] = lang
        self._ALL_PARSED = True

    def language(self, lang_id):
        """
        Get the language info for a specific language id.
        
        `id` is the specific language id to retrieve.

        Returns a dict with all the language info.
        """
        return self.__getitem__(lang_id)

    def __iter__(self):
        for i in self.all():
            yield i

    def __getitem__(self, lang_id):
        try:
            return self.LANGUAGES[lang_id]
        except KeyError:
            return {}

    def __setitem__(self):
        raise Exception('Function Disabled')
        
    def __delitem__(self):
        raise Exception('Function Disabled')
