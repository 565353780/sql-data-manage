from sql_data_manage.Module.prompt_generator import PromptGenerator


def demo():
    dataset_folder_path = '/home/chli/chLi/Sql-Dataset/person/'

    prompt_generator = PromptGenerator(dataset_folder_path)
    prompt_generator.generatePrompt()
    return True
