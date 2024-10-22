#IMPORTS
import os
import sys
from PySide2 import QtWidgets, QtCore
from maya.OpenMayaUI import MQtUtil
from shiboken2 import wrapInstance

sys.path.append("D:/Documentos/5/Pipeline_TD")
from project_manager import ProjectManager

production_path="D:/Documentos/5/Production_Test"

class ProductionUI(QtWidgets.QDialog):
    def __init__(self):
        super(ProductionUI, self).__init__(parent=wrapInstance(int(MQtUtil.mainWindow()), QtWidgets.QWidget))

        #Set title and default config of the UI
        self.setWindowTitle("Production UI")
        self.setFixedSize(450,690)

        self.prj_manager = ProjectManager(production_path)

        self._create_widgets()
        self._create_main_screen()
        self._create_project_sceen()
        self._connect_project_screen()

    def _create_widgets(self):
        #TITLE
        #Create windows title
        self.title_label=QtWidgets.QLabel("PIPELINE TOOL")
        self.title_label.setStyleSheet("""
            font-size: 20px;
            """)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)

        #Frame lines & separator item
        self.separation_line=QtWidgets.QFrame()
        self.separation_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.separation=QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Expanding)

        #TABS
        #Create main tab widgets
        self.tab_widget=QtWidgets.QTabWidget()

        #Create each tab and widgets
        #Project tab
        self.tab_widget.addTab(QtWidgets.QWidget(), "Project Manager")
        self.project_tab=self.tab_widget.widget(0)

        #Project info and path
        self.production_name_title=QtWidgets.QLabel("PRODUCTION:")
        self.production_name=QtWidgets.QLabel("Production-Test")
        self.production_name.setStyleSheet("""
            font-size: 15px;
            font-weight: bold;
            """)

        self.project_name=QtWidgets.QLabel("Project Name:")
        self.project_name_menu=QtWidgets.QComboBox()

        self.project_path=QtWidgets.QLabel("Project Path:")
        self.project_path_line=QtWidgets.QLineEdit()

        self.new_project_name=QtWidgets.QLineEdit()
        self.new_project_name.setMaximumWidth(170)
        self.create_project_button=QtWidgets.QPushButton("Create default project")
        self.add_folder_button=QtWidgets.QPushButton("Add folders")

        self.window_explorer = QtWidgets.QTreeView()
        self.file_model = QtWidgets.QFileSystemModel()
        self.file_model.setRootPath(production_path)
        self.window_explorer.setModel(self.file_model)
        self.window_explorer.setRootIndex(self.file_model.index(production_path))

        #Folder creation
        self.sequence_label=QtWidgets.QLabel("Sequence:")
        self.shot_label=QtWidgets.QLabel("Shot:")
        self.sequence_line=QtWidgets.QLineEdit()
        self.shot_line=QtWidgets.QLineEdit()

        self.layout_label=QtWidgets.QLabel("Layout")
        self.layout_check=QtWidgets.QCheckBox()
        self.animation_label=QtWidgets.QLabel("Animation")
        self.animation_check=QtWidgets.QCheckBox()
        self.lighting_label=QtWidgets.QLabel("Lighting")
        self.lighting_check=QtWidgets.QCheckBox()
        self.vfx_label=QtWidgets.QLabel("VFX")
        self.vfx_check=QtWidgets.QCheckBox()

        #Assets info and path
        self.asset_path=QtWidgets.QLabel("Assets path:")
        self.asset_path_line=QtWidgets.QLineEdit()
        self.asset_path_button=QtWidgets.QPushButton("Choose path")

        #Create editors tab widget
        self.editor_tab_widget=QtWidgets.QTabWidget()
        self.editor_tab_widget.setTabPosition(QtWidgets.QTabWidget.East)
        self.editor_tab_widget.addTab(QtWidgets.QWidget(), "Asset Editor")
        self.asset_tab=self.editor_tab_widget.widget(0)
        self.editor_tab_widget.addTab(QtWidgets.QWidget(), "Reference Editor")
        self.reference_tab=self.editor_tab_widget.widget(1)

        #Asset tab widgets
        self.asset_log=QtWidgets.QTextEdit("Assets List:")
        self.asset_log.setMaximumHeight(300)
        self.asset_log.setMaximumWidth(200)

        self.import_asset_button=QtWidgets.QPushButton("Import Asset")
        self.save_asset_button=QtWidgets.QPushButton("Save Asset")
        self.delete_asset_button=QtWidgets.QPushButton("Delete Asset")

        #Reference tab widgets
        self.reference_namespace=QtWidgets.QLabel("Namespace:")
        self.reference_namespace_line=QtWidgets.QLineEdit()

        self.reference_log=QtWidgets.QTextEdit("References List:")
        self.reference_log.setMaximumHeight(300)
        self.reference_log.setMaximumWidth(200)

        self.create_reference_button=QtWidgets.QPushButton("Create Reference")
        self.remove_reference_button=QtWidgets.QPushButton("Remove Reference")
        self.reload_reference_button=QtWidgets.QPushButton("Reload Reference")
        self.replace_reference_button=QtWidgets.QPushButton("Replace Reference")

    def _create_main_screen(self):
        #Create main layout and add the tabs
        main_layout=QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.tab_widget)

    def _create_project_sceen(self):
        #Create and add layouts
        project_main_layout=QtWidgets.QVBoxLayout(self.project_tab)

        production_name_layout=QtWidgets.QHBoxLayout()
        production_name_layout.addWidget(self.production_name_title)
        production_name_layout.addWidget(self.production_name)

        project_name_layout=QtWidgets.QHBoxLayout()
        project_name_layout.addWidget(self.project_name)
        project_name_layout.addWidget(self.project_name_menu)

        project_path_layout=QtWidgets.QHBoxLayout()
        project_path_layout.addWidget(self.project_path)
        project_path_layout.addWidget(self.project_path_line)

        project_buttons_layout=QtWidgets.QHBoxLayout()
        project_buttons_layout.addWidget(self.new_project_name)
        project_buttons_layout.addWidget(self.create_project_button)


        logger_layout=QtWidgets.QVBoxLayout()
        logger_layout.addWidget(self.window_explorer)

        folder_creation_layout=QtWidgets.QHBoxLayout()
        folder_creation_layout.addWidget(self.sequence_label)
        folder_creation_layout.addWidget(self.sequence_line)
        folder_creation_layout.addWidget(self.shot_label)
        folder_creation_layout.addWidget(self.shot_line)

        checker_layout=QtWidgets.QHBoxLayout()
        checker_layout.addWidget(self.layout_label)
        checker_layout.addWidget(self.layout_check)
        checker_layout.addWidget(self.animation_label)
        checker_layout.addWidget(self.animation_check)
        checker_layout.addWidget(self.lighting_label)
        checker_layout.addWidget(self.lighting_check)
        checker_layout.addWidget(self.vfx_label)
        checker_layout.addWidget(self.vfx_check)

        add_folder_layout=QtWidgets.QVBoxLayout()
        add_folder_layout.addWidget(self.add_folder_button)
        add_folder_layout.addWidget(self.separation_line)

        asset_layout=QtWidgets.QHBoxLayout()
        asset_layout.addWidget(self.asset_path)
        asset_layout.addWidget(self.asset_path_line)
        asset_layout.addWidget(self.asset_path_button)

        asset_tab_loger_layout=QtWidgets.QVBoxLayout()
        asset_tab_loger_layout.addWidget(self.asset_log)

        asset_buttons_layout=QtWidgets.QVBoxLayout()
        asset_buttons_layout.addWidget(self.import_asset_button)
        asset_buttons_layout.addWidget(self.save_asset_button)
        asset_buttons_layout.addWidget(self.delete_asset_button)

        asset_tab_layout=QtWidgets.QHBoxLayout(self.asset_tab)
        asset_tab_layout.addLayout(asset_tab_loger_layout)
        asset_tab_layout.addLayout(asset_buttons_layout)

        reference_namespace_layout=QtWidgets.QHBoxLayout()
        reference_namespace_layout.addWidget(self.reference_namespace)
        reference_namespace_layout.addWidget(self.reference_namespace_line)

        reference_tab_buttons_layout=QtWidgets.QVBoxLayout()
        reference_tab_buttons_layout.addWidget(self.create_reference_button)
        reference_tab_buttons_layout.addWidget(self.remove_reference_button)
        reference_tab_buttons_layout.addWidget(self.reload_reference_button)
        reference_tab_buttons_layout.addWidget(self.replace_reference_button)

        reference_tab_loger_layout=QtWidgets.QHBoxLayout()
        reference_tab_loger_layout.addWidget(self.reference_log)
        reference_tab_loger_layout.addLayout(reference_tab_buttons_layout)

        reference_tab_layout=QtWidgets.QVBoxLayout(self.reference_tab)
        reference_tab_layout.addLayout(reference_namespace_layout)
        reference_tab_layout.addLayout(reference_tab_loger_layout)

        project_main_layout.addLayout(production_name_layout)
        project_main_layout.addLayout(project_name_layout)
        project_main_layout.addLayout(project_path_layout)
        project_main_layout.addLayout(project_buttons_layout)
        project_main_layout.addLayout(logger_layout)
        project_main_layout.addLayout(folder_creation_layout)
        project_main_layout.addLayout(checker_layout)
        project_main_layout.addLayout(add_folder_layout)
        project_main_layout.addLayout(asset_layout)
        project_main_layout.addWidget(self.editor_tab_widget)

    def _connect_project_screen(self):
        file_list=self.prj_manager.search_files()
        self.project_name_menu.clear()
        for i, folder in enumerate(file_list):
            if i == 0:
                self.project_name_menu.addItem("")
            else:
                self.project_name_menu.addItem(os.path.basename(folder))

        self.project_name_menu.currentIndexChanged.connect(lambda: self.project_path_line.setText(self.prj_manager.update_project_path(self.project_name_menu)))
        self.create_project_button.clicked.connect(lambda: self.prj_manager.create_default_project(production_path,self.new_project_name.text()))


if __name__ == "__main__":
    try:
        window.close()
        window = None

    except:
        pass

    window = ProductionUI()
    window.show()