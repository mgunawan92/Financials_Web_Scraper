import re
import json
import csv
from io import StringIO
from bs4 import BeautifulSoup
import requests

url_stats = 'https://finance.yahoo.com/quote/{}/key-statistics?p={}'
url_profile = 'https://finance.yahoo.com/quote/{}/profile?p={}'
url_financials = 'https://finance.yahoo.com/quote/{}/financials?p={}'

stock = 'SBUX'

# use financials url to request data, assigning request to response variable
response = requests.get(url_financials.format(stock, stock))

# parse html data using Soup and default html parser
soup = BeautifulSoup(response.text, 'html.parser')

# use regex text pattern to locate Data section within html data
pattern = re.compile(r'\s--\sData\s--\s')

# locate script element matching pattern and return first item in contents list
script_data = soup.find('script', text=pattern).contents[0]

# set start of slice, beginning with "context" in script_data
start = script_data.find("context")-2

# stop at 12 characters from end of data, then patch using json.loads
json_data = json.loads(script_data[start:-12])

json_data['context'].keys()

# contains both quarterly and annual statements
json_data['context']['dispatcher']['stores']['QuoteSummaryStore'].keys()

# set annual and quarterly income statements
annual_is = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistory']['incomeStatementHistory']
quarterly_is = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistoryQuarterly']['incomeStatementHistory']

# set annual and quarterly cash flow statements
annual_cf = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['cashflowStatementHistory']['cashflowStatements']
quarterly_cf = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['cashflowStatementHistoryQuarterly']['cashflowStatements']

# set annual and quarterly balance sheet statements
annual_bs = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['balanceSheetHistory']['balanceSheetStatements']
quarterly_bs = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['balanceSheetHistoryQuarterly']['balanceSheetStatements']


# printing annual income statements
annual_is_statements = []

for s in annual_is:
		statement = {}
		for key, val in s.items():
			try:
				statement[key] = val['raw']
			except TypeError:
				continue
			except KeyError:
				continue
		annual_is_statements.append(statement)


print(annual_is_statements)


# printing annual cash flow statements
annual_cf_statements = []

for s in annual_cf:
		statement = {}
		for key, val in s.items():
			try:
				statement[key] = val['raw']
			except TypeError:
				continue
			except KeyError:
				continue
		annual_cf_statements.append(statement)


print(annual_cf_statements)


# printing annual balance sheet statements
annual_bs_statements = []

for s in annual_bs:
		statement = {}
		for key, val in s.items():
			try:
				statement[key] = val['raw']
			except TypeError:
				continue
			except KeyError:
				continue
		annual_bs_statements.append(statement)


print(annual_bs_statements)
