from .interface_widget import InterfaceWidget
from ..simulation.bugworld import BugWorld

from PyQt6.QtWidgets import (
    QMainWindow,
)
from PyQt6 import QtCore

import time

class SimulationThread(QtCore.QThread):
    iteration_done = QtCore.pyqtSignal(object)

    def __init__(self, parent, world):
        super().__init__(parent)
        self.world = world
    
    def run(self):
        while True:
            time.sleep(1)
            self.world.iterate_simulation()
            self.iteration_done.emit(self.world.get_state())


class WorldViewer(QMainWindow):
    def __init__(self, world):
        super().__init__()
        self.world = world
        
        self.interface_widget = InterfaceWidget(self.world.width, self.world.height)
        self.setCentralWidget(self.interface_widget)
        
        self.interface_widget.on_start_button(self.start_sim)
        
        self.simulation_thread = None
    

    def update_window(self):
        raise NotImplementedError()
    
    def on_iteration_ready(self, stuff):
        print(stuff)
    
    def start_sim(self):
        if self.simulation_thread is not None:
            print("Already running simulation")
            return

        self.simulation_thread = SimulationThread(parent=self, world=self.world)
        self.simulation_thread.iteration_done.connect(self.on_iteration_ready)
        self.simulation_thread.start()
    