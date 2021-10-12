import json
import threading
import random
import time
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url = 'https://abc.tngtech.com/'
thread_list = list()
lock = threading.Lock()

with open('config.json') as fin:
  config = json.load(fin)

port = 9222

def do_work():
  global url, config, port, lock
  d = DesiredCapabilities.CHROME
  d['goog:loggingPrefs'] = { 'browser':'ALL' }
  options = Options()
  options.add_argument('--no-sandbox')
  options.add_argument('--log-level=3')
  options.add_argument('--disable-gpu')
  options.add_argument('--disable-software-rasterizer')
  options.add_argument(f'--remote-debugging-port={port}')
  port += 1
  options.add_argument('--headless')
  browser = webdriver.Chrome(desired_capabilities=d, options=options)
  browser.get(url)
  name_field = browser.find_element_by_id('user')
  name_field.send_keys(config.get('name'))
  start_button = browser.find_elements_by_class_name("_flex_3j81w_16")[1]
  browser_id = uuid.uuid4()

  while True:
    try:
      start_button.click()
      time.sleep(1)

      for log in browser.get_log('browser'):
        if "worker result" in (m := log.get('message')):
          data = json.loads(m[m.index('{'):])
          data['browser_id'] = str(browser_id)
          data['low_a'] = int(data['low_a'])
          data['low_b'] = int(data['low_b'])
          data['high_a'] = int(data['high_a'])
          data['high_b'] = int(data['high_b'])
          if any(data['result']):
            for index in range(len(data['result'])):
              data['result'][index]['a'] = int(data['result'][index]['a'])
              data['result'][index]['b'] = int(data['result'][index]['b'])
              data['result'][index]['q'] = float(data['result'][index]['q'])
          with lock:
            with open('output.ndjson', 'a') as fout:
              fout.write(json.dumps(data) + '\n')
          time.sleep(2+4*random.random())
    except:
      time.sleep(2+4*random.random())
      continue
  return

for _ in range(config.get('threads')):
  time.sleep(1)
  t = threading.Thread(target=do_work)
  t.start()
  thread_list.append(t)

for thread in thread_list:
  thread.join()
