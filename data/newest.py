#!/usr/bin/python3
# NPNDecode :)

import os
try:
import requests,colorama,prettytable
except:
os.system("pip install requests")
os.system("pip install colorama")
os.system("pip install prettytable")
import threading, requests, ctypes, random, json, time, base64, sys, re
from prettytable import PrettyTable
import random
from time import strftime
from colorama import init, Fore
from urllib.parse import urlparse, unquote, quote
from string import ascii_letters, digits

class Zefoy:
# if os.path.exists('config.json') is False: open('config.json','w',encoding='utf-8',errors='ignore').write(json.dumps( {'url':'https://www.tiktok.com/t/ZTRToxYct','service':'Views'},indent=4))

def __init__(self):
self.base_url = 'https://zefoy.com/'
self.headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
self.session = requests.Session()
self.captcha_1 = None
self.captcha_ = {}
self.service = 'Views'
self.video_key = None
self.services = {}
self.services_ids = {}
self.services_status = {}
self.url = 'None'
self.text = 'LAM TILO'
url1=input("[LÁMTILO]</> Enter video link: ")
self.url=url1

def get_captcha(self):
if os.path.exists('session'): self.session.cookies.set("PHPSESSID", open('session',encoding='utf-8').read(), domain='zefoy.com' )
request = self.session.get(self.base_url, headers=self.headers)
if 'Enter Video URL' in request.text: self.video_key = request.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]; return True

try:
for x in re.findall(r'<input type="hidden" name="(.*)" value="(.*)">', request.text): self.captcha_[x[0]] = x[1]

self.captcha_1 = request.text.split('type="text" name="')[1].split('" oninput="this.value=this.value.toLowerCase()"')[0]
captcha_url = request.text.split('<img src="')[1].split('" onerror="imgOnError()" class="')[0]
request = self.session.get(f"{self.base_url}{captcha_url}",headers=self.headers)
open('captcha.png', 'wb').write(request.content)
print('[LâmTILO]</> Solving capcha..')
return False
except Exception as e:
print(f"[LâmTILO]</> Unable to solve captcha: {e}")
time.sleep(2)
self.get_captcha()

def send_captcha(self, new_session = False):
if new_session: self.session = requests.Session(); os.remove('session'); time.sleep(2)
if self.get_captcha(): print('[LÁMTILO]</> Connecting to session');return (True, 'The session already exists')
captcha_solve = self.solve_captcha('captcha.png')[1]
self.captcha_[self.captcha_1] = captcha_solve
request = self.session.post(self.base_url, headers=self.headers, data=self.captcha_)

if 'Enter Video URL' in request.text:
print('[LâmTILO]</> Session has been created')
open('session','w',encoding='utf-8').write(self.session.cookies.get('PHPSESSID'))
print(f"[LâmTILO]</> Captcha solved successfully: {captcha_solve}")
self.video_key = request.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]
return (True,captcha_solve)
else: return (False,captcha_solve)

def solve_captcha(self, path_to_file = None, b64 = None, delete_tag = ['\n','\r']):
if path_to_file: task = path_to_file
else: open('temp.png','wb').write(base64.b64decode(b64)); task = 'temp.png'
request = self.session.post('https://api.ocr.space/parse/image?K87899142388957', headers={'apikey':'K87899142388957'}, files={'task':open(task,' rb')}).json()
solved_text = request['ParsedResults'][0]['ParsedText']
for x in delete_tag: solved_text = solved_text.replace(x,'')
return (True, solved_text)

def get_status_services(self):
request = self.session.get(self.base_url, headers=self.headers).text
for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+\n.+', request): self.services[x.split('<h5 class ="card-title">')[1].split('<')[0].strip()] = x.split('d-sm-inline-block">')[1].split( '</small>')[0].strip()
for x in re.findall(r'<h5 class="card-title mb-3">.+</h5>\n<form action=".+">', request): self.services_ids[x. split('title mb-3">')[1].split('<')[0].strip()] = x.split('<form action="')[1].split('" >')[0].strip()
for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+<button .+', request): self.services_status[x.split('<h5 class ="card-title">')[1].split('<')[0].strip()] = False if 'disabled class' in x else True
return (self.services, self.services_status)

def get_table(self, i = 1):
table = PrettyTable(field_names=["ID", "SERVICES", "Status"], title="Status Services", header_style="upper",border=True)
whileTrue:
if len(self.get_status_services()[0])>1:break
else:print('Cant get services, retrying...');self.send_captcha();time.sleep(2)
for service in self.services: table.add_row([f"{Fore.CYAN}{i}{Fore.RESET}", service, f"{Fore.GREEN if 'ago updated' in self.services[service] else Fore.RED}{self.services[service]}{Fore.RESET}"]); i+=1
table.title = f"{Fore.YELLOW}Active Services Number: {len([x for x in self.services_status if self.services_status[x]])}{Fo
