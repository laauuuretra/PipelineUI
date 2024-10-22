import os
import maya.cmds as mc

class ProjectManager(object):
    def __init__(self, production_path):
        self.main_path=production_path

    def search_files(self):
        project_folder=[""]

        if os.path.exists(self.main_path) and os.path.isdir(self.main_path):
            for i in os.listdir(self.main_path):
                item_path=os.path.join(self.main_path, i)

                if os.path.isdir(item_path):
                    project_folder.append(item_path)

        return project_folder

    def update_project_path(self, project_name_menu):
        selected_project=project_name_menu.currentText()
        project_path=""
        if selected_project:
            project_path=os.path.join(self.main_path,selected_project)

        return project_path

    def create_default_project(self, project_path, project_name):
        folders = {
            "assets": {},
            "autosave": {},
            "cache": {
                "nCache": {
                    "fluid": {}
                },
                "particles": {}
            },
            "clips": {},
            "data": {},
            "images": {},
            "movies": {},
            "renderData": {
                "depth": {},
                "fur": {
                    "furAttrMap": {},
                    "furEqualMap": {},
                    "furFiles": {},
                    "furImages": {},
                    "furShadowMap": {}
                },
                "iprImages": {},
                "shaders": {}
            },
            "sceneAssembly": {},
            "scenes": {
                "edits": {}
            },
            "scripts": {},
            "sound": {},
            "sourceimages": {
                "3dPaintTextures": {}
            },
            "Time Editor": {
                "Clip Exports": {}
            }
        }

        directory=os.path.join(project_path, project_name)
        os.makedirs(directory, exist_ok=True)

        for folder, subfolder in folders.items():
            folder_path=os.path.join(directory, folder)
            os.makedirs(folder_path, exist_ok=True)
        mc.workspace(directory=directory)
        mc.workspace(directory, newWorkspace=True)
        mc.workspace(saveWorkspace=True)
        for folder, subfolder in folders.items():
            mc.workspace(fileRule=[folder, directory])