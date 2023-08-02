from sql_data_manage.Module.data_matcher import DataMatcher


def demo():
    txt_file_path_dict = {
        'dat_order':
            '/home/chli/chLi/Sql-Dataset/text/dat_order.txt',
        'dat_order_item':
            '/home/chli/chLi/Sql-Dataset/text/dat_order_item.txt',
    }
    remove_quotes = True
    match_title = 'order_id'
    save_folder_path = '/home/chli/chLi/Sql-Dataset/person/'

    data_matcher = DataMatcher(txt_file_path_dict, remove_quotes)

    print(data_matcher.txt_loader_dict.keys())

    data_matcher.generateMatchDataDictList(match_title, save_folder_path)
    return True
