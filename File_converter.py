# PyQt Imports
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QComboBox,QFileDialog,QLabel,QProgressBar,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import uic

from PIL import Image
from time import sleep,perf_counter
from pathlib import Path
from pdf2image import convert_from_path
from urllib.request import urlopen,urlretrieve
import os,webbrowser,threading,subprocess

# Variables
File_Converter_Setup_Url='https://github.com/elitefantasy/File-Converter/raw/main/setup/File_Converter_Setup.exe'
versionUrl='https://raw.githubusercontent.com/elitefantasy/File-Converter/main/Version.txt'
Poppler_Path='poppler-22.04.0\\bin'
USERNAME=os.getlogin()
downloadFold_path=str(os.path.join(Path.home(),"Downloads"))

# making File Converter Folder
Path(f"{downloadFold_path}\\File Converter").mkdir(parents=True, exist_ok=True)

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
        
        self.comboBox_to=self.findChild(QComboBox,'comboBox_to')
        
        self.label_update_type_desc=self.findChild(QLabel,'label_update_type_desc')
        
        self.Convert_btn=self.findChild(QPushButton,'Convert_btn')
        self.Convert_btn.clicked.connect(self.Convert_File)
        
        self.label_versionInfo=self.findChild(QLabel,'label_versionInfo')
        
        self.label_status=self.findChild(QLabel,'label_status')
        
        self.Open_Folder_btn=self.findChild(QPushButton,'Open_Folder_btn')
        self.Open_Folder_btn.clicked.connect(self.open_downloads_folder)
        
        self.Github_btn=self.findChild(QPushButton,'Github_btn')
        self.Github_btn.clicked.connect(lambda:webbrowser.open('https://github.com/elitefantasy/File-Converter'))
        
        self.label_selectedFile=self.findChild(QLabel,'label_selectedFile')
        
        self.Clear_btn=self.findChild(QPushButton,'Clear_btn')
        self.Clear_btn.clicked.connect(self.clear_func)
        
        self.cloudconvert_btn=self.findChild(QPushButton,'cloudconvert_btn')
        self.cloudconvert_btn.clicked.connect(lambda:webbrowser.open('https://cloudconvert.com/'))
        
        self.pixlr_btn=self.findChild(QPushButton,'pixlr_btn')
        self.pixlr_btn.clicked.connect(lambda:webbrowser.open('https://pixlr.com/x/'))
        
        self.flaticon_btn=self.findChild(QPushButton,'flaticon_btn')
        self.flaticon_btn.clicked.connect(lambda:webbrowser.open('https://www.flaticon.com/icons'))
        
        self.checkUpdate_btn=self.findChild(QPushButton,'checkUpdate_btn')
        self.checkUpdate_btn.clicked.connect(self.updateapp)
        
        self.progressBar=self.findChild(QProgressBar,'progressBar')
        self.progressBar.setHidden(True)
    
    # function to download files with progress bar
    def Handle_Progress(self, blocknum, blocksize, totalsize):
        ## calculate the progress
        readed_data = blocknum * blocksize
        if totalsize > 0:
            download_percentage = int(readed_data * 100 / totalsize)
            self.label_status.setText("Status:🔽Downloading File_Converter_Setup.exe")
            self.progressBar.setHidden(False)
            self.progressBar.setValue(download_percentage)
            QApplication.processEvents()
            self.label_status.setText("Status:✅File_Converter_Setup.exe Succefully downloaded")
            self.progressBar.setHidden(True)
            
        
    
    def updateapp(self):
        print("Checking for Updates")
        update=False
        versionSource=open('Version.txt','r')
        versionContents=versionSource.readline()
        
        # get newest version
        updateSource=urlopen(versionUrl)
        updateContents=updateSource.readline().decode('utf-8')
        # only version number
        updateversion=urlopen(versionUrl).readline().decode('utf-8').replace("Version","").replace("(current)","")
        if updateContents != versionContents:
            update =True
            # checking file size of setup
            file=urlopen(File_Converter_Setup_Url)
            fileSizeByte=int(file.length)
            fileSizeMb=str(int(fileSizeByte/1048576))
            
            # showing the message box
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Check App Update")
            msg.setText("New Version is Available: "+updateversion+"\nDo You want To Download(file size: "+fileSizeMb+" ) The Update")
            print("Updates are available")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    
            
            retval=msg.exec_()
            if retval==1024:
                down_url =File_Converter_Setup_Url
                save_loc = f'C:/Users/{USERNAME}/Desktop/File_Converter_Setup.exe'
                urlretrieve(down_url,save_loc, self.Handle_Progress)
                proc = subprocess.Popen([save_loc], shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)
        
        if update == False:
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Check App Update")
            msg.setText("You are already running latest version: "+updateversion)
            msg.exec_()
    
    def clear_func(self):
        global filepath
        global filename
        self.label_selectedFile.setText("Selected File😴:")
        filepath=""
        filename=""
        
    def open_downloads_folder(self):
        if os.path.exists(f'{downloadFold_path}\\File Converter'):
            webbrowser.open(f'{downloadFold_path}\\File Converter')
        else:
            # print("download folder was deleted")
            Path(f"{downloadFold_path}\\File Converter").mkdir(parents=True, exist_ok=True)
            webbrowser.open(f'{downloadFold_path}\\File Converter')
    
    def update_desc_label(self):
        if self.comboBox_convert.currentText()=='PNG':
            self.label_update_type_desc.setText(PNG_Desc)
        elif self.comboBox_convert.currentText()=='ICO':
            self.label_update_type_desc.setText(ICO_desc)
        elif self.comboBox_convert.currentText()=='PDF':
            self.label_update_type_desc.setText(PDF_Desc)
        elif self.comboBox_convert.currentText()=='JPG':
            self.label_update_type_desc.setText(JPEG_Desc)
        elif self.comboBox_convert.currentText()=='JPEG':
            self.label_update_type_desc.setText(JPEG_Desc)
    
    def open_file_dialog(self):
        global filepath
        global filename
        self.label_status.setText("Status:😊")
        options=QFileDialog.Options()
        filepath,_=QFileDialog.getOpenFileNames(self,"Select File to Convert","","all supported(*.png *.ico *.jpg *.pdf *.jpeg);;jpeg file(*.jpeg);;pdf file (*.pdf);;png file(*.png);;ico file(*.ico);;jpg file(*.jpg);;All Files(*)",options=options)
        
        try:
            #Extracting full filepath from the list(filepath)
            filepath=filepath[-1]
            # extracting filename from filepath
            filename=os.path.basename(filepath)
            #updating selected file label
            self.label_selectedFile.setText("Selected File😶:"+filename)
            # getting extension name (.ext)
            fileExt=os.path.splitext(filepath)[1]
            # making ext name big
            CapExtName=fileExt.upper().replace('.',"")
            # print("capital Ext Name: "+CapExtName)
            
            # adding extension name into comboBox_convert
            self.comboBox_convert.clear()
            self.comboBox_convert.addItem(CapExtName)
            
            # show possible conversion types for selected filetype
            if CapExtName in ('PNG','ICO','JPG','PDF','JPEG'): # create list each time
                # create a new list each time dialog is called
                conversion_type_list=["PNG","ICO","JPG","PDF","JPEG"] # create a list
                # List of possible conversions for selected file
                if CapExtName in ('PDF'):
                    unwantedExt={CapExtName,'ICO'}
                    conversion_type_list=[ele for ele in conversion_type_list if ele not in unwantedExt]
                elif CapExtName in ('PNG','JPG','JPEG'):
                    unwantedExt={CapExtName}
                    conversion_type_list=[ele for ele in conversion_type_list if ele not in unwantedExt]
                elif CapExtName in ('ICO'):
                    unwantedExt={CapExtName,'PDF'}
                    conversion_type_list=[ele for ele in conversion_type_list if ele not in unwantedExt]
                # show possible conversion types in combobox_to
                self.comboBox_to.clear()
                self.comboBox_to.addItems(conversion_type_list)
            # elif CapExtName in ('PDF'): # for document types
            #     conversion_type_list=['PNG',"JPG","JPEG","PDF"]
            
            # Updating Description area
            self.update_desc_label()
            
        except IndexError:
            # print("User did not selected any file")
            self.label_status.setText("Status:🙄User did not selected any file")

    def Convert_File(self):
        # Convert File
            try:
                if filename!="":
                    Path(f"{downloadFold_path}\\File Converter").mkdir(parents=True, exist_ok=True)
                    start_time = perf_counter()
                    self.label_status.setText("Status:🧐Converting "+filename)
                    QApplication.processEvents()
                    sleep(1.0)
                    # .extensions name for "to" and "from"
                    convert_to_type=self.comboBox_to.currentText().lower()
                    print("Converto to type is: "+convert_to_type)
                    convert_from_type=self.comboBox_convert.currentText().lower()
                    
                    # new filename after conversion
                    converted_filename=os.path.basename(filepath).replace(f'{convert_from_type}',f'{convert_to_type}')
                    # print("after conversion filename is: "+converted_filename)
                    
                    # convert file
                    if convert_from_type in ('pdf'): # pdf to image
                        def convert_pdf_to_images():
                            convert_pdf_to_images_status=""
                            images = convert_from_path(filepath,poppler_path=Poppler_Path)
                            for index, image in enumerate(images):
                                self.label_status.setText(f"Status:🥳 {index} of {filename} is being saved")
                                QApplication.processEvents()
                                image.save(f'{downloadFold_path}\\File Converter\\pdf output\\{index}-{converted_filename}')
                            convert_pdf_to_images_status="Done"
                            if convert_pdf_to_images_status=="Done":
                                end_time = perf_counter()
                                self.label_status.setText(f"Status:🥳 {filename} succesfully converted in {end_time-start_time:0.2f} second(s)")
                                QApplication.processEvents()
                        thread_convert_pdf_to_images=threading.Thread(target=convert_pdf_to_images)
                        thread_convert_pdf_to_images.start()
                    elif convert_from_type in ('jpg','png','jpeg') and convert_to_type=='pdf': # image to pdf
                        image = Image.open(filepath)
                        im_1 = image.convert('RGB')
                        im_1.save(f'{downloadFold_path}\File Converter\{converted_filename}')
                        end_time = perf_counter()
                        self.label_status.setText(f"Status:🥳 {filename} succesfully converted in {end_time-start_time:0.2f} second(s)")
                    elif convert_to_type in ('jpg','jpeg'):
                        try:
                            print("checking in jpg,jpeg")
                            im = Image.open(filepath)
                            bg = Image.new("RGB", im.size, (255,255,255))
                            bg.paste(im,im)
                            bg.save(f'{downloadFold_path}\File Converter\{converted_filename}')
                            end_time = perf_counter()
                            self.label_status.setText(f"Status:🥳 {filename} succesfully converted in {end_time-start_time:0.2f} second(s)")
                        except:
                            print("trying different method")
                            im = Image.open(filepath)
                            rgb_im = im.convert('RGB')
                            rgb_im.save(f'{downloadFold_path}\File Converter\{converted_filename}')
                            end_time = perf_counter()
                            self.label_status.setText(f"Status:🥳 {filename} succesfully converted in {end_time-start_time:0.2f} second(s)")
                                
                    else: # image to image type
                        img = Image.open(filepath)
                        img.save(f'{downloadFold_path}\File Converter\{converted_filename}',format = self.comboBox_to.currentText(), sizes=[(32,32)])
                        end_time = perf_counter()
                        self.label_status.setText(f"Status:🥳 {filename} succesfully converted in {end_time-start_time:0.2f} second(s)")
                else:
                    self.label_status.setText("Status:😒Select File To Convert")
            except NameError:
                # print("No File Was Selected")
                self.label_status.setText("Status:😒Select File To Convert")
            except TypeError:
                self.label_status.setText("Status:😭Error!!,perhaps file not selected")
            except AttributeError:
                self.label_status.setText("Status:😒Select File To Convert")
            except:
                print("Some other error occured")
                self.label_status.setText("Status:😭Error!!,perhaps file not selected")
                raise
        


PNG_Desc='PNG or Portable Network Graphic format is a graphic file format that uses lossless compression algorithm to store raster images. It uses 2 stage compression methods. It is frequently used as web site images rather than printing as it supports only the RGB color model. So CMYK color images cannot be saved as PNG image.'
ICO_desc='ICO is an image file format that can contains image icons. ICO is used in Microsoft Windows Operating systems to contain the icon files. It typically contains bitmap images. Also ICO files are used in websites as favicon. It supports 24 bit colors images.d'
PDF_Desc='PDF is a document file format that contains text, images, data etc. This document type is Operating System independent. It is an open standard that compresses a document and vector graphics. It can be viewed in web browsers if the PDF plug-in is installed on the browser. '
JPEG_Desc='JPG, also known as JPEG, is a file format that can contain image with 10:1 to 20:1 lossy image compression technique. With the compression technique it can reduce the image size without losing the image quality. So it is widely used in web publishing to reduce the image size maintaining the image quality.'

app=QApplication([])
win=UI()
win.setWindowIcon(QIcon('icons\\convert.png'))
win.show()
app.exec_()