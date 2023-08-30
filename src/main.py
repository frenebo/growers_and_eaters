# from simulation import start_simulation
from scripts.simulation.bugworld import BugWorld
from scripts.view.worldviewer import WorldViewer
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    world = BugWorld()
    world.add_random_growers(20)

    
    app = QApplication([])
    
    viewer = WorldViewer(world)
    
    # window.show()
    viewer.show()

    app.exec()

    # w.start()
    # viewer.run_and_watch()