from sql_data_manage.Module.txt_loader import TXTLoader


def demo():
    txt_file_path = "/home/chli/chLi/Sql-Dataset/text/dat_order.txt"

    txt_loader = TXTLoader(txt_file_path)

    print(txt_loader.title_list)
    print(len(txt_loader.data_list_list))
    return True
