import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

site_basedir = '../site'
screenshot_dir = 'assets/screenshots'
site_collection_dir = '_sites'

# the sites to exclude
exception_list=['argumentable', 'default', 'bobcat', 'index']

# start firefox
print('Starting firefox headless...')
opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)

# go through sites and take screenshots
for site_name in os.listdir('../../../all_sites'):
  if site_name in exception_list:
    continue

  # build site url
  site_url=f'{site_name}.talkhaus.com'
  print(f'Processing {site_url}')

  # wrap this inside a try/except in case the request fails
  try:
    # request the site
    browser.get(f'https://{site_url}')

    # get the site's title etc
    title = browser.title

    # save screenshot
    browser.get_screenshot_as_file(f"{site_basedir}/{screenshot_dir}/{site_name}.png")

    # write site data
    with open(f'{site_basedir}/{site_collection_dir}/{site_name}.md', 'w') as f:
      f.write('---\n')
      f.write(f'title: {title}\n')
      f.write(f'site_url: {site_url}\n')
      f.write(f'screenshot: {screenshot_dir}/{site_name}.png\n')
      f.write('---\n')

  except Exception as e:
    print(f'exception when processing {site_url}: {str(e)}')

print("cleaning up browser...")
browser.quit()
