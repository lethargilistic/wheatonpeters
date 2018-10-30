import requests
import v1

class Reporter:
    def __init__(self, api_version=1):
        if not isinstance(api_version, int) or api_version < 1:
            raise ValueError('The api_version must be an integer greater than 0')
        versions = [0, 'v1']
        self.BASE_URL = f'https://api.case.law/{versions[api_version]}/'
        self.api_version = api_version

    def cases(self, max_pages=1, **kwargs):
        if self.api_version == 1:
            return v1.cases(max_pages, **kwargs)
        else:
            raise ValueError(f'Version {self.api_version} is not supported')

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
