import os


class PromptGenerator(object):
    def __init__(self, dataset_folder_path=None):
        self.file_path_list = []

        if dataset_folder_path is not None:
            self.loadDataset(dataset_folder_path)
        return

    def reset(self):
        self.file_path_list = []
        return True

    def loadDataset(self, dataset_folder_path):
        filename_list = os.listdir(dataset_folder_path)

        for filename in filename_list:
            if filename[-5:] != '.json':
                continue

            if filename[-9:] == '_tmp.json':
                continue

            file_path = dataset_folder_path + filename
            self.file_path_list.append(file_path)
        return True

    def generatePrompt(self):
        print(len(self.file_path_list))
        return True
