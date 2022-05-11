from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Transparent Editor")
		self.setWindowOpacity(0.5)

		self.setGeometry(60, 60, 600, 400)

		self.text_box = QPlainTextEdit(self)
		self.text_box.move(10, 10)
		self.tb_width = self.width()
		self.tb_height = self.height()

		self.text_box.resize(self.tb_width, self.tb_height)

		self.show()


	def resizeEvent(self, event):
		self.tb_width = self.width()
		self.tb_height = self.height()

		self.text_box.resize(self.tb_width, self.tb_height)


	def keyPressEvent(self, event):
		if event.key() == Qt.Key_I:
			if event.modifiers() & Qt.ControlModifier:
				cur_opacity = self.windowOpacity()
				self.setWindowOpacity(cur_opacity + 0.05)

		if event.key() == Qt.Key_D:
			if event.modifiers() & Qt.ControlModifier:
				cur_opacity = self.windowOpacity()
				self.setWindowOpacity(cur_opacity - 0.05)


if __name__ == "__main__":
	App = QApplication(sys.argv)

	window = Window()

	sys.exit(App.exec())
