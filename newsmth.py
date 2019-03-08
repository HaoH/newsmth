import sys
import random
import time
import requests

rand = random.Random()

def print_log(msg):
    print('[{}] {}'.format(time.ctime().split()[3], msg))

def auto_hook_newsmth(smth_id, passwd):
    print_log("id:{}, passwd:{}".format(smth_id, passwd))

    sess = requests.session()
    sess.headers = { 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

    print_log("get homepage...")
    resp = sess.get('http://m.newsmth.net/')
    time.sleep(rand.randint(3,5))

    print_log('login...')
    postdata = {'id': smth_id, 'passwd': passwd, 'save':'on'}
    resp = sess.post('http://m.newsmth.net/user/login', data=postdata)
    login_time=time.time()

    print_log('online...')
    while True:
        time.sleep(rand.randint(30,60))
        resp = sess.get('http://m.newsmth.net/board/ITExpress')
        rand_time = 1800 + rand.randint(100, 500)
        if time.time()-login_time > rand_time:
            break

    print_log("logout...")
    resp = sess.get('http://m.newsmth.net/user/logout')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print_log("Usage: python newsmth.py id password")
        exit(1)

    while True:
        try:
            auto_hook_newsmth(sys.argv[1], sys.argv[2])
        except Exception as e:
            print_log("get exception: %s" % e)
            time.sleep(rand.randint(100,200))
