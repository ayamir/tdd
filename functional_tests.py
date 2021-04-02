from msedge.selenium_tools import EdgeOptions, Edge

options = EdgeOptions()
options.use_chromium = True
options.binary_location = r'/usr/bin/microsoft-edge-dev'
options.set_capability("platform", "LINUX")

webdriver_path = r'/home/ayamir/.local/bin/msedgewebdriver'

browser = Edge(options=options, executable_path=webdriver_path)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
