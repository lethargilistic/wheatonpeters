import requests

BASE_URL = f'https://api.case.law/v1/'
VERSION_NAME = 'v1'

def get_paginated_results(max_pages, api_call):
    curr_api_call = api_call
    query_result = dict()

    response = requests.get(curr_api_call)
    response.raise_for_status()
    query_result = response.json()
    max_pages -= 1
    
    while max_pages > 0:
        response = requests.get(curr_api_call)
        response.raise_for_status()
        curr_json = response.json()
        
        query_result['results'] += curr_json['results']

        if not curr_json['next']:
            #Reached end of results, regardless of max_pages
            break
        curr_api_call = curr_json['next']
        max_pages -= 1

    del query_result['previous']
    del query_result['next']
    query_result['count_included'] = len(query_result['results'])
    query_result['query_url'] = api_call
    return query_result


def validate_keywords(expected_arguments, keywords):
    keys = set(keywords.keys())
    if not keys.issubset(expected_arguments):
        raise ValueError('Unexpected kwargs:' + str(keys - expected_arguments))
