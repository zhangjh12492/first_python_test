from  com.bc.cp.util.redis_util import *
import sys

if __name__ == '__main__':

    # exe_pipeline_del_redis_keys('_bet_userOrStatusSet*')
    if len(sys.argv) > 1:
        if sys.argv[1] == 'delete':
            exe_pipeline_del_redis_keys('_bet_userOrStatusSet*')
        elif sys.argv[1] == 'get':
            exe_keys(sys.argv[1] + "*")
    else:
        print('no redis match key')