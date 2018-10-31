from .util import BASE_URL, get_paginated_results, validate_keywords
import requests

def reporters(max_pages=1, **kwargs):
    if max_pages < 1:
        raise ValueError('max_pages must be an integer greater than 1')

    expected_keywords = {'jurisdictions', 'full_name', 'short_name', 'start_year', 'end_year',
            'volume_count', 'cursor'}
    validate_keywords(expected_keywords, kwargs)

    api_call = BASE_URL + 'reporters/'
    return get_paginated_results(max_pages, api_call)
