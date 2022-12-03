import csv

# downstairs, jogging, sitting, standing, upstairs, walking

def create_instances(data, t):
    activities = ["Downstairs", "Jogging", "Sitting", "Standing", "Upstairs", "Walking"]
    item = [1, 5]
    with open(data, mode='r') as data:
        with open('data_organized.csv', 'w', encoding='UTF8') as data_organized:
            data_reader = csv.DictReader(data)
            data_reader_list = list(data_reader)
            writter_data_organized = csv.writer(data_organized)

            total_lines = sum(1 for item in data_reader_list)
            begin_in_line = 0
            line_limit = t * 20

            user = data_reader_list[0]["user"]
            act = activities.index(data_reader_list[0]["activity"])

            print("LIMIT:"+str(line_limit)+" // TOTAL:"+str(total_lines))

            while line_limit <= total_lines:
                print("BEGIN:"+str(begin_in_line)+" -> END:"+str(line_limit))
                for i in range(begin_in_line, line_limit):
                    if str(user) != data_reader_list[i]["user"] or str(activities.index(data_reader_list[i]["activity"])) != str(act):
                        if str(user) != data_reader_list[i]["user"]:
                            user = data_reader_list[i]["user"]
                        if str(activities.index(data_reader_list[i]["activity"])) != str(act):
                            act = activities.index(data_reader_list[i]["activity"])

                        writter_data_organized.writerow(item)
                        item = []
                        item.append(str(user))
                        item.append(str(act))

                    item.append(data_reader_list[i]["x-axis"])
                    item.append(data_reader_list[i]["y-axis"])
                    item.append(data_reader_list[i]["z-axis"])

                begin_in_line += 1
                line_limit += 1

create_instances("time_series_data_human_activities.csv", 53680)