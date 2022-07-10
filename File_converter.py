from threading import Thread
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QComboBox,QFileDialog,QLabel
from PyQt5 import uic
from PIL import Image
from time import sleep,perf_counter
from pathlib import Path
import os,webbrowser


# Variables
USERNAME=os.getlogin()
downloadFold_path=str(os.path.join(Path.home(),"Downloads"))

class UI(QWidget):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi('FileConverter_UI.ui',self)
        # Program Startup
        #-----------------------------------------------------------------------------
        versionSource=open('Version.txt','r')
        version=versionSource.readline()
        version=version.replace("Version","").replace("(current)","")
        self.label_versionInfo.setText(u"🐱‍👤Developed by EliteFantasy |🔮Version: "+version.rstrip('\n'))
        print("running Version is: "+version)
        #-----------------------------------------------------------------------------
        
        #define widgets
        self.SelectFile_btn=self.findChild(QPushButton,'SelectFile_btn')
        self.SelectFile_btn.clicked.connect(self.open_file_dialog)
        
        self.comboBox_convert=self.findChild(QComboBox,'comboBox_convert')
        # self.label_update_type_desc.setText(PNG_Desc)
        
        self.comboBox_to=self.findChild(QComboBox,'comboBox_to')
        
        self.label_update_type_desc=self.findChild(QLabel,'label_update_type_desc')
        
        self.Convert_btn=self.findChild(QPushButton,'Convert_btn')
        self.Convert_btn.clicked.connect(self.Convert_File)
        
        self.label_versionInfo=self.findChild(QLabel,'label_versionInfo')
        
        self.label_status=self.findChild(QLabel,'label_status')
        
        self.Open_Folder_btn=self.findChild(QPushButton,'Open_Folder_btn')
        self.Open_Folder_btn.clicked.connect(self.open_downloads_folder)
        
        self.Github_btn=self.findChild(QPushButton,'Github_btn')
        self.Github_btn.clicked.connect(lambda:webbrowser.open())
        
    def open_downloads_folder(self):
        webbrowser.open(downloadFold_path)
    
    def update_desc_label(self):
        if self.comboBox_convert.currentText()=='PNG':
            self.label_update_type_desc.setText(PNG_Desc)
        elif self.comboBox_convert.currentText()=='ICO':
            self.label_update_type_desc.setText(ICO_desc)
    
    def open_file_dialog(self):
        global filepath
        self.label_status.setText("Status:")
        options=QFileDialog.Options()
        filepath,_=QFileDialog.getOpenFileNames(self,"Select File to Convert","","png file(*.png);;ico file(*.ico);;All Files(*)",options=options)
        
        try:
            #Extracting full filepath from the list(filepath)
            filepath=filepath[-1]
            # getting extension name (.ext)
            fileExt=os.path.splitext(filepath)[1]
            # making ext name big
            ExtNameInCap=fileExt.upper().replace('.',"")
            # print("capital Ext Name: "+ExtNameInCap)
            
            # adding extension name into comboBox_convert
            self.comboBox_convert.clear()
            self.comboBox_convert.addItem(ExtNameInCap)
            
            # show possible conversion types for selected filetype
            if ExtNameInCap in ('PNG','ICO'): # more can be added in future
                # List of conversions
                conversion_type_list=["PNG","ICO"]
                conversion_type_list.remove(ExtNameInCap)
                
                # show possible conversion types in combobox_to
                self.comboBox_to.clear()
                self.comboBox_to.addItems(conversion_type_list)
            
            # Updating Description area
            self.update_desc_label()
            
        except IndexError:
            # print("User did not selected any file")
            self.label_status.setText("Status:User did not selected any file")

    def Convert_File(self):
        # Convert File
        try:
            # update statusbar
            filename1=os.path.basename(filepath)

            start_time = perf_counter()
            self.label_status.setText("Status:Converting "+filename1)
            QApplication.processEvents()
            sleep(1.0)
            # .extensions name for "to" and "from"
            convert_to_type=self.comboBox_to.currentText().lower()
            convert_from_type=self.comboBox_convert.currentText().lower()
            
            # new filename after conversion
            filename=os.path.basename(filepath).replace(f'{convert_from_type}',f'{convert_to_type}')
            # print("after conversion filename is: "+filename)
            
            # convert file
            img = Image.open(filepath)
            img.save(f'{downloadFold_path}\{filename}',format = self.comboBox_to.currentText(), sizes=[(32,32)])
            # print("Done")
            
            end_time = perf_counter()
            self.label_status.setText(f"Status: {filename1} succesfully converted in {end_time-start_time:0.2f} second(s)")
            
        except NameError:
            # print("No File Was Selected")
            self.label_status.setText("Status: Error!!,perhaps file not selected")
        except:
            raise
        

PNG_Desc='PNG or Portable Network Graphic format is a graphic file format that uses lossless compression algorithm to store raster images. It uses 2 stage compression methods. It is frequently used as web site images rather than printing as it supports only the RGB color model. So CMYK color images cannot be saved as PNG image.'
ICO_desc='ICO is an image file format that can contains image icons. ICO is used in Microsoft Windows Operating systems to contain the icon files. It typically contains bitmap images. Also ICO files are used in websites as favicon. It supports 24 bit colors images.d'

app=QApplication([])
win=UI()
win.show()
app.exec_()