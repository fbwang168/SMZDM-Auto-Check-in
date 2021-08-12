"""
什么值得买自动签到脚本
@author : 2kjiejie
"""

import requests
import os

class ZDM:
    def __init__(self):
        self.session = requests.session()
        self.session.headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'zhiyou.smzdm.com',
        'Referer': 'https://www.smzdm.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
        }
        # 不能keep alive，不然会被服务器拒绝
        self.session.keep_alive = False

    def load_cookie_str(self, cookies):
        self.session.headers['Cookie'] = cookies

    def checkin(self):
        url = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin'
        msg = self.session.get(url)
        print(msg.content)

if __name__ == '__main__':
    zdmInstance = ZDM()
    # cookies = os.environ["COOKIES"]
    # zdmInstance.load_cookie_str(cookies)
    zdmInstance.load_cookie_str('__ckguid=Wwh3cbKgpWaoPbVFJQrKy76; __jsluid_s=d8ea646bbbc7b81eddbe081467b0031f; device_id=19960827311621411426277566d29d264fcb2d99264a7aa1da7e7bc6ea; homepage_sug=e; r_sort_type=score; footer_floating_layer=0; ad_date=10; ad_json_feed=%7B%7D; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1628584871; _zdmA.vid=*; zdm_qd=%7B%7D; _gid=GA1.2.457506497.1628584876; sess=AT-y3TnvpsYaGV60EK%2FAG3aBIjK4oDzjMlm9b%2FBZoLSBJh2ez4XI2E85P%2FajWlCMGl9VP87ZMBH%2FPFWXTcPJhptdg4IurO%2BJzrwARBn32Bd3fl%2FG45Ugu7uaTT%2F; user=user%3A1781074131%7C1781074131; userId=user:1781074131|1781074131; smzdm_id=1781074131; _dc_gtm_UA-27058866-1=1; _zdmA.uid=ZDMA.lSVren5Dn.1628586439.2419200; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217983a6ea4f77f-08c820b5ed27c4-2363163-1024000-17983a6ea50fe9%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.smzdm.com%2F%22%7D%2C%22%24device_id%22%3A%2217983a6ea4f77f-08c820b5ed27c4-2363163-1024000-17983a6ea50fe9%22%7D; _ga_09SRZM2FDD=GS1.1.1628584870.7.1.1628586438.0; _ga=GA1.2.116003610.1621411426; _gat_UA-27058866-1=1; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1628586440; bannerCounter=%5B%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A3%7D%2C%7B%22number%22%3A2%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%5D; __gads=ID=dfe41af4607f0437:T=1627098958:S=ALNI_Mbsm30VojYm8f9E1NFmhqIQ4d7-jw; amvid=b66a7efa0e9dea46c2d42d9aec51bcab; _zdmA.time=1628586442604.0.https%3A%2F%2Fwww.smzdm.com%2F')
    zdmInstance.checkin()
