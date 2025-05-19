import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont
from style import apply_dark_theme
from playground.index import Playground

from PySide6.QtWidgets import QFileDialog

def open_image_dialog():
    dialog = QFileDialog(window, "Selecionar Imagem")
    dialog.setFileMode(QFileDialog.ExistingFile)
    dialog.setNameFilter("Imagens (*.png *.jpg *.jpeg)")

    dialog.resize(1000, 800) 
    
    font = QFont()
    font.setPointSize(14) 
    dialog.setFont(font)

    if dialog.exec():
        selected_files = dialog.selectedFiles()
        if selected_files:
            window.set_image(selected_files[0])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_dark_theme(app)

    window = Playground(choose_image_callback=lambda: open_image_dialog())

    window.setWindowTitle("Filters APP")
    window.resize(2560, 1590)
    window.show()
    sys.exit(app.exec())
