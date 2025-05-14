import sys
from PySide6.QtWidgets import QApplication
from style import apply_dark_theme
from playground import Playground

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_dark_theme(app)

    def on_image_selected(image_path):
        window.set_image(image_path)

    window = Playground(next_page_callback=None, choose_image_callback=lambda: open_image_dialog())

    def open_image_dialog():
        from PySide6.QtWidgets import QFileDialog
        file_path, _ = QFileDialog.getOpenFileName(window, "Selecionar Imagem", "", "Imagens (*.png *.jpg *.jpeg)")
        if file_path:
            window.set_image(file_path)

    window.setWindowTitle("Filters APP")
    window.resize(1000, 700)
    window.show()
    sys.exit(app.exec())
