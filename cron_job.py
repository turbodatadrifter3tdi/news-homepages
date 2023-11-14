import random
from datetime
import datetime
now = datetime.now()
num = random.randint(1, 101)
with open('/tmp/rand.txt', 'a') as f:
    f.write{f'{} - Your random number is {}\n'. format(now, num))
    # As a next step, now in the `crontab -e` put the absolute path:  ***** /usr/bin/python3 /root/cron_job.py