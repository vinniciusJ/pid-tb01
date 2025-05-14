from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt

PRIMARY_COLOR = QColor(51, 101, 255) 
PRIMARY_HOVER_COLOR = QColor(87, 128, 255) 
PRIMARY_PRESSED_COLOR = QColor(48, 76, 159) 
BACKGROUND_COLOR = QColor(13, 21, 32)
TEXT_COLOR = QColor(220, 220, 220)

DROP_ZONE_COLOR = QColor(30, 36, 48)
DROP_ZONE_BORDER_COLOR = PRIMARY_COLOR

def apply_dark_theme(app):
    palette = QPalette()
    palette.setColor(QPalette.Window, BACKGROUND_COLOR)
    palette.setColor(QPalette.WindowText, TEXT_COLOR)
    palette.setColor(QPalette.Base, BACKGROUND_COLOR.darker())
    palette.setColor(QPalette.AlternateBase, BACKGROUND_COLOR)
    palette.setColor(QPalette.ToolTipBase, TEXT_COLOR)
    palette.setColor(QPalette.ToolTipText, TEXT_COLOR)
    palette.setColor(QPalette.Text, TEXT_COLOR)
    palette.setColor(QPalette.Button, PRIMARY_COLOR)
    palette.setColor(QPalette.ButtonText, TEXT_COLOR)
    palette.setColor(QPalette.Highlight, PRIMARY_COLOR)
    palette.setColor(QPalette.HighlightedText, Qt.white)
    app.setPalette(palette)
