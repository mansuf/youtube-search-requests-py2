# youtube-search-requests_py2
# async_session.py

from youtube_search_requests_py2.utils.errors import UnsupportedPython

class AsyncYoutubeSession:
    """
    **Same as YoutubeSession, but with async method**
    
    Normally, YoutubeSession class will automatically call new_session() when you call __init__().
    But, AsyncYoutubeSession doesn't do that, you have to call new_session()
    in order to get a new session from Youtube.

    AsyncYoutubeSession arguments

    preferred_user_agent: :class:`str` (optional, default: 'BOT')
        a User-Agent header to pass in session, 
        see constants.py to see all supported user-agents
    loop: :class:`asyncio.AbstractEventLoop` (optional, default: None)
        a event loop to pass in session
    restricted_mode: :class:`bool` (optional, default: False)
        This helps hide potentially mature videos.
        No filter is 100% accurate.
    """
    def __init__(self):
        raise UnsupportedPython('python 2 is not support to use async method. Please Upgrade your python.')

    def check_valid_user_agent(self):
        pass

    def get_user_agent(self):
        pass

    def _parse_preference_cookies(self):
        pass

    # TODO: add external cookies support
    def _parse_cookies(self):
        pass

    def get_session_data(self, user_agent_header=None):
        """
        coroutine / async function

        get session data from youtube
        """
        pass

    def _parse_session_data(self):
        pass


    def new_session(self):
        """
        coroutine / async function

        create a new session
        """
        pass