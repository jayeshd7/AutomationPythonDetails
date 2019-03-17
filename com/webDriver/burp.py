# import the package
from PyBurprestapi import burpscanner

# setup burp connection
host = 'http://localhost:8080'


#

bi = burpscanner.BurpApi(host)
bi.

# Add target in burp scope

response = bi.burp_scope('http://testwebsite.com')

# Get the response message
print(response.message)
