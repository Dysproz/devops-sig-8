import time
import random
import urllib.request 

def write_time():
    with open('/etc/config/time', 'w') as f:
        f.write(str(time.time()))

def write_const():
    with open('/etc/config/const', 'w') as f:
        f.write("{'devops_sig_no': 8}")

def write_magic(WORDS):
    with open('/etc/config/magic', 'w') as f:
        f.write(str(random.choice(WORDS)))

if __name__ == '__main__':
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = urllib.request.urlopen(word_site).read()
    WORDS = response.splitlines()
    while True:
        write_time()
        write_const()
        write_magic(WORDS)
        time.sleep(1)

