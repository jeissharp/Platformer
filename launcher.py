import sys
import subprocess
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QFileDialog)
from PyQt5.QtCore import Qt

# ---------- Глобальные переменные ----------
level_path = None
status_label = None

# ---------- Функции обработки ----------
def pick_file():
    global level_path, status_label
    path, _ = QFileDialog.getOpenFileName(None, "Открыть уровень", "", "Excel (*.xlsx)")
    if path:
        level_path = path
        

def launch_game():
    args = [sys.executable, "game.py"]
    if level_path:
        args.append(level_path)
    subprocess.Popen(args)

# ---------- Создание интерфейса ----------
app = QApplication(sys.argv)

win = QWidget()
win.setWindowTitle("Платформер")
win.setFixedSize(360, 200)

layout = QVBoxLayout(win)

title = QLabel("Платформер")
title.setAlignment(Qt.AlignCenter)
layout.addWidget(title)

status_label = QLabel("Выберите Excel-файл с уровнем или запустите встроенный")
status_label.setAlignment(Qt.AlignCenter)
status_label.setWordWrap(True)
layout.addWidget(status_label)

row = QHBoxLayout()
btn_open = QPushButton("Открыть .xlsx")
btn_open.clicked.connect(pick_file)

btn_play = QPushButton("Играть")
btn_play.clicked.connect(launch_game)

row.addWidget(btn_open)
row.addWidget(btn_play)
layout.addLayout(row)

win.show()
sys.exit(app.exec_())