#-*-codeing=utf-8 -*-
#@Time :2021/11/30 21:05
#@Author :Csn
#@File:抖音2.0
#@Software:PyCharm

#-*-codeing=utf-8 -*-
#@Time :2021/11/27 23:01
#@Author :Csn
#@File:抖音界面
#@Software:PyCharm

import sys

from PyQt5.QtCore import pyqtSignal
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QPushButton
from PySide2.QtCore import QFile, QThread, Signal
from aip import AipOcr
from bs4 import  BeautifulSoup

import  re #正则表达式
import requests
import time
import requests
import re
import ast
import json
import pprint
import subprocess
from threading import Thread
#from PyQt5.Qt import *

class jiexi_pc(QThread):
    dive_list=Signal(str,str,str,int,dict)

    def run(self):
        self.headers = {
            "X-Argus": "+FT5llXVSaCkCWpbSkokeJ77sKJDGjWb8jH6nvzUot7LDDbLJWWTvZHju4fAqI2iaO/yKmfwXGgnJIQIU4yzkbSPsqOwdMXPkq67KJoLuWAcI4ZcU158OuHSG8aBkrk5uJ9wmhNpSX5wl9sUO5/+TC2kwn10F4LohAO/vCCrzApbTkrkEmSBMLloTtugU6lXOpBOwyGri8Q0o1ZGmgtd2r26qo0i24cPW+1WnbyvyMDB7kgn5oNx+4jsj1EzUr+ONjVcwFJeDnuFpiSEfqk5+2v6",
            "User-Agent": "okhttp/3.10.0.1"

        }
        self.jiexi()
    def jiexi(self):
        data_move={}
        max_cursor = 0
        sp = True
        a=0
        while sp:
            sec_user_id=sec_user_id1
            times = time.time()
            ts = int(times)
            _rticket = int(times * 1000)
            url = "https://aweme.snssdk.com/aweme/v1/aweme/post/?publish_video_strategy_type=2&source=0&user_avatar_shrink=96_96&video_cover_shrink=248_330&" \
                  f"max_cursor={max_cursor}" \
                  f"&sec_user_id={sec_user_id}&" \
                  "count=12&show_live_replay_strategy=1&is_order_flow=0&page_from=2&location_permission=1&" \
                  "os_api=22&device_type=OPPO+R11+Plus&ssmix=a&manifest_version_code=170001&dpi=320&is_guest_mode=0&uuid=351564294346317&app_name=aweme&version_name=17.0.0&" \
                  f"ts={ts}&cpu_support64=false&app_type=normal&appTheme=light&ac=wifi&host_abi=armeabi-v7a&update_version_code=17009900&channel=tengxun_1128_0722&" \
                  f"_rticket={_rticket}&device_platform=android&iid=1592548315891661&version_code=170000&cdid=0db026d7-bb4b-4011-93a3-050156847b8d&os=android&is_android_pad=0&openudid=5f61c42cf0cdc898&device_id=453353939470&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=OPPO&aid=1128&minor_status=0&mcc_mnc=46007"

            req = requests.get(url=url, headers=self.headers)
            # print(req.text)
            if re.findall("暂时没有", req.text):
                sp = False
                print("完成")
            else:


                home_data = json.loads(req.text)
                max_cursor = home_data["max_cursor"]
                #print(max_cursor)
                aweme_list = home_data["aweme_list"]

                for aweme in aweme_list:
                    a = a + 1
                    time.sleep(0.1)
                    name = aweme["author"]["nickname"]
                    desc = aweme["desc"]
                    play = aweme["video"]["play_addr"]["url_list"][0]  # 不带水印
                    play_logo = aweme["video"]["download_addr"]["url_list"][0]  # 带水印
                    #print(desc, name)
                   # data_move[desc]=play_logo
                    data_move[desc] = play

                    self.dive_list[str,str,str,int,dict].emit(name,desc,play,a,data_move)
class pcvideo_down(QThread):
    dive_list1=Signal(str,str,str,int,dict)
    def run(self):
        self.headers = {
            "X-Argus": "+FT5llXVSaCkCWpbSkokeJ77sKJDGjWb8jH6nvzUot7LDDbLJWWTvZHju4fAqI2iaO/yKmfwXGgnJIQIU4yzkbSPsqOwdMXPkq67KJoLuWAcI4ZcU158OuHSG8aBkrk5uJ9wmhNpSX5wl9sUO5/+TC2kwn10F4LohAO/vCCrzApbTkrkEmSBMLloTtugU6lXOpBOwyGri8Q0o1ZGmgtd2r26qo0i24cPW+1WnbyvyMDB7kgn5oNx+4jsj1EzUr+ONjVcwFJeDnuFpiSEfqk5+2v6",
            "User-Agent": "okhttp/3.10.0.1"

        }
        self.jiexi()

    def jiexi(self):
        data_move1 = {}
        max_cursor = 0
        sp = True
        a1 = 0

        sec_user_id = sec_user_id2
        times = time.time()
        ts = int(times)
        _rticket = int(times * 1000)

        url = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=" \
              f"{sec_user_id2}"
        req = requests.get(url=url, headers=self.headers)
        # print(req.text)
        if re.findall("暂时没有", req.text):
            sp = False
            print("完成")
        else:

            home_data = json.loads(req.text)
            time.sleep(0.1)

            # print(desc, name)
            # data_move[desc]=play_logo

            video = home_data["item_list"]
            for list in video:
                stt1 = list["video"]["play_addr"]["url_list"]
                name1 = list["author"]["nickname"]
                desc1 = list["desc"]

                play_logo1 = list["video"]["cover"]["url_list"][0]  # 带水印
                data_move1[desc1] = stt1
                #print(stt)

                self.dive_list1[str, str, str, int, dict].emit(name1, desc1, play_logo1, a1, data_move1)
class video_down(QThread):
    jindu = Signal(int,int)
    def run(self):
        self.headers = {
            "X-Argus": "+FT5llXVSaCkCWpbSkokeJ77sKJDGjWb8jH6nvzUot7LDDbLJWWTvZHju4fAqI2iaO/yKmfwXGgnJIQIU4yzkbSPsqOwdMXPkq67KJoLuWAcI4ZcU158OuHSG8aBkrk5uJ9wmhNpSX5wl9sUO5/+TC2kwn10F4LohAO/vCCrzApbTkrkEmSBMLloTtugU6lXOpBOwyGri8Q0o1ZGmgtd2r26qo0i24cPW+1WnbyvyMDB7kgn5oNx+4jsj1EzUr+ONjVcwFJeDnuFpiSEfqk5+2v6",
            "User-Agent": "okhttp/3.10.0.1"

        }
        self.video_download()
    def video_download(self):
        size=0
        row1=row
        url_name1=url_name
        down_lujing=lujing
        #print(down_url)
        req=requests.get(url=down_url,headers=self.headers,stream=True)
        chunk_size=1024
        content_size=int(req.headers["Content-Length"])
        filepath=down_lujing+"/"+url_name1+".mp4"

        with open(filepath,'wb') as f:
            for data in req.iter_content(chunk_size=chunk_size):
                f.write(data)
                size+=len(data)
                s=int(size/content_size*100)
                self.jindu[int,int].emit(s,row1)
class video_down_pc(QThread):
    jindu = Signal(int,int)
    def run(self):
        self.headers = {
            "X-Argus": "+FT5llXVSaCkCWpbSkokeJ77sKJDGjWb8jH6nvzUot7LDDbLJWWTvZHju4fAqI2iaO/yKmfwXGgnJIQIU4yzkbSPsqOwdMXPkq67KJoLuWAcI4ZcU158OuHSG8aBkrk5uJ9wmhNpSX5wl9sUO5/+TC2kwn10F4LohAO/vCCrzApbTkrkEmSBMLloTtugU6lXOpBOwyGri8Q0o1ZGmgtd2r26qo0i24cPW+1WnbyvyMDB7kgn5oNx+4jsj1EzUr+ONjVcwFJeDnuFpiSEfqk5+2v6",
            "User-Agent": "okhttp/3.10.0.1"

        }
        self.video_download()
    def video_download(self):
        size=0
        row1=row
        url_name1=url_name
        down_lujing=lujing
        #print(down_url1)
        stt1 = ''.join(down_url1)
        req=requests.get(url=stt1,headers=self.headers,stream=True)
        chunk_size=1024
        # content_size=int(req.headers["Content-Length"])
        filepath=down_lujing+"/"+url_name1+".mp4"

        with open(filepath,'wb') as f:
            for data in req.iter_content(chunk_size=chunk_size):
                f.write(data)
                # size+=len(data)
                # s=int(size/content_size*100)
                #self.jindu[int,int].emit(s,row1)


class ui:

    def __init__(self):
        self.app=QApplication(sys.argv)
        self.file=QFile("douyin_main.ui")
        self.file.open(QFile.ReadOnly)

        self.headers={
                    "X-Argus": "+FT5llXVSaCkCWpbSkokeJ77sKJDGjWb8jH6nvzUot7LDDbLJWWTvZHju4fAqI2iaO/yKmfwXGgnJIQIU4yzkbSPsqOwdMXPkq67KJoLuWAcI4ZcU158OuHSG8aBkrk5uJ9wmhNpSX5wl9sUO5/+TC2kwn10F4LohAO/vCCrzApbTkrkEmSBMLloTtugU6lXOpBOwyGri8Q0o1ZGmgtd2r26qo0i24cPW+1WnbyvyMDB7kgn5oNx+4jsj1EzUr+ONjVcwFJeDnuFpiSEfqk5+2v6",
                    "User-Agent": "okhttp/3.10.0.1"

        }


        self.loader=QUiLoader()
        self.win=self.loader.load(self.file)
        #self.win.line.setText('https://www.huya.com/g/4079')
        self.win.PB_kaishi.clicked.connect(self.smain)
        self.win.save_pb.clicked.connect(self.save_path)
        self.win.tableWidget.clicked.connect(self.cellClicked_TBW)
        self.thread1 =jiexi_pc()
        # self.win.pushButton_2.clicked.connect(self.pushButton_2)
        # self.win.pushButton_3.clicked.connect(self.pushButton_3)
        # self.win.pushButton_4.clicked.connect(self.pushButton_4)
        self.win.show()



        sys.exit(self.app.exec_())

    def insert_data(self,name,desc,play,a,data_move):
        #print(name,desc)
        self.video_data=data_move

        self.win.tableWidget.setRowCount(a)
        name1=QTableWidgetItem(name)
        self.win.tableWidget.setItem(a-1,0,name1)
        desc1 = QTableWidgetItem(desc)
        self.win.tableWidget.setItem(a -1, 2, desc1)
        play1 = QTableWidgetItem("下载")
        self.win.tableWidget.setItem(a - 1, 1, play1)
    def insert_data1(self,name1,desc1,play1,a1,data_move1):
        #print(name,desc)
        #self.video_data=data_move
        self.video_data1=data_move1
        self.win.tableWidget.setRowCount(1)
        name1=QTableWidgetItem(name1)
        self.win.tableWidget.setItem(0,0,name1)
        desc1 = QTableWidgetItem(desc1)
        self.win.tableWidget.setItem(0, 2, desc1)
        play1 = QTableWidgetItem("下载")
        self.win.tableWidget.setItem(0, 1, play1)
    def cellClicked_TBW(self):
        global row,url_name,down_url,down_url1
        row=self.win.tableWidget.selectedItems()[0].row()#获取行标
        column = self.win.tableWidget.selectedItems()[0].column()  # 获取列标
        self.contents = self.win.tableWidget.selectedItems()[0].text()  # 获取内容
        if column==2:
            print("播放")
            self.url_logo=self.video_data[self.contents]
            print(self.url_logo)
            self.play_video()
        if self.contents=="下载":
            jiexi_f = self.win.QB_APP.isChecked()
            if jiexi_f:
                url_name=self.win.tableWidget.item(row,column+1).text()
                down_url = self.video_data[url_name]


                # lujing=QFileDialog.getExistingDirectory(self)
                #print(down_url)
                self.thread2 = video_down()
                self.thread2.start()
                self.thread2.jindu.connect(self.jindu_show)
            else:
                url_name = self.win.tableWidget.item(row, column + 1).text()
                down_url1 = self.video_data1[url_name]
                # lujing=QFileDialog.getExistingDirectory(self)
                # print(down_url)
                self.thread4 = video_down_pc()
                self.thread4.start()
                self.thread4.jindu.connect(self.jindu_show1)
        #print(row,column,contents)
    def jindu_show(self,s,row1):
        if s==100:
            jd = QTableWidgetItem("下载完成")
            self.win.tableWidget.setItem(row1, 1, jd)
        else:
            jd = QTableWidgetItem(str(s)+"%")
            self.win.tableWidget.setItem(row1, 1, jd)
    def jindu_show1(self,s,row1):

        jd = QTableWidgetItem("下载完成")
        self.win.tableWidget.setItem(0, 1, jd)

    def play_video(self):
        self.play_window=QWebEngineView()
        self.play_window.setWindowTitle(self.contents)
        self.play_window.resize(600,900)
        self.play_window.load(QtCore.QUrl(self.url_logo))
        self.play_window.show()
    def save_path(self):
        global lujing
        qfile=QFileDialog(self.win)
        lujing=qfile.getExistingDirectory(self.win)
        print(lujing)
    def smain(self):
        #print(123)
        global sec_user_id1,sec_user_id2
        url1 = self.win.E_shuru.text()
        jiexi_f=self.win.QB_APP.isChecked()
        if jiexi_f:

            # url1 = "http://v.douyin.com/RPFkNRY/"
            req1 = requests.get(url=url1, headers=self.headers).url
            # print(req1)

            sec_user_id1 = re.findall("user/(.*?)\?", req1)[0]
            # print(sec_user_id1)
            self.thread1.start()
            # print(sec_user_id)
            self.thread1.dive_list.connect(self.insert_data)
            print("app解析")
        else:
            req1 = requests.get(url=url1, headers=self.headers).url
            print(req1)
            sec_user_id2 = re.findall("video/(.*?)\?", req1)[0]
            #sec_user_id1 = re.findall("https(.*?)复制",req1)[0]
            #sec_user_id1="https"+sec_user_id1
            # print(sec_user_id1)
            self.thread3=pcvideo_down()
            self.thread3.start()
            # print(sec_user_id)
            self.thread3.dive_list1.connect(self.insert_data1)
            print("PC解析")

    # def pushButton(self):
    #     header=self.win.plainTextEdit.toPlainText()
    #     print(type(header))
    #
    #     headers=ast.literal_eval(header)
    #     print(type(headers))
    #     #https://www.bilibili.com/bangumi/play/ep409607
    #     #url=self.win.line.displayText()
    #     url=self.win.line.text()
    #     title=self.win.line_2.text()
    #     print(url)
    #     video =self.video_info(url,title)
    #     self.save(video[0], video[1], video[2])
    #     self.merge_date(title)
    #     QMessageBox.about(self.win,
    #                       '结果',
    #                       '保存成功'
    #                       )
    #
    # def thredget(self,text):
    #     self.win.plainTextEdit.appendPlainText(text)
    # def pushButton_2(self):
    #     # openfile=QFileDialog.getOpenFileName(self.win,'打开图片','','*.jpg *.png')
    #     # print(openfile[0])
    #     # print(type(openfile))
    #     # self.win.line.setText(openfile[0])
    #     text=self.win.line.displayText()
    #
    #
    # def pushButton_3(self):
    #     # headers=self.win.plainTextEdit.toPlainText()
    #     text=self.win.plainTextEdit.toPlainText()
    #     print(text)
    #
    # def pushButton_4(self):
    #     APP_ID = '24699283'
    #     API_KEY = 'cdkqito0IsBxKXmfnbA1hxab'
    #     SECRET_KEY = 'NgHnMsHmkb6leKeLLsNM9OiS4G6QAPY2'
    #
    # def getresponse(self,url):
    #     header =self.win.plainTextEdit.toPlainText()
    #     headers = ast.literal_eval(header)
    #     response = requests.get(url=url, headers=headers)
    #     return response
    # def video_info(self,url,title):
    #     response = self.getresponse(url)
    #     # print(response.text)
    #
    #     # title=re.findall('<h1 title="侦探已死：第3话 这就是唯喵品质！">(.*?)</h1>',response.text)[0]
    #     title = title.replace(' ', '')
    #     # print(title)
    #     html_data = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]
    #     json_data = json.loads(html_data)
    #     audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    #     video_url = json_data['data']['dash']['video'][0]['baseUrl']
    #     video_info = [title, audio_url, video_url]
    #     return video_info
    #     # pprint.pprint(json_data)
    #     # print(html_data)
    #
    # def save(self,title, audio_url, vedio_url):
    #     audio_content = self.getresponse(audio_url).content
    #     vedio_content = self.getresponse(vedio_url).content
    #     with open(title + '.mp3', mode='wb') as f:
    #         f.write(audio_content)
    #     with open(title + '.mp4', mode='wb') as f1:
    #         f1.write(vedio_content)
    #     print('ok')
    #
    # def merge_date(self,video_name):
    #     # ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac -strtict experimental output.mp4
    #     i = 1
    #     print(video_name)
    #     COMMAND = f'ffmpeg -i {video_name}.mp4 -i {video_name}.mp3 -c:v copy -c:a aac -strict experimental {video_name}ou.mp4'
    #     # ffmpeg -i ou.mp4 -i ou.mp3 -c:v copy -c:a aac -strict experimental ou.mp4
    #     print(COMMAND)
    #     # ffmpeg -i 侦探已死：第3话这就是唯喵品质！.mp4 -i 侦探已死：第3话这就是唯喵品质！.mp3 -c:v copy -c:a aac -strict experimental output.mp4
    #     # p=subprocess.Popen(COMMAND, shell=True,encoding='utf-8',cwd=r'F:\代码存储\Python\bilibili')
    #     p = subprocess.Popen(COMMAND, shell=True)
    #     print(p.stderr)
ui()