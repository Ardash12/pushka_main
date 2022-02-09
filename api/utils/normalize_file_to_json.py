import json
import pandas as pd

user_rec_filtered_3_days = pd.read_csv('User_rec_filtered_3_days.csv', sep=",")
user_rec_without_filter = pd.read_csv('User_rec_without_filter.csv', sep=",")

user_rec_filtered_3_days_to_json = user_rec_filtered_3_days.to_json('User_rec_filtered_3_days.json', orient="records")
user_rec_without_filter_to_json = user_rec_without_filter.to_json('User_rec_without_filter.json', orient="records")

day3_recs_from_filtered_top_json = {}
day3_recs_from_filtered_events_json = {}
user_rec_without_filter_json = {}

FOLDER = 'rec_files/'


def create_json_day3_recs_from_filtered_top():
    with open('User_rec_filtered_3_days.json', encoding='utf-8') as file1:
        data = json.load(file1)
        for i in data:
            try:
                col1 = i['3day_recs_from_filtered_top']
                removal = col1.replace('[', '').replace(']', '').replace(', ', ',')
                map_object1 = map(int, removal.split(','))
                final1 = list(map_object1)
                # rec_dict1 = {
                #     i['user_bmf']: final1,
                # }
                # day3_recs_from_filtered_top_json.append(rec_dict1)
                day3_recs_from_filtered_top_json[i['user_bmf']] = final1
                # print('rec_dict1', rec_dict1)
            except:
                rec_dict1 = {
                    i['user_bmf']: i['3day_recs_from_filtered_top'],
                }
                # print('rec_dict1', rec_dict1)
                # day3_recs_from_filtered_top_json.append(rec_dict1)
                day3_recs_from_filtered_top_json[i['user_bmf']] = i['3day_recs_from_filtered_top']
        file1.close()

    with open(FOLDER + '3day_recs_from_filtered_top_final.json', 'w') as fp:
        json.dump(day3_recs_from_filtered_top_json, fp)

        fp.close()


def create_json_day3_recs_from_filtered_events():
    with open('User_rec_filtered_3_days.json', encoding='utf-8') as file2:
        data = json.load(file2)
        for i in data:
            try:
                col2 = i['3day_recs_from_filtered_events']
                if col2[1] == ' ':
                    b = (col2[0] + col2[2::])
                else:
                    b = col2
                delete_triple_space = b.replace('   ', ' ')
                avg = delete_triple_space.replace('\n', '').replace('  ', ' ').replace(' ', ',')
                result = avg.replace('[', '').replace(']', '')
                map_object2 = map(int, result.split(','))
                final2 = list(map_object2)
                # rec_dict2 = {
                #     i['user_bmf']: final2,
                # }
                # print('rec_dict2', rec_dict2)
                # day3_recs_from_filtered_events_json.append(rec_dict2)
                day3_recs_from_filtered_events_json[i['user_bmf']] = final2

            except Exception as e:
                print(e)
                # rec_dict2 = {
                #     i['user_bmf']: i['3day_recs_from_filtered_events'],
                # }
                # print('rec_dict2', rec_dict2)
                # day3_recs_from_filtered_events_json.append(rec_dict2)
                day3_recs_from_filtered_events_json[i['user_bmf']] = i['3day_recs_from_filtered_events']

        file2.close()

    with open(FOLDER + '3day_recs_from_filtered_events_final.json', 'w') as fp:
        json.dump(day3_recs_from_filtered_events_json, fp)

        fp.close()


def create_json_user_rec_without_filter():
    with open('User_rec_without_filter.json', encoding='utf-8') as file3:
        data = json.load(file3)
        for i in data:
            try:
                col1 = i['item_id']
                if col1[1] == ' ' and col1[2] == ' ':
                    b = (col1[0] + col1[3::])
                elif col1[1] == ' ':
                    b = (col1[0] + col1[2::])
                else:
                    b = col1
                delete_triple_space = b.replace('   ', ' ')
                avg = delete_triple_space.replace('\n', '').replace('  ', ' ').replace(' ', ',')
                result = avg.replace('[', '').replace(']', '')
                map_object3 = map(int, result.split(','))
                final3 = list(map_object3)
                # rec_dict3 = {
                #     i['user_bmf']: final3,
                # }
                # print('rec_dict3', rec_dict3)
                # user_rec_without_filter_json.append(rec_dict3)
                user_rec_without_filter_json[i['user_bmf']] = final3

            except Exception as e:
                print(e)
                # rec_dict3 = {
                #     i['user_bmf']: i['item_id'],
                # }
                # print('rec_dict3', rec_dict3)
                # user_rec_without_filter_json.append(rec_dict3)
                user_rec_without_filter_json[i['user_bmf']] = i['item_id']

        file3.close()

    with open(FOLDER + 'User_rec_without_filter_final.json', 'w') as fp:
        json.dump(day3_recs_from_filtered_events_json, fp)

        fp.close()


create_json_day3_recs_from_filtered_top()
create_json_day3_recs_from_filtered_events()
create_json_user_rec_without_filter()