from sql_data_manage.Module.data_matcher import DataMatcher


def demo():
    txt_file_path_dict = {
        'dat_order':
            '/home/chli/dataset/text/dat_order.txt',
        'dat_order_item':
            '/home/chli/dataset/text/dat_order_item.txt',
    }
    remove_quotes = True
    match_title = 'order_id'

    data_matcher = DataMatcher(txt_file_path_dict, remove_quotes)

    print(data_matcher.txt_loader_dict.keys())

    data_matcher.generatePrompt(match_title)

    print(len(data_matcher.prompt_list))
    return True
