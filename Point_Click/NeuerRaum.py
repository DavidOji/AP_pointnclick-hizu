from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent, QPixmap
from PyQt6.QtWidgets import QPushButton, QLabel

from TemplateRoom import TemplateRoom  # Angenommen, diese Klasse existiert bereits


#x: Die X-Koordinate des Widgets im Fenster (von links nach rechts).
#y: Die Y-Koordinate des Widgets im Fenster (von oben nach unten).
#width: Die Breite des Widgets.
#height: Die Höhe des Widgets.

class NeuerRaum(TemplateRoom):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_room("gemstone.jpg")
        self.offset_balloon_x = int((1440 - 500) / 2)
        self.offset_balloon_y = 25
        self.set_offset_mouth(self.offset_balloon_x + self.offset_balloon_length, self.offset_balloon_y +
                              self.offset_balloon_width, 0, 0)




        self.mp3_button = QPushButton("Play MP3", self)
        self.mp3_button.setGeometry(600, 400, 150, 50)  # Angenommene Position und Größe
        self.mp3_button.clicked.connect(self.play_mp3_file)  # Verbindung des Buttons mit der play_mp3_file Funktion


        # Label erstellen, das das Bild enthält
        self.image_label = QLabel(self)
        self.pixmap = QPixmap('QR-Code.png')  # Pfad zu deinem Bild
        self.image_label.setPixmap(self.pixmap)
        self.image_label.setGeometry(400, 300, 200, 40)
        self.image_label.setScaledContents(True)  # Stellt sicher, dass das Bild skaliert wird, um in das Label zu passen
        self.image_label.resize(300, 200)  # Größe des Labels anpassen

        # Button erstellen, der die Sichtbarkeit des Labels steuert
        self.toggle_button = QPushButton("Bild anzeigen/verstecken", self)
        self.toggle_button.clicked.connect(self.toggle_image_visibility)

    def toggle_image_visibility(self):
        # Wechselt die Sichtbarkeit des Labels
        self.image_label.setVisible(not self.image_label.isVisible())

    def button_action(self):
        print("Button wurde geklickt")

    def play_mp3_file(self):
        self.play_sound("TemplateRoom.mp3")





