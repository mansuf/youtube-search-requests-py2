# Note: Abandoned project

This repository no longer receives updates (bug fixes or new features). If you still wanna maintain it, please fork this repository. Thank you.

# youtube-search-requests-py2
### Search Youtube videos using python requests without Youtube API.

This project is for python 2 release with no async support. You can find for python 3 release with async support [in here](https://github.com/trollfist20/youtube-search-requests).

CLI (Command Line Interface) Usage:
```

usage: python -m youtube_search_requests_py2 [-h] [--max-results={Number}] [-t={Number}] [-v] [--json]
                                          [--json-output={Filename}] [--include-related-videos]
                                          [--safe-search]
                                          Search terms

Search Youtube videos using python requests without Youtube API

positional arguments:
  Search terms          a string terms want to search (if include space, you
                        must use double quotes "")

optional arguments:
  -h, --help            show this help message and exit
  --max-results={Number} 
                        maximum search results
  -t={Number} , --timeout={Number} 
                        give number of times to execute search, if times runs
                        out, search stopped & returning results
  -v , --version        show youtube-search-requests-py2 version
  --json                Return results in json format
  --json-output={Filename} 
                        Return results in output file based on json format
  --include-related-videos 
                        include all related videos each url's
  --safe-search         This helps hide potentially mature videos.
example usage:

python -m youtube_search_requests_py2 "fish" --json

# {"urls": {'title': ..., 'url': 'https://www.youtube.com/watch?v=0gT8Ty0ClHc', thumbnails: [...], ...}}


```

Simple usage:

```python

from youtube_search_requests_py2 import YoutubeSearch

y = YoutubeSearch('fish', max_results=10)
videos = y.search()

print(videos)
```

Search with given time usage:
```python

from youtube_search_requests_py2 import YoutubeSearch

# given time 60 seconds for searching videos
y = YoutubeSearch('fish', max_results=10, timeout=60) 

# if search not complete after 60 seconds
# force it to return results
videos = y.search()

print(videos)
```

Search with related videos usage:
```python

from youtube_search_requests_py2 import YoutubeSearch

y = YoutubeSearch('fish', max_results=10, include_related_videos=True) 
videos = y.search()

print(videos)

```

### youtube-search-requests-py2 support safe search !!!
### this helps to prevent mature videos in search results.

search with safe search usage:
```python

from youtube_search_requests_py2 import YoutubeSearch

y = YoutubeSearch('fish', max_results=10, safe_search=True) 
videos = y.search()

print(videos)

```

## You might be wonder, how youtube-search-requests-py2 work ?

### in-short-word:
youtube-search-requests-py2 work like Youtube in browsers (playing with POST and GET method).

### in-long-word:
- First, youtube-search-requests-py2 create a session for Youtube. (every opened youtube page in browser have it own session id)
- Second, youtube-search-requests-py2 search videos using "internal Youtube API" that have been used youtube for searching videos in browsers.
- There we go, done !!! :D.
