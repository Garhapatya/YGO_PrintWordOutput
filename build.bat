pyinstaller --icon="resource/L.ico"^
            --onefile^
            --windowed^
            --name=YgoPDC^
            --add-data ".\resource:resource"^
            --add-data ".\DIY:DIY"^
            --add-data ".\config.txt:."^
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