'''

REST API 'Spammer' for creating, updating and deleting large amount of records for testing/debug purpose

Use example (on FHIR vonk.fire.ly API):

	spammer = Spammer('https://vonk.fire.ly', 'Goal')
	> ['f0a08d20-74fe-4c15-9952-f9856c5ea8eb']
	
	goal = {
		"resourceType": "Goal",
		"status": "on-hold"
	}
	
	ids = ['f0a08d20-74fe-4c15-9952-f9856c5ea8eb']
	
	spammer.spamPut('status', 'achieved', ids)
	
	spammer.spamPost(goal, 5),
	
	spammer.deleteSpam(ids)
'''

import requests
import json

HEADERS = {"Content-type": "application/json"}

class Spammer:

	def __init__(self, url, endpoint):
		"""
		@param endpoint: API endpoint
		@param url: API url
		@return: nothing - prints ids of first 500 records at this endpoint
		"""
		
		self.url = '{}/{}'.format(url, endpoint)
		self.id_list = self.fetchIds()
        print(self.id_list)
		
	def fetchIds(self):
		"""
		Fetches ids of given FHIR endpoint - edit mapping to adjust it for any API
		"""
		try:
			return list(map(lambda resource: resource['resource']['id'], requests.get(self.url+'?_count=500').json()['entry']))
		except:
			print('Given API does not match FHIR schema. To see your endoint ids edit fetchIds() function.')
            return []

	def spamPut(self, prop, new_value, ids):
		"""
		@param prop: property to update
		@param new_value: new value of given property
		@param ids: range of ids to PUT
		@returns None: prints HTTP response log
		"""
		
		for i in ids:
			data = requests.get('{}/{}'.format(self.url, str(i)), headers = HEADERS).json()
			data[prop] = new_value
			data = json.dumps(data)
			
			response = requests.put('{}/{}'.format(self.url, str(i)), data, headers= HEADERS)
			print(response.text)
		
	def spamPost(self, data, size):
		"""
		@param data: dictionary representation of JSON you want to POST
		@param size: number of records to POST
		@returns None: prints HTTP response log
		"""
		data = json.dumps(data)
		
		for i in range(1, size):
			response = requests.post(self.url, data, headers = HEADERS)
			print(response.text)
	
	def spamDelete(self, ids):
		"""
		@param ids: range of ids to be DELETEd
		@returns None: prints HTTP response log
		"""
	
		for i in ids:
			response = requests.delete(self.url + '/' + str(i))
			print(response.text)
