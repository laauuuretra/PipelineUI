import os

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
