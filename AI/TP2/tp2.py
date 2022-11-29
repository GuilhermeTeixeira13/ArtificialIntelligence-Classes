import csv

# downstairs, jogging, sitting, standing, upstairs, walking

def create_instances(data, t):
    activities = ["Downstairs", "Jogging", "Sitting", "Standing", "Upstairs", "Walking"]
    user = 1
    act = 5
    item = [1, 5]
    with open(data, mode='r') as data:
        with open('data_organized.csv', 'w', encoding='UTF8') as data_organized:
            data_reader = csv.DictReader(data)
            writter_data_organized = csv.writer(data_organized)

            total_lines = sum(1 for row in data_reader)
            begin_in_line = 2
            line_limit = t * 20

            while(line_limit <= total_lines):
                line_count = begin_in_line
                for i, row in enumerate(data_reader):
                    if i == line_count and line_count != line_limit:
                        if str(user) != row["user"] or str(activities.index(row["activity"])) != str(act):
                            if str(user) != row["user"]:
                                user += 1
                            if str(activities.index(row["activity"])) != str(act):
                                act = activities.index(row["activity"])
                            writter_data_organized.writerow(item)
                            item = []
                            item.append(str(user))
                            item.append(str(act))

                        item.append(row["x-axis"])
                        item.append(row["y-axis"])
                        item.append(row["z-axis"])
                        line_count += 1

                        #Tirar próximas 2 linhas caso seja para guardar a info toda
                        #if line_count == line_limit:
                        #    break
                writter_data_organized.writerow(item)
                begin_in_line += 1
                line_limit += 1

create_instances("time_series_data_human_activities.csv", 1)