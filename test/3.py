import requests

response = requests.post(
    'https://mp.weixin.qq.com/mp/getappmsgext',
    params=[('__biz',
             'MzI5OTUzMjQ1NQ=='),
            ('appmsg_type',
             '9'),
            ('mid',
             '2247485258'),
            ('sn',
             'c4ce4f9b39a7bc7a7d05fcad28e3016b'),
            ('idx',
             '1'),
            ('scene',
             '27'),
            ('title',
             '这是英国最好幼儿园：孩子天天在村里玩'),
            ('ct',
             '1517529600'),
            ('abtest_cookie',
             'AgABAAoADAAJAGiKHgCbih4An4oeAPGKHgA2ix4APoseAEmLHgBMix4AUoseAAAA'),
            ('devicetype',
             'android-25'),
            ('version',
             '/mmbizwap/zh_CN/htmledition/js/appmsg/index3b1748.js'),
            ('f',
             'json'),
            ('r',
             '0.8534424633719688'),
            ('is_need_ad',
             '1'),
            ('comment_id',
             '1133623003'),
            ('is_need_reward',
             '0'),
            ('both_ad',
             '0'),
            ('reward_uin_count',
             '0'),
            ('msg_daily_idx',
             '1'),
            ('is_original',
             '0'),
            ('uin',
             '777'),
            ('key',
             '777'),
            ('pass_ticket',
             'FhveV34Lga%252BVd%252F68dz70uqjC6TsvyiBuvJCgRDiBQ39PHMHS%252BSS%252Bk%252FM%252BWSPqwS3D'),
            ('wxtoken',
             '231068325'),
            ('devicetype',
             'android-25'),
            ('clientversion',
             '26060235'),
            ('appmsg_token',
             '942_sZe03a17vMcd5Rf3uuErjSr6OgL5llF50vCOcrs12gPAXG3M7kaNMdT1vZGlh-6DwSv_7gDQZe9odNm0'),
            ('x5',
             '1'),
            ('f',
             'json')],
    headers={'Accept': '*/*',
             'Accept-Encoding': 'gzip, '
                                'deflate',
             'Accept-Language': 'zh-CN,en-US;q=0.8',
             'Connection': 'keep-alive',
             'Content-Type': 'application/x-www-form-urlencoded; '
                             'charset=UTF-8',
             'Cookie': 'sd_userid=95501515129566605; '
                       'sd_cookie_crttime=1515129566605; '
                       'tvfe_boss_uuid=348c774be61fe40d; '
                       'uid_uin=144115209587362569; '
                       'uid_a2=f62afcd657b5d68dbd9b6f87d043ea905a7f7e92710693d46357c3b01706570b619e1999bf05ffdf59d19d8e68703d91f823f034cf3a1d952e3f58fc2592c6c023d8fbbd568245c5; '
                       'uid_type=2; '
                       'uid_appid=1400000008; '
                       'openid=oZMPft7ubKAJljG5-Arsb22p0Hek; '
                       'pac_uid=0_5a61e4f05a7ca; '
                       '_ga=GA1.2.1464213711.1516365043; '
                       'pgv_info=ssid=s2276347571; '
                       'pgv_pvid=4674337370; '
                       'rewardsn=; '
                       'wxtokenkey=ad32fa61abb10fbe3b89ce025ad91d9cfe4a4b25dd6c814dc0451228e21a6650; '
                       'wxuin=2050863400; '
                       'devicetype=android-25; '
                       'version=26060235; '
                       'lang=zh_CN; '
                       'pass_ticket=FhveV34Lga+Vd/68dz70uqjC6TsvyiBuvJCgRDiBQ39PHMHS+SS+k/M+WSPqwS3D; '
                       'wap_sid2=CKji9tEHEnByNTlNTm1ablRXNGI5X1dDVVZLODZJX2pKV2EwODhUQWlzZk5QRjAtWDFlakc0Z0JEZFR5RVZYZGg5OS1waUdUeVczQkIwMlh0cUF2R2w0Y3ZIUTdacnpIamNRaHY4eThyYVhvRndjR2tjLXVBd0FBMPvx1NMFOA1AAQ==',
             'Origin': 'https://mp.weixin.qq.com',
             'Q-Auth': '31045b957cf33acf31e40be2f3e71c5217597676a9729f1b',
             'Q-GUID': '5eb5db0bde0cc30385026afe111b88cb',
             'Q-UA2': 'QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.6.2&TBSVC=43603&CO=BK&COVC=043808&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= '
                      'ONEPLUSA5010 '
                      '&RL=1080*2046&OS=7.1.1&API=25',
             'Referer': 'https://mp.weixin.qq.com/s?__biz=MzI5OTUzMjQ1NQ==&mid=2247485258&idx=1&sn=c4ce4f9b39a7bc7a7d05fcad28e3016b&chksm=ec946e82dbe3e794b2edd246342b8e08e61fd8abc513149a33c95f36a9901928695c0ab1384e&scene=27&ascene=0&devicetype=android-25&version=26060235&nettype=WIFI&abtest_cookie=AgABAAoADAAJAGiKHgCbih4An4oeAPGKHgA2ix4APoseAEmLHgBMix4AUoseAAAA&lang=zh_CN&pass_ticket=FhveV34Lga%2BVd%2F68dz70uqjC6TsvyiBuvJCgRDiBQ39PHMHS%2BSS%2Bk%2FM%2BWSPqwS3D&wx_header=1',
             'User-Agent': 'Mozilla/5.0 '
                           '(Linux; '
                           'Android '
                           '7.1.1; '
                           'ONEPLUS '
                           'A5010 '
                           'Build/NMF26X; '
                           'wv) '
                           'AppleWebKit/537.36 '
                           '(KHTML, '
                           'like '
                           'Gecko) '
                           'Version/4.0 '
                           'Chrome/57.0.2987.132 '
                           'MQQBrowser/6.2 '
                           'TBS/043808 '
                           'Mobile '
                           'Safari/537.36 '
                           'MicroMessenger/6.6.2.1240(0x26060235) '
                           'NetType/WIFI '
                           'Language/zh_CN',
             'X-Requested-With': 'XMLHttpRequest'},
    data=(b'is_only_read=1&req_id=0312g9nQwTzG4JBrom2UIlFs&pass_ticket=FhveV34Lga%25252B'
          b'Vd%25252F68dz70uqjC6TsvyiBuvJCgRDiBQ39PHMHS%25252BSS%25252Bk%25252FM%25252BW'
          b'SPqwS3D&is_temp_url=0')
)

print(response.text)
