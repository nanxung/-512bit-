# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_main import Ui_MainWindow
import requests
import re
from PyQt5.QtWidgets import QMessageBox
import os

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.textEdit.setText("比特币交易ID：\n")
        self.label.setText('关于高校比特币病毒 社工破解的可能性尝试\n(来自知乎：https://www.zhihu.com/pin/846570592869183488#comment-280580859)：\n\
    1:打开自己的那个勒索软件界面，点击copy. \n（复制黑客的比特币地址）\n\
    2:把copy粘贴到btc.com （区块链查询器）\n\
    3:在区块链查询器中找到黑客收款地址的交易记录，\n然后随意选择一个txid（交易哈希值）\n\
    4:把txid 复制粘贴给 勒索软件界面按钮connect us.\n\
    5:等黑客看到后 你再点击勒索软件上的check payment. \n\
    6:再点击decrypt 解密文件即可。\n'+
    '我将上面6个步骤封装成GUI破解软件\n'+
    '点击下方破解按钮即可破解\n(本人github：https://github.com/nanxung，\n码云：https://git.oschina.net/nanxun)'
                           )
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.pojie()
        QMessageBox.information(self, "Warning", "破解成功！！！",
                                QMessageBox.Ok)


    def pojie(self):

        btc_list = ['https://btc.com/' + add for add in
                    ['13AM4VW2dhxYgXeQepoHkHSQuy6NgaEb94', '12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw',
                     '115p7UMMngoj1pMvkpHijcRdfJNXj6LrLn']]
        reg = r'class="tx-item-summary-hash">(.*)</a>'
        r_list = [requests.get(btc) for btc in btc_list]
        self.label_2.setText(
            u'请将在列出的比特币交易ID中选择一串，复制粘贴到勒索软件的Contact us,等待黑客验证后，点击check payment再点击Decypt即可恢复\n'+'Please select one transaction ID，and paste it to the Contact us ,after the hacker confirmed,click Chek payment and then click Decrypt\n')
        s=''
        for r in r_list:
            for txid in re.findall(reg, r.text):
                print(txid)
                s+=txid+"\n"

        self.textEdit.setText(s)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = MainWindow()

    ui.show()
    sys.exit(app.exec_())