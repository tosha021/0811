import requests
import pprint
import pandas as pd


BASE_URL = 'https://akabab.github.io/superhero-api/api'
ALL_API = '/all.json'
URL_FULL_GET = BASE_URL + ALL_API
res = requests.get(URL_FULL_GET)
res_text = res.json()


full_name_biography_data_list =[]
id_data_list = []
for res_data in res_text:
    id_data = res_data['id']
    full_name_biography_data = res_data['biography']['fullName']

    full_name_biography_data_list.append(full_name_biography_data)
    id_data_list.append(id_data)

# full_id_ferst_name_data = dict(zip(id_data_list, full_name_biography_data_list))

full_df_id_name = {
    'ID': id_data_list,
    'Имя': full_name_biography_data_list
}
df = pd.DataFrame(full_df_id_name)
df.to_excel('C:/Users/tosha021/PycharmProjects/0811/id_name.xlsx')


# if full_name_biography_data_list == id_data_list

    # pprint.pprint(full_name_biography_data)
# pprint.pprint(full_name_biography_data_list)
# pprint.pprint(id_data_list)
# pprint.pprint(len(full_name_biography_data_list))
# pprint.pprint(len(id_data_list))
#
# # pprint.pprint(res_data)
# # pprint.pprint(len(res_text))
# # print(type(res_text))
# #
# #
