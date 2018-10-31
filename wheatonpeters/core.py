import requests
import v1

class Reporter:
    def __init__(self, api_version=1):
        versions = [0, v1]
        if not isinstance(api_version, int) or not api_version < len(versions):
            raise ValueError(f'You entered: {repr(api_version)}. It either has no support, or you did not enter an integer.')
        self.api = versions[api_version]

    def cases(self, max_pages=1, **kwargs):
        if self.api in [v1]:
            return self.api.cases(max_pages, **kwargs)
        else:
            raise ValueError(f'cases/ is not supported for Version {self.api.VERSION_NAME}')
    
    def citations(self, max_pages=1, **kwargs):
        if self.api in [v1]:
            return self.api.citations(max_pages, **kwargs)
        else:
            raise ValueError(f'citations/ is not supported for Version {self.api.VERSION_NAME}')
    
    def courts(self, max_pages=1, **kwargs):
        if self.api in [v1]:
            return self.api.courts(max_pages, **kwargs)
        else:
            raise ValueError(f'courts/ is not supported for Version {self.api.VERSION_NAME}')

    def jurisdictions(self, max_pages=1, **kwargs):
        if self.api in [v1]:
            return self.api.jurisdictions(max_pages, **kwargs)
        else:
            raise ValueError(f'jurisdictions/ is not supported for Version {self.api.VERSION_NAME}')

    def volumes(self, max_pages=1, **kwargs):
        if self.api in [v1]:
            return self.api.volumes(max_pages, **kwargs)
        else:
            raise ValueError(f'volumes/ is not supported for Version {self.api.VERSION_NAME}')

if __name__ == "__main__":
    r = Reporter()
    #response = r.cases(max_pages=1, cite='2 Ill. App. 3d 538', full_case=True)
    #response = r.jurisdictions(max_pages=1)
    #response = r.courts(max_pages=1)
    response = r.volumes(max_pages=1)
    #response = r.citations(max_pages=5)
    print(response['count'])
    print(response)
    
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
    
