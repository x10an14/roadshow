from subprocess import Popen, PIPE, call
import re

pipe = Popen(["git", "log", "-1"], stdout=PIPE)
stdout, stderr = pipe.communicate()

matchObj = re.search(r"Task\s+(\d+)", stdout, flags=0)

if not matchObj:
    call("echo 'Your commit message needs to contain Task XXXX where X is number.'",shell=1)
    call(["exit","1"], shell=1)
