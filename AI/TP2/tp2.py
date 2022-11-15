import csv

# downstairs, jogging, sitting, standing, upstairs, walking

def create_instances(data, t):
    activities = ["Downstairs", "Jogging", "Sitting", "Standing", "Upstairs", "Walking"]
    user = 1
    act = 5
    item = [1, 5]
    line_count = 2
    with open(data, mode='r') as csv_file:
        with open('sorted.csv', 'w', encoding='UTF8') as f:
            csv_reader = csv.DictReader(csv_file)
            writer = csv.writer(f)
            for row in csv_reader:
                if str(user) != row["user"] or str(activities.index(row["activity"])) != str(act):
                    if str(user) != row["user"]:
                        user += 1
                    if str(activities.index(row["activity"])) != str(act):
                        act = activities.index(row["activity"])
                    writer.writerow(item)
                    item = []
                    item.append(str(user))
                    item.append(str(act))
                item.append(row["x-axis"])
                item.append(row["y-axis"])
                item.append(row["z-axis"])
                line_count += 1

                # Tirar próximas 2 linhas caso seja para guardar a info toda
                if line_count == t * 20:
                    break
            writer.writerow(item)


create_instances("time_series_data_human_activities.csv", 1)