import os,subprocess
USERNAME=os.getlogin()
command=f"C:\\Users\\{USERNAME}\\Desktop\\File_Converter_Setup.exe"
print(command)
subprocess.run(f"C:\\Users\\{USERNAME}\\Desktop\\File_Converter_Setup.exe")