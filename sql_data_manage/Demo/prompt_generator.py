from sql_data_manage.Module.prompt_generator import PromptGenerator


def demo():
    dataset_folder_path = '/home/chli/chLi/Sql-Dataset/person/'
    save_folder_path = '/home/chli/chLi/Sql-Dataset/alpaca_test1_dataset/'
    dataset_file_path = '/home/chli/chLi/Sql-Dataset/data_test1.json'
    train_percent = 0.9

    prompt_generator = PromptGenerator(dataset_folder_path)
    prompt_generator.generateAllPrompt(save_folder_path, dataset_file_path)
    prompt_generator.generatePromptDataset(
        save_folder_path, dataset_file_path, train_percent)
    return True


def demo_merge():
    save_folder_path = '/home/chli/chLi/Sql-Dataset/alpaca_test1_dataset/'
    dataset_file_path = '/home/chli/chLi/Sql-Dataset/data_test1.json'
    train_percent = 0.99

    prompt_generator = PromptGenerator()
    prompt_generator.generatePromptDataset(
        save_folder_path, dataset_file_path, train_percent)
    return True
