from .util import BASE_URL, get_paginated_results, validate_keywords
import requests

def courts(max_pages=1, **kwargs):
    if max_pages < 1:
        raise ValueError('max_pages must be an integer greater than 1')

    expected_keywords = {'slug', 'name', 'name_abbreviation', 'jurisdiction', 'cursor'}
    validate_keywords(expected_keywords, kwargs)

    api_call = BASE_URL + 'courts/'
    return get_paginated_results(max_pages, api_call)

