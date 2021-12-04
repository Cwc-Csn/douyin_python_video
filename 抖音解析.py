#-*-codeing=utf-8 -*-
#@Time :2021/11/26 20:51
#@Author :Csn
#@File:抖音解析
#@Software:PyCharm
import random

import requests
import re
import time
import json

#https://v.douyin.com/RpMQ9uL/
#解析单个视频
st="4.33 ATL:/ 弓毛终结者完整版%%音乐现场 %%演出现场  %%大提琴  %%小提琴 @抖音小助手  %%创作灵感 %%嗨翻全场 %%酒吧  https://v.douyin.com/RpMQ9uL/ 复制此链接，打开Dou音搜索，直接观看视频！"
s=re.findall("https(.*?)复制",st)[0]
s="https"+s
#print(s)
headers={
"X-Argus":""   ,
"User-Agent":"okhttp/3.10.0.1"
}

# url1="https://v.douyin.com/RbwDoNB/"
#url1=" https://v.douyin.com/RpM2MFK/ "
req1=requests.get(url=s,headers=headers).url
#print(req1)
sec_user_id=re.findall("video/(.*?)\?",req1)[0]
#print(sec_user_id)
times=time.time()
ts=int(times)
_rticket=int(times*1000)

url="https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=" \
    f"{sec_user_id}"
# url="https://aweme.snssdk.com/aweme/v1/aweme/detail/?" \
#     f"aweme_id={sec_user_id}&origin_type=link&request_source=0&is_story=0&location_permission=1&recommend_collect_feedback=0&os_api=22&device_type=OPPO+R11+Plus&ssmix=a&manifest_version_code=170001&dpi=320&is_guest_mode=0&uuid=351564294346317&app_name=aweme&version_name=17.0.0&" \
#     f"ts={ts}&cpu_support64=false&app_type=normal&appTheme=light&ac=wifi&host_abi=armeabi-v7a&update_version_code=17009900&channel=tengxun_1128_0722&" \
#     f"_rticket={_rticket}&device_platform=android&iid=1592548315891661&version_code=170000&cdid=0db026d7-bb4b-4011-93a3-050156847b8d&os=android&is_android_pad=0&openudid=5f61c42cf0cdc898&device_id=453353939470&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=OPPO&aid=1128&minor_status=0&mcc_mnc=46007"
req=requests.get(url=url,headers=headers).text
#print(req)
home_data = json.loads(req)
#print(req)
video=home_data["item_list"]
for list in video:
    stt=list["video"]["play_addr"]["url_list"]
    print(type(stt))
    stt1=''.join(stt)
    print(stt1)
    url_name1 = list["author"]["nickname"]
    req = requests.get(url=stt1, headers=headers, stream=True)

    filepath = url_name1 + ".mp4"

    with open(filepath, 'wb') as f:
        for data in req.iter_content():
            f.write(data)
    #print(stt)
#["video"]["play_addr"]["uri"][0]
#print(video)

# # 解析主页
# headers={
# # "Accept-Encoding":"gzip",
# # "x-tt-dt":"AAA67BBXK3G6YJ4JSWLZSY4X3TLPQRSTWSXGD3OCPT732RA5USFFLHZWI67C3CG35TFTPXUL2R5FZAOO7O3GAXXTXYTOTIGGXVT7KER2O742UE4H6IV2LVQWARO5NSWUTL3WVYK4FUIRK3BPRRAHCVI",
# # "activity_now_client":"1637932062402",
# # "passport-sdk-version":"20353",
# # "sdk-version":"2",
# # "X-SS-REQ-TICKET":"1637932061806",
# # "x-vc-bdturing-sdk-version":"2.2.0.cn",
# # "Cookie":"install_id=1592548315891661; ttreq=1$153007bee5f8689e7beefc9505af60d1f2b4cb31; odin_tt=836ded8fb73b5a5057fe636375f9e654c9c4f8fc82b6d18ee108343e9e891c1a76126ec2bee60649fd25ffa0274f60f626622f80322460d7944a7f334f40f7ff398a0712396a776311ef1cd0b6fc499c",
# # "X-Ladon":"PE/FM5whMERmtIdNDbKyYrMETuTl0cUNDf24MAUR0eQVfIOr",
# # "X-Khronos":"1637932061",
# # "X-Gorgon":"040400240000f32ad8b91ccb3463b43494c45b45e536308f9179",
# "X-Argus":"+FT5llXVSaCkCWpbSkokeJ77sKJDGjWb8jH6nvzUot7LDDbLJWWTvZHju4fAqI2iaO/yKmfwXGgnJIQIU4yzkbSPsqOwdMXPkq67KJoLuWAcI4ZcU158OuHSG8aBkrk5uJ9wmhNpSX5wl9sUO5/+TC2kwn10F4LohAO/vCCrzApbTkrkEmSBMLloTtugU6lXOpBOwyGri8Q0o1ZGmgtd2r26qo0i24cPW+1WnbyvyMDB7kgn5oNx+4jsj1EzUr+ONjVcwFJeDnuFpiSEfqk5+2v6",
# # "Host":"aweme.snssdk.com",
# # "Connection":"Keep-Alive",
# "User-Agent":"okhttp/3.10.0.1"
#
# }
# times=time.time()
# ts=int(times)
# _rticket=int(times*1000)
#
# url1="http://v.douyin.com/RPFkNRY/"
# req1=requests.get(url=url1,headers=headers).url
# # print(req1)
# sec_user_id=re.findall("user/(.*?)\?",req1)[0]
# # print(sec_user_id)
# max_cursor=0
# sp=True
#
# while sp:
#     banben1 = "os_api=22&device_type=LIO-AN00&ssmix=a&manifest_version_code=170001&dpi=320&is_guest_mode=0&uuid=351564294346317&app_name=aweme&version_name=17.0.0&ts=1638064596&cpu_support64=false&app_type=normal&appTheme=light&ac=wifi&host_abi=armeabi-v7a&update_version_code=17009900&channel=tengxun_1128_0722&_rticket=1638064596336&device_platform=android&iid=1592548315891661&version_code=170000&cdid=0db026d7-bb4b-4011-93a3-050156847b8d&os=android&is_android_pad=0&openudid=5f61c42cf0cdc898&device_id=453353939470&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=HUAWEI&aid=1128&minor_status=0&mcc_mnc=46007"
#     banben2 = "os_api=22&device_type=OPPO+R11+Plus&ssmix=a&manifest_version_code=170001&dpi=320&is_guest_mode=0&uuid=351564294346317&app_name=aweme&version_name=17.0.0&ts=1638012586&cpu_support64=false&app_type=normal&appTheme=light&ac=wifi&host_abi=armeabi-v7a&update_version_code=17009900&channel=tengxun_1128_0722&_rticket=1638012586684&device_platform=android&iid=1592548315891661&version_code=170000&cdid=0db026d7-bb4b-4011-93a3-050156847b8d&os=android&is_android_pad=0&openudid=5f61c42cf0cdc898&device_id=453353939470&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=OPPO&aid=1128&minor_status=0&mcc_mnc=46007"
#     banben3 = "os_api=22&device_type=M2007J22C&ssmix=a&manifest_version_code=170001&dpi=320&is_guest_mode=0&uuid=351564294346317&app_name=aweme&version_name=17.0.0&ts=1638064756&cpu_support64=false&app_type=normal&appTheme=light&ac=wifi&host_abi=armeabi-v7a&update_version_code=17009900&channel=tengxun_1128_0722&_rticket=1638064757376&device_platform=android&iid=1592548315891661&version_code=170000&cdid=0db026d7-bb4b-4011-93a3-050156847b8d&os=android&is_android_pad=0&openudid=5f61c42cf0cdc898&device_id=453353939470&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=Xiaomi&aid=1128&minor_status=0&mcc_mnc=46007"
#     banben_list = [banben1, banben2, banben3]
#     a=random.randint(0,2)
#     banben=banben_list[a]
#     # url = "https://aweme.snssdk.com/aweme/v1/aweme/post/?publish_video_strategy_type=2&source=0&user_avatar_shrink=96_96&video_cover_shrink=248_330&" \
#     #       f"max_cursor={max_cursor}" \
#     #       f"&sec_user_id={sec_user_id}&" \
#     #       "count=12&show_live_replay_strategy=1&is_order_flow=0&page_from=2&location_permission=1&" \
#     #       "os_api=22&device_type=OPPO+R11+Plus&ssmix=a&manifest_version_code=170001&dpi=320&is_guest_mode=0&uuid=351564294346317&app_name=aweme&version_name=17.0.0&" \
#     #       f"ts={ts}&cpu_support64=false&app_type=normal&appTheme=light&ac=wifi&host_abi=armeabi-v7a&update_version_code=17009900&channel=tengxun_1128_0722&" \
#     #       f"_rticket={_rticket}&device_platform=android&iid=1592548315891661&version_code=170000&cdid=0db026d7-bb4b-4011-93a3-050156847b8d&os=android&is_android_pad=0&openudid=5f61c42cf0cdc898&device_id=453353939470&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=OPPO&aid=1128&minor_status=0&mcc_mnc=46007"
#     url = "https://aweme.snssdk.com/aweme/v1/aweme/post/?publish_video_strategy_type=2&source=0&user_avatar_shrink=96_96&video_cover_shrink=248_330&" \
#           f"max_cursor={max_cursor}" \
#           f"&sec_user_id={sec_user_id}&" \
#           "count=12&show_live_replay_strategy=1&is_order_flow=0&page_from=2&location_permission=1&"
#     url=url+banben+"&"+str(ts)+"&"+str(_rticket)
#     #print(url)
#     req = requests.get(url=url, headers=headers)
#     # print(req.text)
#     if re.findall("暂时没有",req.text):
#         sp=False
#         print("完成")
#     else:
#         home_data = json.loads(req.text)
#         max_cursor = home_data["max_cursor"]
#         print(max_cursor)
#         aweme_list = home_data["aweme_list"]
#
#         for aweme in aweme_list:
#             name=aweme["author"]["nickname"]
#             desc = aweme["desc"]
#             play = aweme["video"]["play_addr"]["url_list"][0]  # 不带水印
#             play_logo = aweme["video"]["download_addr"]["url_list"][0]  # 带水印
#             #print(desc, name)
#



