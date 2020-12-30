# youtube-search-requests_py2
# session.py

import json
import random
from requests import Session
from youtube_search_requests_py2.constants import USER_AGENT_HEADERS
from youtube_search_requests_py2.utils import parse_json_session_data, YoutubePreferenceCookie
from youtube_search_requests_py2.utils.errors import InvalidArgument

# Because i don't know how to subclass in python 2
# i will do it in old way
class YoutubeSession:
    """
    YoutubeSession arguments

    preferred_user_agent: :class:`str` (optional, default: 'BOT')
        a User-Agent header to pass in session, 
        see constants.py to see all supported user-agents
    restricted_mode: :class:`bool` (optional, default: False)
        This helps hide potentially mature videos.
        No filter is 100% accurate.
    """
    def __init__(self, preferred_user_agent='BOT', restricted_mode=False):
        self.BASE_URL = 'https://www.youtube.com/'
        self.check_valid_user_agent(preferred_user_agent)
        self._subclass = Session()
        self.preferred_user_agent = preferred_user_agent
        self.restricted_mode = restricted_mode
        self._RESTRICTED_MODE_PREFERENCE = 'f2=8000000'
        self.new_session()

    def check_valid_user_agent(self, user_agent):
        try:
            USER_AGENT_HEADERS[user_agent]
        except KeyError:
            raise InvalidArgument('invalid user-agent')

    def get_user_agent(self, preferred_user_agent):
        return random.choice(USER_AGENT_HEADERS[preferred_user_agent])

    def get(self, url, **kwargs):
        return self._subclass.get(url, **kwargs)

    def post(self, url, **kwargs):
        return self._subclass.post(url, **kwargs)

    def _parse_preference_cookies(self):
        c = YoutubePreferenceCookie()
        if self.restricted_mode:
            c.add_preference(self._RESTRICTED_MODE_PREFERENCE)
        return c.get_cookie()

    # TODO: add external cookies support
    def _parse_cookies(self):
        return self._parse_preference_cookies()

    def get_session_data(self, user_agent_header=None):
        if user_agent_header is None:
            r = self.get(self.BASE_URL)
        else:
            r = self.get(self.BASE_URL, headers={'User-Agent': user_agent_header})
        return parse_json_session_data(r)

    def _parse_session_data(self, data):
        self.data = data
        self.key = data['INNERTUBE_API_KEY']
        self.client = data['INNERTUBE_CONTEXT']
        self.id = data['INNERTUBE_CONTEXT']['request']['sessionId']

    def new_session(self):
        while True:
            self._subclass = Session()
            self.USER_AGENT = self.get_user_agent(self.preferred_user_agent)
            data = self.get_session_data(self.USER_AGENT)
            try:
                self._parse_session_data(data)
                break
            except KeyError:
                continue


