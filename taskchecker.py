from subprocess import Popen, PIPE
import re
from sys import exit

pipe = Popen(["git", "log", "-1"], stdout=PIPE)
gitLog = pipe.communicate()[0]

matchObj = re.search(r"Task\s+(\d+)",gitLog, flags=0)

if not matchObj:
    call("echo 'Your commit message needs to contain Task XXXX where X is number.'",shell=1)
    exit(1)
