from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtWidgets import QFileDialog

from ui_view import Ui_FormCompasTimber


class UiMainWindow(QDockWidget, Ui_FormCompasTimber):
    
    def __init__(self, controller):
        super().__init__()
        self._controller = controller
        self.setupUi(self)
        self._init_gui_state()

    def _init_gui_state(self):
        """Inits the gui state."""
        self.pushButton.clicked.connect(self.load_ct_assembly)
        self.pushButton_2.clicked.connect(self.save_ct_assembly)
        self.pushButton_3.clicked.connect(self.select_ct_assembly)
        
    def select_ct_assembly(self):
        # Open file dialog to select a file
        file_dialog = QFileDialog(self)
        file_dialog.setDirectory(
            r"C:\Users\ckasirer\Documents\Projects\COMPAS Timber\240325_SoundingBoard\02_Chen_SWaaEditor")
        filePath, _ = QFileDialog.getOpenFileName(self, 'Select File')
        if filePath:
            self.lineEdit.setText(filePath)

    def load_ct_assembly(self):
        # Import action using the file path
        filePath = self.lineEdit.text()
        self._controller.load_model_from_file(filePath)

    def save_ct_assembly(self):
        # Export action using the file path
        filePath = self.lineEdit.text()
        print(f"Exporting file: {filePath}")
        self._controller.export_model_to_file(filePath)
        