from .util import BASE_URL, get_paginated_results
import requests

def validate_arguments(kwargs):
    expected_arguments = {'cursor'}
    keys = set(kwargs.keys())
    if not keys.issubset(expected_arguments):
        raise ValueError('Unexpected kwargs:' + str(keys - expected_arguments))

def citations(max_pages=1, **kwargs):
    if max_pages < 1:
        raise ValueError('max_pages must be an integer greater than 1')
    validate_arguments(kwargs)

    api_call = BASE_URL + 'citations/'
    return get_paginated_results(max_pages, api_call)

