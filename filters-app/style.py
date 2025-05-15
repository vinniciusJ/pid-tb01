from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt

PRIMARY_COLOR = QColor(51, 101, 255) 
PRIMARY_HOVER_COLOR = QColor(70, 115, 255) 
PRIMARY_PRESSED_COLOR = QColor(32, 61, 144)

BG_COLOR_1 = QColor(13, 21, 32)
BG_COLOR_2 = QColor(22, 29, 40)
BG_COLOR_3 = QColor(30, 36, 48)
TEXT_COLOR = QColor(220, 220, 220)

DROP_ZONE_BORDER_COLOR = PRIMARY_COLOR

def apply_dark_theme(app):
    palette = QPalette()
    palette.setColor(QPalette.Window, BG_COLOR_1)
    palette.setColor(QPalette.WindowText, TEXT_COLOR)
    palette.setColor(QPalette.Base, BG_COLOR_1.darker())
    palette.setColor(QPalette.AlternateBase, BG_COLOR_1)
    palette.setColor(QPalette.ToolTipBase, TEXT_COLOR)
    palette.setColor(QPalette.ToolTipText, TEXT_COLOR)
    palette.setColor(QPalette.Text, TEXT_COLOR)
    palette.setColor(QPalette.Button, PRIMARY_COLOR)
    palette.setColor(QPalette.ButtonText, TEXT_COLOR)
    palette.setColor(QPalette.Highlight, PRIMARY_COLOR)
    palette.setColor(QPalette.HighlightedText, Qt.white)
    app.setPalette(palette)
