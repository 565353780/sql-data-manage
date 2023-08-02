from sql_data_manage.Module.prompt_generator import PromptGenerator


def demo():
    dataset_folder_path = '/home/chli/chLi/Sql-Dataset/person/'
    save_folder_path = '/home/chli/chLi/Sql-Dataset/alpaca_dataset/'
    dataset_file_path = '/home/chli/chLi/Sql-Dataset/train.json'

    prompt_generator = PromptGenerator(dataset_folder_path)
    prompt_generator.generateAllPrompt(save_folder_path, dataset_file_path)
    return True
