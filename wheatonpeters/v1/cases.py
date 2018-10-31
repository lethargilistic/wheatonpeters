from .util import BASE_URL, get_paginated_results, validate_keywords
import requests

def cases(max_pages=1, **kwargs):
    if max_pages < 1:
        raise ValueError('max_pages must be an integer greater than 1')

    expected_keywords = {'cite', 'name_abbreviation', 'jurisdiction',
            'reporter', 'decision_date_min', 'decision_date_max',
            'docket_number', 'court', 'search', 'full_case', 'body_format',
            'cursor'}
    validate_keywords(expected_keywords, kwargs)

    api_call = BASE_URL + 'cases/'

    for i, key in enumerate(kwargs):
        if i == 0:
            api_call += "?"
        else:
            api_call += "&"
        value = str(kwargs[key]).lower()
        api_call += f"{key}={value}"

    return get_paginated_results(max_pages, api_call)
