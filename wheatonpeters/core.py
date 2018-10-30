import requests

class Reporter:
    def __init__(self, api_version=1):
        if not isinstance(api_version, int) or api_version < 1:
            raise ValueError('The api_version must be an integer greater than 0')
        versions = [0, 'v1']
        self.BASE_URL = f'https://api.case.law/{versions[api_version]}/'

    def cases(self, max_pages=1, **kwargs):
        if max_pages < 1:
            raise ValueError('max_pages must be an integer greater than 1')

        api_call = self.BASE_URL + 'cases/'

        expected_arguments = {'cite', 'name_abbreviation', 'jurisdiction',
                'reporter', 'decision_date_min', 'decision_date_max',
                'docket_number', 'court', 'search', 'full_case', 'body_format',
                'cursor'}
        keys = set(kwargs.keys())
        if not keys.issubset(expected_arguments):
            raise ValueError('Unexpected kwargs:' + str(keys - expected_arguments))

        
        for i, key in enumerate(kwargs):
            if i == 0:
                api_call += "?"
            else:
                api_call += "&"
            print(key)
            value = str(kwargs[key]).lower()
            api_call += f"{key}={value}"

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

if __name__ == "__main__":
    r = Reporter()
    #response = r.cases(cite='2 Ill. App. 3d 538', full_case=True)
    response = r.cases(max_pages=5, jurisdiction='alaska', full_case=True, decision_date_min='2001-04-01')
    print(response.keys())
    print(">>>response['count']")
    print(response['count'])
    print(">>>response['count_included']")
    print(response['count_included'])
    print(">>>response['query_url']")
    print(response['query_url'])
    print(">>>response['results'][0].keys()")
    print(response['results'][0].keys())
