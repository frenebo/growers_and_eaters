

from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget
)

from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore


class InterfaceWidget(QWidget):
    def __init__(self, worldwidth, worldheight):
        super().__init__()

        self.worldwidth = worldwidth
        self.worldheight = worldheight

        self.setWindowTitle("Bug World")

        # Vertical layout at top level
        topVLayout = QVBoxLayout()
        # topVWidget  = QWidget()
        self.setLayout(topVLayout)
        # self.setCentralWidget(topVWidget)

        # Canvas
        
        canvasLabel = QLabel()
        canvas = QPixmap(self.worldwidth, self.worldheight)
        canvas.fill(QtCore.Qt.GlobalColor.white)
        canvasLabel.setPixmap(canvas)
        topVLayout.addWidget(canvasLabel)

        # Buttons row
        buttonsRowLayout = QHBoxLayout()
        buttonsRowWidget = QWidget()
        buttonsRowWidget.setLayout(buttonsRowLayout)
        topVLayout.addWidget(buttonsRowWidget)

        # Start button
        self.callbacks_on_start_button = []

        startButton = QPushButton("Start")
        startButton.clicked.connect(self.start_button_pressed)
        buttonsRowLayout.addWidget(startButton)

    def start_button_pressed(self):
        for c in self.callbacks_on_start_button:
            c()
    
    def on_start_button(self, callback):
        self.callbacks_on_start_button.append(callback)

    
    # d