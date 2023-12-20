pyinstaller --icon="resource/L.ico"^
            --onefile^
            --windowed^
            --name=YgoPDO^
            --distpath ./YgoPDC/^
            --hidden-import=tkinter^
            --hidden-import=PIL^
            --hidden-import=doc^
            --hidden-import=requests^
            --hidden-import=io^
            --hidden-import=time^
            --hidden-import=bs4^
            --hidden-import=urllib^
            --hidden-import=re^
            --hidden-import=os^
            --hidden-import=docx^
            --hidden-import=tempfile^
            main.py

xcopy "resource\" "ygoPDC\resource\" /E /I /Y
xcopy "DIY\" "ygoPDC\DIY\" /E /I /Y
xcopy "config.txt" "ygoPDC\" /C /I /Y