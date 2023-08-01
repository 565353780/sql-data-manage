from sql_data_manage.Module.txt_loader import TXTLoader


def demo():
    txt_file_path = "/home/chli/chLi/Sql-Dataset/text/dat_order.txt"
    remove_quotes = True
    prompt_type = '[TITLE]:[DATA]'
    prompt_multi_line = True
    skip_empty_prompt = True

    txt_loader = TXTLoader(txt_file_path, remove_quotes)

    print(txt_loader.title_list)
    print(len(txt_loader.data_list_list))

    txt_loader.generatePrompt(
        prompt_type, prompt_multi_line, skip_empty_prompt)

    print(len(txt_loader.prompt_list))
    return True
