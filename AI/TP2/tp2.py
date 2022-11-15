import csv

# downstairs, jogging, sitting, standing, upstairs, walking

def create_instances(data, t):
    activities = ["Downstairs", "Jogging", "Sitting", "Standing", "Upstairs", "Walking"]
    user = 1
    item = ""
    with open(data, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                if line_count == 1:
                    item = "1/"

                # Muda de user
                if str(user) == row["user"]:
                    item = item + (f'{row["x-axis"]},{row["y-axis"]},{row["z-axis"]}/')
                    line_count += 1
                else:
                    user += 1
                    item = item + str(user) + '/' + (f'{row["x-axis"]},{row["y-axis"]},{row["z-axis"]}/')
                    line_count += 1
            else:
                line_count += 1
            if line_count == t*20:
                break
        print(item)

#str(activities.index(row["activity"]))
create_instances("time_series_data_human_activities.csv", 5500)