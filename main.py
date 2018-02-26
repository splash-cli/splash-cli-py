import urllib2, urllib
import json
import os	
from appscript import app, mactypes


HOME_PATH = os.path.expanduser('~')
BASE_PATH = os.path.join(HOME_PATH, 'Pictures', 'splash_py')
CLIENT_ID = 'daf9025ad4da801e4ef66ab9d7ea7291a0091b16d69f94972d284c71d7188b34'

website = urllib2.urlopen("https://api.unsplash.com/photos/random?client_id=" + CLIENT_ID).read()
photo = json.loads(website)

if os.path.exists(BASE_PATH) == False:
	os.mkdir(BASE_PATH)

download = {
	'path': os.path.join(BASE_PATH, photo['id'] + '.jpg'),
    'url': photo['urls']['full']
}

file = urllib.urlretrieve(download['url'], download['path'])
app('Finder').desktop_picture.set(mactypes.File( file[0] ))

print "All done!"
