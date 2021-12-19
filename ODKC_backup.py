from urllib2 import Request, urlopen, URLError
import requests
import json
import cgi
import os

##funciton def
def backup(central_url, session_token, passphrase):

    backup_response = requests.post(
        central_url + "/v1/backup",
        data = json.dumps({"passphrase": passphrase}),
        headers = {"Authorization": "Bearer " + session_token,
                   "Content-Type": "application/json"},
        stream = True
    )

    if backup_response.status_code == 200:
        _, params = cgi.parse_header(backup_response.headers.get('Content-Disposition', ''))
        filename = params["filename"].replace(":","-")
        file = open(filename, "wb")
        file.write(backup_response.content)
        print("Backup successful")


##variables
central_url =  "server_url"
passphrase = "login_password"

##Login  and Session API Calling
print("Assessing credentials ...")
values = """
  {
    "email": "login_email",
    "password": "login_password"
  }
"""



headers = {
  'Content-Type': 'application/json'
}

print("Attempting login ...")
request = Request(central_url +'/v1/sessions', data=values, headers=headers)

try:
	response_body = urlopen(request).read()
except URLError, e:
	if hasattr(e, 'reason'):
		print 'We failed to reach a server.'
		print 'Reason: ', e.reason

	elif hasattr(e, 'code'):
		print 'The server could not fulfill the request.'
		print 'Error code: ', e.code
else:
	print("Success!")


print("Obtaining session token ...")
json_object = json.loads(response_body)

session_token = json_object["token"]
#print(token)

##Backup API Calling
print("Downloading backup. NB: This may take some few minutes.")
backup(central_url, session_token, passphrase)



