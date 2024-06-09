from PyQt6.QtCore import QRect, Qt, QDateTime, QTimer
from PyQt6.QtGui import QMouseEvent, QPixmap
from PyQt6.QtWidgets import QLabel, QPushButton

# Importieren einer benutzerdefinierten Klasse TemplateRoom, die als Basis für diesen spezifischen Raum dient
from TemplateRoom import TemplateRoom

# Definition der Klasse Hinzufügen, die von TemplateRoom erbt
class Hinzufügen(TemplateRoom):
    def __init__(self, parent=None):
        # Aufruf des Konstruktors der Elternklasse, um die Basisklasseninitialisierung durchzuführen
        super(Hinzufügen, self).__init__(parent)

        # Verbergen des Exit-Buttons in diesem speziellen Raum
        self.show_exit_button(False)

        # Initialisieren des Raumes mit einem spezifischen Bild
        self.init_room("stars.jpg")

        # Muss mit EINGEFÜGT werden
        self.offset_balloon_x = int((1440 - 500) / 2)
        self.offset_balloon_y = 25
        self.set_offset_mouth(self.offset_balloon_x + self.offset_balloon_length, self.offset_balloon_y +
                              self.offset_balloon_width, 0, 0)

        # Datum- und Uhrzeit-Label hinzufügen
        self.datetime_label = QLabel(self)
        self.datetime_label.setGeometry(600, 50, 200, 40)  # Position und Größe des Labels
        self.datetime_label.setStyleSheet("background-color: lightgray; color: black; font-size: 16px;")

        # Timer für das Aktualisieren des Labels
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)  # Timer wird alle 1000 Millisekunden (1 Sekunde) ausgelöst

        # Sofortiges Update, um das aktuelle Datum und die Uhrzeit beim Start anzuzeigen
        self.update_datetime()

        # Label erstellen, das das Bild enthält
        self.image_label = QLabel(self)
        self.pixmap = QPixmap('QR-Code.png')  # Pfad zu deinem Bild
        self.image_label.setPixmap(self.pixmap)
        self.image_label.setGeometry(400, 300, 200, 40)
        self.image_label.setScaledContents(
            True)  # Stellt sicher, dass das Bild skaliert wird, um in das Label zu passen
        self.image_label.resize(100, 50)  # Größe des Labels anpassen

        # Button erstellen, der die Sichtbarkeit des Labels steuert
        self.toggle_button = QPushButton("Bild anzeigen/verstecken", self)
        self.toggle_button.clicked.connect(self.toggle_image_visibility)

    def toggle_image_visibility(self):
        # Wechselt die Sichtbarkeit des Labels
        self.image_label.setVisible(not self.image_label.isVisible())

    def update_datetime(self):
        # Aktuelles Datum und Uhrzeit abrufen und im Label anzeigen
        current_datetime = QDateTime.currentDateTime().toString("dd.MM.yyyy hh:mm:ss")
        self.datetime_label.setText(current_datetime)
