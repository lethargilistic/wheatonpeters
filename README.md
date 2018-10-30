#WheatonPeters

This Python wrapper grants easy access to the [CAPAPI](https://case.law/api/)
provided by the [Caselaw Access Project](https://case.law/). It liberates state
and federal court cases.

#Usage
Start by creating a Reporter.

```python
>>>from wheatonpeters import Reporter
>>>wheaton = Reporter()
```

You can then use your Reporter to make the level API calls and pass in filter
arguments. In return, you'll get an object representing the json response.

WheatonPeters adds some useful entries to the top level dictionary, but the
`results` list matches the response from the CAPAPI exactly. WheatonPeters will
retrieve up to `max_pages` API calls and concatenate the `results` of all of
them.

```python
>>>response = wheaton.case('2 Ill. App. 3d 538')
>>>response
{'count': 1, 'count_included': 1, 'url': "THE_URL", 'results': {...}}
>>>response['results'][0].
dict_keys(['id', 'url', 'name', 'name_abbreviation', 'decision_date', 'docket_number', 'first_page', 'last_page', 'citations', 'volume', 'reporter', 'court', 'jurisdiction', 'casebody'])
```

```python
>>>response = r.cases(max_pages=5, jurisdiction='alaska', full_case=True, decision_date_min='2001-04-01')
>>>response.keys()
dict_keys(['count', 'results', 'count_included', 'query_url'])
>>>response['count']
1548
>>>response['count_included']
500
>>>response['query_url']
https://api.case.law/v1/cases/?jurisdiction=alaska&full_case=true&decision_date_min=2001-04-01
>>>response['results'][0].keys()
dict_keys(['id', 'url', 'name', 'name_abbreviation', 'decision_date', 'docket_number', 'first_page', 'last_page', 'citations', 'volume', 'reporter', 'court', 'jurisdiction', 'casebody'])
```

The contents of results

#TODO
[x] cases
[] citations
[] jurisdictions
[] courts
[] volumes
[] reporters
[] bulk

#Name
WheatonPeters is named for a legendary Supreme Court case, *Wheaton v. Peters*,
between two Supreme Court reporters that determined that the text of the Court's
decisions could not be restricted by copyright.

#Platform Support
I only use Linux, and I'm not personally going to test it on anything else.
