from sql_data_manage.Config.info_title import INFO_QUERY_TITLE_LIST
from sql_data_manage.Module.txt_loader import TXTLoader


def demo():
    txt_file_path = "/home/chli/chLi/Sql-Dataset/text/dat_order.txt"
    remove_quotes = True
    query_title_list = INFO_QUERY_TITLE_LIST
    prompt_type = '[TITLE]:[DATA]'
    prompt_multi_line = False
    skip_empty_prompt = True

    txt_loader = TXTLoader(txt_file_path, remove_quotes)

    print(txt_loader.title_list)
    print(len(txt_loader.data_list_list))

    txt_loader.generatePrompt(
        query_title_list, prompt_type, prompt_multi_line, skip_empty_prompt)

    print(len(txt_loader.prompt_list))
    print(txt_loader.prompt_list[0])
    return True
