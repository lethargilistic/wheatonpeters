import requests
import v1

class Reporter:
    def __init__(self, api_version=1):
        if not isinstance(api_version, int) or api_version < 1:
            raise ValueError('The api_version must be an integer greater than 0')
        versions = [0, v1]
        self.api = versions[api_version]
        self.api_version = api_version

    def cases(self, max_pages=1, **kwargs):
        if self.api in [v1]:
            return self.api.cases(max_pages, **kwargs)
        else:
            raise ValueError(f'Version {self.api_version} is not supported')
    
    def citations(self, max_pages=1, **kwargs):
        if self.api in [v1]:
            return self.api.citations(max_pages, **kwargs)
        else:
            raise ValueError(f'Version {self.api_version} is not supported')
    
    def courts(self, max_pages=1, **kwargs):
        if self.api in [v1]:
            return self.api.courts(max_pages, **kwargs)
        else:
            raise ValueError(f'Version {self.api_version} is not supported')

    def jurisdictions(self, max_pages=1, **kwargs):
        if self.api in [v1]:
            return self.api.jurisdictions(max_pages, **kwargs)
        else:
            raise ValueError(f'Version {self.api_version} is not supported')

if __name__ == "__main__":
    r = Reporter()
    response = r.cases(max_pages=1, cite='2 Ill. App. 3d 538', full_case=True)
    response = r.jurisdictions(max_pages=1)
    response = r.courts(max_pages=1)
    #response = r.citations(max_pages=5)
    print(response['count'])
    
    response = r.cases(max_pages=5, jurisdiction='alaska', full_case=True,
            decision_date_min='2001-04-01')
    print(response.keys())
    print(">>>response['count']")
    print(response['count'])
    print(">>>response['count_included']")
    print(response['count_included'])
    print(">>>response['query_url']")
    print(response['query_url'])
    print(">>>response['results'][0].keys()")
    print(response['results'][0].keys())
    
