import pytest
import requests
import json
import pdb

from com.PyTestDemo.API.conftest import supply_url

'''
@pytest.mark.parametrize("userid, firstname, lastname",[(1,"George","Bluth"),(2,"Janet","Weaver")])
def test_list_valid_user(supply_url,userid,firstname,lastname):
	url = supply_url + "/users/" + str(userid)
	resp = requests.get(url)
	print(resp)
	j = json.loads(resp.text)
	assert resp.status_code == 200, resp.text
	assert j['data']['id'] == userid, resp.text
	assert j['data']['first_name'] == firstname, resp.text
	assert j['data']['last_name'] == lastname,resp.text
	#assert j['token']=='QpwL5tke4Pnpja7X',resp.text

def test_list_invaliduser(supply_url):
	url = supply_url + "/users/50"
	resp = requests.get(url)
	assert resp.status_code == 404, resp.text
	
'''



def test_fingerDeviceID(supply_url):
	url = supply_url + "/user_qa/device?id1=8920f88ad7c5fb9f&id2=b23ec479-fb46-46bc-8063-f1eeb31b5c0c"
	headers = {'Content-type':'application/json','x-client-auth':'b6fea2dd3d110b12fbd23d7ab8cd0ba3',
				'x-request-id':'1','x-session-id':'VQEaCWPNLZDdQjB1IGGx1xVlyQNTQeIp','x-client':'android'

			   }
	resp = requests.get(url, headers=headers)

	print(resp)

	j = json.loads(resp.text)

	assert resp.status_code == 200, resp.text
	assert j['deviceId'] == '9442f50f-f1d3-47ba-b531-03f0cf248084', resp.text

'''
def test_identity(supply_url):
	url = supply_url + "/user_qa"
	headers = {'Content-type': 'application/json',
			   'x-request-id': '2', 'x-session-id': 'VQEaCWPNLZDdQjB1IGGx1xVlyQNTQeIp', 'x-client': 'android'

			   }
	data = {'deviceId':'9442f50f-f1d3-47ba-b531-03f0cf248084'}



	resp = requests.post(url, headers=headers, data=json.dumps(data))


	#assert resp.status_code == 200, resp.text
	assert resp.json['userId'] == 'cf2f3549-9176-48e6-9ecd-8a59f8070274', resp.text
'''