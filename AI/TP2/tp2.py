import csv
import os
from random import shuffle
import random
import numpy as np
from sklearn.neural_network import MLPClassifier
from yellowbrick.classifier import ROCAUC
from sklearn.linear_model import RidgeClassifier


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


def count_csv_files(folder):
    count = 0
    for file in os.listdir(folder):
        if file.endswith(".csv"):
            count += 1
    return count


def create_instances(data, t):
    activities = ["Downstairs", "Jogging", "Sitting", "Standing", "Upstairs", "Walking"]
    item = []
    with open(data, mode='r') as data:
        with open('C:/Users/gui/Desktop/Escola/ArtificialIntelligence-UBI/AI/TP2/nova/data_organized.csv', 'w', newline='', encoding='UTF8') as data_organized:
            data_reader = csv.DictReader(data)
            data_reader_list = list(data_reader)
            writter_data_organized = csv.writer(data_organized)

            total_lines = sum(1 for item in data_reader_list)
            begin_in_line = 0
            line_limit = t * 20

            user = data_reader_list[0]["user"]
            act = activities.index(data_reader_list[0]["activity"])

            while line_limit <= total_lines:
                for i in range(begin_in_line, line_limit):
                    if str(user) != data_reader_list[i]["user"] or str(
                            activities.index(data_reader_list[i]["activity"])) != str(act):
                        if str(user) != data_reader_list[i]["user"]:
                            user = data_reader_list[i]["user"]
                        if str(activities.index(data_reader_list[i]["activity"])) != str(act):
                            act = activities.index(data_reader_list[i]["activity"])
                        item = []

                    item.append(data_reader_list[i]["x-axis"])
                    item.append(data_reader_list[i]["y-axis"])
                    item.append(data_reader_list[i]["z-axis"])

                item.append(str(user))
                item.append(str(act))

                if len(item) == (t * 20 * 3) + 2:
                    writter_data_organized.writerow(item)

                item = []
                begin_in_line += 1
                line_limit += 1


# Passo 2 - KFoldState
def create_k_fold_states(k):
    idsUsers = []
    conjListas = []
    with open('C:/Users/gui/Desktop/Escola/ArtificialIntelligence-UBI/AI/TP2/nova/dtime_series_data_human_activities.csv', "r") as data:
        data_reader = csv.reader(data)
        next(data_reader)
        data_reader_list = list(data_reader)

    for row in data_reader_list:
        idUser_lido = row[0]
        verifpertence = idsUsers.count(idUser_lido)
        if verifpertence == 0:
            idsUsers.append(idUser_lido)

    shuffle(idsUsers)
    divide_ids = list(divide_chunks(idsUsers, k))

    for i in range(0, len(divide_ids)):
        conjListas.append("list_Conj" + str(i))

    with open('C:/Users/gui/Desktop/Escola/ArtificialIntelligence-UBI/AI/TP2/nova/data_organized.csv',"r") as data_org:
        dataOrg_reader = csv.reader(data_org)
        dataOrg_reader_list = list(dataOrg_reader)

    for i in range(0, len(conjListas)):
        with open("list_Conj" + str(i) + ".csv", 'w', newline='', encoding='UTF8') as fich_kFold:

            writter_fichFold = csv.writer(fich_kFold)
            for row in dataOrg_reader_list:
                idLido = row[-2]
                if idLido in divide_ids[i]:
                    writter_fichFold.writerow(row)


# Passo 3 - Train/Test
def train_test():
    csv_files_name = []
    csvFilesEscolhidos = []
    csvTestesTreino = []
    dir_path = r'C:/Users/gui/Desktop/Escola/ArtificialIntelligence-UBI/AI/TP2'
    for file in os.listdir(dir_path):
        if file.endswith('.csv'):
            csv_files_name.append(file)
    numberCSVFiles = len(csv_files_name)
    for i in range(0, numberCSVFiles):
        csv_files_nameTemp = csv_files_name.copy()
        csvRandom = random.choice(csv_files_name)
        while csvRandom in csvFilesEscolhidos:
            csvRandom = random.choice(csv_files_name)
        csvFilesEscolhidos.append(csvRandom)
        posCSVRandom = csv_files_nameTemp.index(csvRandom)
        csv_files_name.pop(posCSVRandom)
        csv_files_name.append(csvRandom)
        csvTestesTreino.append(csv_files_name)
        csv_files_name = csv_files_nameTemp
    return csvTestesTreino


# Passo 4 — Normalização
def find_min_max(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            data.append(row)
    data = np.array(data).astype(np.float64)
    return np.min(data), np.max(data)


def normalize(filename, min_value, max_value):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            normalized_row = [(float(val) - min_value) / (max_value - min_value) if i < len(row) - 2 else val for i, val in enumerate(row)]
            data.append(normalized_row)
    return data


def normalizarGeral():
    listTrainTest = train_test()

    for i in range(0, len(listTrainTest)):
        train = []
        test = []
        for j in range(0, len(listTrainTest[i])):
            train.append(listTrainTest[i][j])
            if j == len(listTrainTest[i]) - 1:
                test.append(listTrainTest[i][j])
                train.pop()

        global_min = float('inf')
        global_max = float('-inf')
        normalized_dataTrain = []

        for t in train:
            min_val, max_val = find_min_max(t)
            global_min = min(global_min, min_val)
            global_max = max(global_max, max_val)
            normalized_dataTrain.extend(normalize(t, global_min, global_max))

        with open('ficheiroTreino_' + str(i) + ".csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(normalized_dataTrain)

        normalized_dataTest = []
        normalized_dataTest.extend(normalize(test[0], global_min, global_max))

        with open('ficheiroTeste_' + str(i) + ".csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(normalized_dataTest)


# Passo 5 — Rede Neuronal
def redeneuronal():
    k = count_csv_files("C:/Users/gui/Desktop/Escola/ArtificialIntelligence-UBI/AI/TP2/")
    for i in range(0, 1):
        with open('C:/Users/gui/Desktop/Escola/ArtificialIntelligence-UBI/AI/TP2/ficheiroTreino_' + str(i) + ".csv",'r') as f:
            X = []
            Y = []

            reader = csv.reader(f)
            for row in reader:
                X.append(row)
            for x in X:
                Y.append(x[-1])

        with open('C:/Users/gui/Desktop/Escola/ArtificialIntelligence-UBI/AI/TP2/ficheiroTeste_' + str(i) + ".csv",'r') as f:
            Xt = []
            Yt = []

            reader = csv.reader(f)

            for row in reader:
                Xt.append(row)
            for xt in Xt:
                Yt.append(xt[-1])

        mlp = MLPClassifier()
        mlp.fit(X, Y)

        model = RidgeClassifier()
        visualizer = ROCAUC(model, classes=[0., 1., 2., 3., 4., 5.])
        visualizer.fit(np.array(X, dtype=float), np.array(Y, dtype=float))  # Fit the training data to the visualizer
        visualizer.score(np.array(Xt, dtype=float), np.array(Yt, dtype=float))  # Evaluate the model on the test data
        visualizer.show()


# Main
k = 5
#create_instances("C:/Users/gui/Desktop/Escola/ArtificialIntelligence-UBI/AI/TP2/nova/dtime_series_data_human_activities.csv",1)
#create_k_fold_states(k) # K = 5, TODOS OS CONJUNTOS TÊM 5 IDS DIFERENTES, PARA ISSO CRIARAM-SE 8 FICHEIROS.
#normalizarGeral()
redeneuronal()


