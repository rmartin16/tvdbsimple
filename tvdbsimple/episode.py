# -*- coding: utf-8 -*-

"""
This module implements the Episode functionality of TheTVDb API.
Allows to retrieve episode detailed info.

See [Episodes API section](https://api.thetvdb.com/swagger#!/Episodes)
"""

from .base import TVDB


class Episode(TVDB):
    """
    Episode class to retrieve detailed info about an episode.
    Requires the episode id.
    """
    _BASE_PATH = 'episodes'
    _URLS = {
        'info': '/{id}'
    }

    def __init__(self, episode_id, language=''):
        """
        Initialize the episode class.

        `id` is the TheTVDb episode id. You can also provide `language`, 
        the language id you want to use to retrieve the info.
        """
        super(Episode, self).__init__(episode_id, language=language)
        self.response = None
        self._fetch_info()

    def _fetch_info(self):
        """
        Get the episode information of the episode and set its values to the local attributes.

        You can set `language` with the language id to retrieve info in that specific language.
        """
        path = self._get_id_path('info')
        
        self.response = self._GET(path)
        self._set_attrs_to_values(self.response)

    def info(self):
        """
        get raw TVDB episode dict
        :return: episode dict
        """
        return self.response
