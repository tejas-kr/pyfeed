import time
import notify2
from topnews import topStories

ICON_PATH = 'icon.png'
newsitems = topStories()
notify2.init("pyfeed News Notifier")
n = notify2.Notification(None, icon = ICON_PATH)
n.set_urgency(notify2.URGENCY_NORMAL)
n.set_timeout(20000)
for newsitem in newsitems:
    n.update(newsitem['title'], newsitem['description'])
    n.show()
    time.sleep(15)
