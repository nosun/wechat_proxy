import requests

response = requests.get(
    'https://mp.weixin.qq.com/mp/profile_ext',
    params=[('action', 'getmsg'),
            ('__biz', 'MzI5OTUzMjQ1NQ=='),
            ('f', 'json'),
            ('offset', '10'),
            ('count', '10'),
            ('is_ok', '1'),
            ('scene', ''),
            ('uin', '777'),
            ('key', '777'),
            ('pass_ticket', 'FhveV34Lga+Vd/68dz70uqjC6TsvyiBuvJCgRDiBQ39PHMHS+SS+k/M+WSPqwS3D'),
            ('wxtoken', ''),
            ('appmsg_token', '942_CX018yRw%2F2N0mvPYOpLdzuUhs5WsnVSVaorPUA~~'),
            ('x5', '1'),
            ('f', 'json')],
    headers={'Accept': '*/*',
             'Accept-Encoding': 'gzip, '
                                'deflate',
             'Accept-Language': 'zh-CN,en-US;q=0.8',
             'Connection': 'keep-alive',
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
                       'wxtokenkey=35f34ad5c295278f60dad838db80885a6d7a52d119988ecfff118682da3033c0; '
                       'wxuin=2050863400; '
                       'devicetype=android-25; '
                       'version=26060235; '
                       'lang=zh_CN; '
                       'pass_ticket=FhveV34Lga+Vd/68dz70uqjC6TsvyiBuvJCgRDiBQ39PHMHS+SS+k/M+WSPqwS3D; '
                       'wap_sid2=CKji9tEHEnByNTlNTm1ablRXNGI5X1dDVVZLODZONUc2S0F5VUdldE1fVkNrcExoUFdOczZRMU5ZeXhYNDBRVkFnS29QZmpNVnBoSFdnSEdfUVRwOWdmSm9KOW5HM01VNFZtT0dOS3A1Zlc4bDB6cmtZS3VBd0FBMM3j1NMFOAxAlE4=',
             'Q-Auth': '31045b957cf33acf31e40be2f3e71c5217597676a9729f1b',
             'Q-GUID': '5eb5db0bde0cc30385026afe111b88cb',
             'Q-UA2': 'QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.6.2&TBSVC=43603&CO=BK&COVC=043808&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= '
                      'ONEPLUSA5010 '
                      '&RL=1080*2046&OS=7.1.1&API=25',
             'Referer': 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzI5OTUzMjQ1NQ==&devicetype=android-25&version=26060235&lang=zh_CN&nettype=WIFI&a8scene=7&session_us=gh_41dd018d534f&pass_ticket=FhveV34Lga%2BVd%2F68dz70uqjC6TsvyiBuvJCgRDiBQ39PHMHS%2BSS%2Bk%2FM%2BWSPqwS3D&wx_header=1',
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
             'X-Requested-With': 'XMLHttpRequest'}
)

print(response.text)
