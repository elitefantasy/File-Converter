# Make sure to run in powershell

Set-Location "E:\3 Programing\Github\File-Converter"

.\venv\Scripts\Activate.ps1

Remove-Item 'dist' -Recurse

pyinstaller --noconfirm --onedir --windowed --icon "E:/3 Programing/Github/File-Converter/icons/convert.ico" --add-data "E:/3 Programing/Github/File-Converter/icons;icons/" --add-data "E:/3 Programing/Github/File-Converter/poppler-22.04.0;poppler-22.04.0/" --add-data "E:/3 Programing/Github/File-Converter/Version.txt;." --add-data "E:/3 Programing/Github/File-Converter/FileConverter_UI.ui;."  "E:/3 Programing/Github/File-Converter/File_converter.py"

Remove-Item 'build' -Recurse
Remove-Item File_converter.spec
& "E:\3 Programing\Github\File-Converter\setup\File_Converter.iss"
# pause