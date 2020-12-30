import pathlib
from setuptools import setup
import sys

__VERSION__ = 'v0.0.25'

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").open('r').read()

setup(
  name = 'youtube-search-requests-py2',         
  packages = ['youtube_search_requests_py2', 'youtube_search_requests_py2/utils'],   
  version = __VERSION__,
  license='MIT',     
  description = 'Search Youtube videos using python requests without Youtube API in python 2',
  long_description= README,
  long_description_content_type= 'text/markdown',
  author = 'Rahman Yusuf',              
  author_email = 'danipart4@gmail.com',
  url = 'https://github.com/trollfist20/youtube-search-requests-py2',  
  download_url = 'https://github.com/trollfist20/youtube-search-requests-py2/archive/%s.tar.gz' % (__VERSION__),
  keywords = ['youtube', 'youtube-search', 'python 2'], 
  install_requires=[           
          'requests'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',  
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 2 :: Only',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7'
  ],
)
