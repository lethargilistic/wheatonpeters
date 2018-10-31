from .util import BASE_URL, get_paginated_results, validate_keywords
import requests

def volumes(max_pages=1, **kwargs):
    if max_pages < 1:
        raise ValueError('max_pages must be an integer greater than 1')

    expected_keywords = {'cursor'}
    validate_keywords(expected_keywords, kwargs)

    api_call = BASE_URL + 'volumes/'
    return get_paginated_results(max_pages, api_call)
