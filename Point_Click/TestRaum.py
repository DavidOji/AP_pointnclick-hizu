# Importieren der notwendigen Module aus PyQt6 für UI-Elemente und Ereignisverarbeitung
from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

# Importieren einer benutzerdefinierten Klasse TemplateRoom, die als Basis für diesen spezifischen Raum dient
from TemplateRoom import TemplateRoom


# Definition der Klasse QrCode, die von TemplateRoom erbt
class TestRaum(TemplateRoom):
    def __init__(self, parent=None):
        # Aufruf des Konstruktors der Elternklasse, um die Basisklasseninitialisierung durchzuführen
        super(TestRaum, self).__init__(parent)

        # Verbergen des Exit-Buttons in diesem speziellen Raum
        self.show_exit_button(False)

        # Initialisieren des Raumes mit einem spezifischen Bild
        self.init_room("weis.png")

        # Festlegen der Position und Größe eines UI-Elements, das vermutlich einen Sprechblasenbereich darstellt
        self.offset_balloon_x = 750
        self.offset_balloon_y = 20
        self.offset_balloon_width = 180
        self.offset_balloon_length = 650

        # Festlegen der Position und Größe des "Mundes", möglicherweise für eine Sprechblase
        self.set_offset_mouth(787, 271, 50, 150)

        # Definition der Hitboxen, die interaktive Bereiche repräsentieren, um mit Türen im Raum zu interagieren
        self.hitbox_door_1 = QRect(5, 215, 350, 600)
        self.append_hitbox(self.hitbox_door_1)


        # Eine weitere Hitbox, die eine Schaltfläche für Vorwärts- oder Weiteraktionen darstellt
        self.hitbox_forward = QRect(1270, 150, 100, 25)
        self.append_hitbox(self.hitbox_forward)

        # Interne Zähler, die verwendet werden, um den Dialogfortschritt zu steuern
        self.__counter = 0

        # Eine spezielle Hitbox für ein Easter Egg
        self.hitbox_easter_egg = QRect(740, 410, 35, 35)

        # Initialisieren der Textzeilen, die in der Benutzeroberfläche angezeigt werden
        self.text_line_1 = ""
        self.text_line_2 = "Hallo und herzlich willkommen,"
        self.text_line_3 = "zum Tag der offenen Tür am 16. März 2024"
        self.text_line_4 = "im SBS Herzogenaurach."
        self.text_line_5 = ""
        self.text_line_6 = "                                    weiter"

    # Behandlung von Mausklick-Ereignissen
    def mousePressEvent(self, ev: QMouseEvent) -> None:
        # Aufruf der entsprechenden Methode der Elternklasse
        super(TestRaum, self).mousePressEvent(ev)

        # Abfragen der Mausposition beim Klick
        mouse_pos = ev.pos()

        # Überprüfen, ob der Klick innerhalb der Easter Egg Hitbox erfolgt
        if self.hitbox_easter_egg.contains(mouse_pos):
            # Ändern der Textzeilen, um den Fund des Easter Eggs zu feiern
            self.text_line_1 = ""
            self.text_line_2 = ""
            self.text_line_3 = "GLÜCKWUNSCH!!!"
            self.text_line_4 = "Du hast deine erste Kaffeetasse gefunden."
            self.text_line_5 = ""
            self.text_line_6 = ""

            # Abspielen eines Soundeffekts
            self.play_sound("TemplateRoom.mp3")

            # Aktualisieren des UI, um die Änderungen anzuzeigen
            self.update()

        # Überprüfen, ob eine der Tür-Hitboxen getroffen wurde, um den Raum zu wechseln
        if self.hitbox_door_1.contains(mouse_pos):
            self.stop_player()  # Beendet möglicherweise die Wiedergabe von Animationen oder ähnlichem
            self.new_room.emit("Aula.jpg")  # Signalisiert einen Raumwechsel

        # Fortschreiten des Dialogs durch Klicken auf die Vorwärts-Hitbox
        if self.hitbox_forward.contains(mouse_pos):
            self.__counter += 1  # Erhöhen des Zählers zur Steuerung der Dialogsequenzen
            # Eine Reihe von if-else Bedingungen, um den Text basierend auf dem Wert von __counter zu ändern
            # Ähnlich wie oben für andere Zählerwerte

            # Nach Durchlaufen aller Dialoge, den UI aktualisieren
            self.update()
