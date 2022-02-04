import requests, time, os, urllib3, json
from datetime import datetime, date
from requests.auth import HTTPBasicAuth
urllib3.disable_warnings()

ip_address = "192.168.1.1"
login = "user"
password = "password"
filesystems = ["fs1", "fs2"]
locked_time = 1000*round(time.time())+144*360000 #6 days

payload = {'page_size': '50'}
json_headers = {"content-type": "application/json"}
today = "day"+str(datetime.today().isoweekday())

for fs in filesystems:
	fs_query = requests.get('https://'+ip_address+':443/api/rest/filesystems?name='+fs, auth=HTTPBasicAuth(login,password), params=payload, verify=False)
	fs_str = fs_query.json()
	fs_res = fs_str['result']
	fs_data = fs_res[0]
	fs_id =fs_data['id']
	snap_query = requests.get('https://'+ip_address+':443/api/rest/filesystems?type=eq:SNAPSHOT&sort=name&parent_id=eq:'+str(fs_id), auth=HTTPBasicAuth(login,password), params=payload, verify=False)
	snap_json = snap_query.json()
	for snap in snap_json['result']:
		if today in snap['name']:
			snap_to_del = str(snap['id'])
			del_today_snap = requests.delete('https://'+ip_address+':443/api/rest/filesystems/'+snap_to_del+'?approved=true', auth=HTTPBasicAuth(login,password), verify=False)
	snap_create_data = json.dumps({"parent_id": fs_id, "name": fs_data['name']+"_"+str(date.today())+"_"+today, "lock_expires_at": locked_time})
	create_today_snap = requests.post('https://'+ip_address+':443/api/rest/filesystems/?approved=true', data=snap_create_data, auth=HTTPBasicAuth(login,password), headers=json_headers, verify=False)
