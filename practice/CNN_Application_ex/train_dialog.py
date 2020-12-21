#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes

class Train_Dialog(QtWidgets.QDialog):
    
    def __init__(self, image_data):
        super().__init__()
        self.class_count = len(image_data)
        self.learning_rate = 0
        self.batch = 0
        self.epochs = 0
        self.train_data = []
        self.train_label = []
        self.test_data = []
        self.test_label = []
        self.image_data = image_data
        
        self.setupUI()
        
    def setupUI(self):
        screen_height = ctypes.windll.user32.GetSystemMetrics(1)
        self.dialog_height = screen_height * 0.5
        self.dialog_width = self.dialog_height * 0.7
        self.resize(self.dialog_width, self.dialog_height)
        self.class_label = QtWidgets.QLabel(self)
        self.class_label.setGeometry(QtCore.QRect(self.dialog_width * 0.05, self.dialog_height * 0.05, self.dialog_width * 0.4, self.dialog_height * 0.1))
        self.class_label.setStyleSheet("border-style:solid;\n"
                                      "border-color:black;\n"
                                      "border-width:3px;\n")
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(self.dialog_height/40)
        self.class_label.setFont(font)
        self.class_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.class_edit = QtWidgets.QLineEdit(self)
        self.class_edit.setGeometry(QtCore.QRect(self.dialog_width * 0.55, self.dialog_height * 0.05, self.dialog_width * 0.4, self.dialog_height * 0.1))
        self.class_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.class_edit.setFont(font)
        self.class_edit.setReadOnly(True)
        
        self.learning_rate_label = QtWidgets.QLabel(self)
        self.learning_rate_label.setGeometry(QtCore.QRect(self.dialog_width * 0.05, self.dialog_height * 0.2, self.dialog_width * 0.4, self.dialog_height * 0.1))
        self.learning_rate_label.setStyleSheet("border-style:solid;\n"
                                      "border-color:black;\n"
                                      "border-width:3px;\n")
        self.learning_rate_label.setFont(font)
        self.learning_rate_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.learning_rate_edit = QtWidgets.QLineEdit(self)
        self.learning_rate_edit.setGeometry(QtCore.QRect(self.dialog_width * 0.55, self.dialog_height * 0.2, self.dialog_width * 0.4, self.dialog_height * 0.1))
        self.learning_rate_edit.setFont(font)
        self.learning_rate_edit.setAlignment(QtCore.Qt.AlignCenter)
        
        self.batch_label = QtWidgets.QLabel(self)
        self.batch_label.setGeometry(QtCore.QRect(self.dialog_width * 0.05, self.dialog_height * 0.35, self.dialog_width * 0.4, self.dialog_height * 0.1))
        self.batch_label.setStyleSheet("border-style:solid;\n"
                                      "border-color:black;\n"
                                      "border-width:3px;\n")
        self.batch_label.setFont(font)
        self.batch_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.batch_edit = QtWidgets.QLineEdit(self)
        self.batch_edit.setGeometry(QtCore.QRect(self.dialog_width * 0.55, self.dialog_height * 0.35, self.dialog_width * 0.4, self.dialog_height * 0.1))
        self.batch_edit.setFont(font)
        self.batch_edit.setAlignment(QtCore.Qt.AlignCenter)
        
        self.epochs_label = QtWidgets.QLabel(self)
        self.epochs_label.setGeometry(QtCore.QRect(self.dialog_width * 0.05, self.dialog_height * 0.5, self.dialog_width * 0.4, self.dialog_height * 0.1))
        self.epochs_label.setStyleSheet("border-style:solid;\n"
                                      "border-color:black;\n"
                                      "border-width:3px;\n")
        self.epochs_label.setFont(font)
        self.epochs_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.epochs_edit = QtWidgets.QLineEdit(self)
        self.epochs_edit.setGeometry(QtCore.QRect(self.dialog_width * 0.55, self.dialog_height * 0.5, self.dialog_width * 0.4, self.dialog_height * 0.1))
        self.epochs_edit.setFont(font)
        self.epochs_edit.setAlignment(QtCore.Qt.AlignCenter)
        
        self.alam_label = QtWidgets.QLabel(self)
        self.alam_label.setGeometry(QtCore.QRect(self.dialog_width * 0.05, self.dialog_height * 0.65, self.dialog_width * 0.9, self.dialog_height * 0.2))
        self.alam_label.setStyleSheet("border-style:solid;\n"
                                      "border-color:black;\n"
                                      "border-width:3px;\n")
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(self.dialog_height/50)
        self.alam_label.setFont(font)
        self.alam_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.learning_button = QtWidgets.QPushButton(self)
        self.learning_button.setGeometry(QtCore.QRect(self.dialog_width * 0.05, self.dialog_height * 0.88, self.dialog_width * 0.4, self.dialog_height * 0.1))
        self.learning_button.setFont(font)
        
        self.quit_button = QtWidgets.QPushButton(self)
        self.quit_button.setGeometry(QtCore.QRect(self.dialog_width * 0.55, self.dialog_height * 0.88, self.dialog_width * 0.4, self.dialog_height * 0.1))
        self.quit_button.setFont(font)
        
        self.class_label.setText("클래스 수")
        self.class_edit.setText(str(self.class_count))
        self.learning_rate_label.setText("학습률")
        self.learning_rate_edit.setText("0.001")
        self.batch_label.setText("Batch수량")
        self.batch_edit.setText("16")
        self.epochs_label.setText("Epoch수량")
        self.epochs_edit.setText("10")
        self.alam_label.setText("알림판 입니다.")
        self.learning_button.setText("학습시키기")
        self.quit_button.setText("돌아가기")
        
        self.quit_button.clicked.connect(self.quit)
        self.learning_button.clicked.connect(self.start_learning)
        
    def quit(self):
        self.reject()
        
    def start_learning(self):
        try:
            self.learning_rate = float(self.learning_rate_edit.text())
            if self.learning_rate <= 0:
                self.alam_label.setText("학습률은 0보다 커야합니다.")
        except:
            self.alam_label.setText("학습률에는 숫자만 입력 가능합니다.")
        try:
            self.batch = int(self.batch_edit.text())
            if self.batch <= 0:
                self.alam_label.setText("Batch수량은 0보다 커야합니다.")
        except:
            self.alam_label.setText("Batch수량에는 숫자만 입력 가능합니다.")
        try: 
            self.epochs = int(self.epochs_edit.text())
            if self.epochs <= 0:
                self.alam_label.setText("Epoch수량은 0보다 커야합니다.")
        except:
            self.alam_label.setText("Epoch수량에는 숫자만 입력 가능합니다.")
        
        count = 0
        for step in range(len(self.image_data)):
            count = step + 1
            train_count = int(len(self.image_data[step]) * 0.8)
            test_count = len(self.image_data[step]) - train_count
            for train_step in range(train_count):
                self.train_data.append((self.image_data[step][train_step] / 127.0) - 1)
                self.train_label.append(step)
            for test_step in range(test_count):
                self.test_data.append((self.image_data[step][test_step + train_step] / 127.0) - 1)
                self.test_label.append(step)
        self.accept()
                
                
        

