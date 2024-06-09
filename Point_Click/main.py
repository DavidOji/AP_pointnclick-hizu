
import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QSplashScreen

from MainWindow import MainWindow
# All you need is
# https://doc.qt.io/qtforpython/


"""Dieses Hauptskript initialisiert die gesamte Anwendung. Es erstellt eine QApplication-Instanz, 
zeigt ein Splash-Screen mit dem Logo an und startet dann das Hauptfenster der Anwendung (MainWindow). 
Es handelt dabei um die zentrale Steuerungsdatei, die alle anderen Komponenten der Anwendung in Gang setzt."""

app = QApplication(sys.argv)

splash = QSplashScreen(QPixmap("logo.png"))
splash.show()

app.processEvents()

main_window = MainWindow()
splash.finish(main_window)
main_window.show()
sys.exit(app.exec())
