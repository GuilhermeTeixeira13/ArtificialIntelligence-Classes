import csv
import os
from random import shuffle
import random
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from collections import defaultdict


# Função de Ajuda
def integerencode(categorias):
    # Cria um dicionário para armazenar os mapeamentos de valores para inteiros
    valores_para_inteiros = defaultdict(int)
    # Inicializa um contador para atribuir valores inteiros únicos
    contador = 0
    # Para cada valor na lista de categorias
    for valor in categorias:
        # Se o valor ainda não tiver sido mapeado para um inteiro, atribua um novo inteiro
        if valor not in valores_para_inteiros:
            valores_para_inteiros[valor] = contador
            contador += 1
    # Transforma a lista de categorias numa lista de inteiros usando o dicionário de mapeamento
    inteiros = [valores_para_inteiros[valor] for valor in categorias]
    return inteiros


def divide_chunks(l, n):
    # looping till length l
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


# Passo 1 - Create Instances
def create_instances(data, t):
    activities = ["Downstairs", "Jogging", "Sitting", "Standing", "Upstairs", "Walking"]
<<<<<<< Updated upstream
    item = [1, 5]
=======
    item = []
>>>>>>> Stashed changes
    with open(data, mode='r') as data:
        with open('data_organized.csv', 'w', newline='', encoding='UTF8') as data_organized:
            data_reader = csv.DictReader(data)
            data_reader_list = list(data_reader)
            writter_data_organized = csv.writer(data_organized)

            total_lines = sum(1 for item in data_reader_list)
<<<<<<< Updated upstream
=======
            # data_reader_list[total_lines-1]

>>>>>>> Stashed changes
            begin_in_line = 0
            line_limit = t * 20

            user = data_reader_list[0]["user"]
            act = activities.index(data_reader_list[0]["activity"])

<<<<<<< Updated upstream
            print("LIMIT:"+str(line_limit)+" // TOTAL:"+str(total_lines))

            while line_limit <= total_lines:
                print("BEGIN:"+str(begin_in_line)+" -> END:"+str(line_limit))
                for i in range(begin_in_line, line_limit):
                    if str(user) != data_reader_list[i]["user"] or str(activities.index(data_reader_list[i]["activity"])) != str(act):
=======
            print("LIMIT:" + str(line_limit) + " // TOTAL:" + str(total_lines))

            while line_limit <= total_lines:
                print("BEGIN:" + str(begin_in_line) + " -> END:" + str(line_limit))
                for i in range(begin_in_line, line_limit):
                    if str(user) != data_reader_list[i]["user"] or str(
                            activities.index(data_reader_list[i]["activity"])) != str(act):
>>>>>>> Stashed changes
                        if str(user) != data_reader_list[i]["user"]:
                            user = data_reader_list[i]["user"]
                        if str(activities.index(data_reader_list[i]["activity"])) != str(act):
                            act = activities.index(data_reader_list[i]["activity"])
<<<<<<< Updated upstream

                        writter_data_organized.writerow(item)
                        item = []
                        item.append(str(user))
                        item.append(str(act))
=======
                        item = []
>>>>>>> Stashed changes

                    item.append(data_reader_list[i]["x-axis"])
                    item.append(data_reader_list[i]["y-axis"])
                    item.append(data_reader_list[i]["z-axis"])

<<<<<<< Updated upstream
=======
                item.append(str(user))
                item.append(str(act))

                if len(item) == (t * 20 * 3) + 2:
                    writter_data_organized.writerow(item)

                item = []
>>>>>>> Stashed changes
                begin_in_line += 1
                line_limit += 1
def create_k_fold_states(k):




# Passo 2 - KFoldState
def create_k_fold_states(k):
    idsUsers = []
    conjListas = []
    with open('time_series_data_human_activities.csv', "r") as data:
        # Ler cvs
        data_reader = csv.reader(data)

        # the below statement will skip the first row
        next(data_reader)

        # Colocar conteúdo numa lista
        data_reader_list = list(data_reader)

    # Armazenar ID's do csv em Lista. (Baralhados)
    for row in data_reader_list:
        idUser_lido = row[0]
        verifpertence = idsUsers.count(idUser_lido)
        if verifpertence == 0:
            idsUsers.append(idUser_lido)
    shuffle(idsUsers)
    divide_ids = list(divide_chunks(idsUsers, k))
    print(divide_ids)
    print(len(divide_ids))
    # Gerar nome dos ficheiros.csv
    for i in range(0, len(divide_ids)):
        conjListas.append("list_Conj" + str(i))
    print(conjListas)
    # Colocar conteúdo do data_organized numa lista
    with open('C:/Users/joaob/OneDrive/Ambiente de Trabalho/SCH DEV/CSV TP2 PYTHON/data_organized.csv',
              "r") as data_org:
        dataOrg_reader = csv.reader(data_org)
        dataOrg_reader_list = list(dataOrg_reader)
    # Percorrer cada ficheiro
    for i in range(0, len(conjListas)):
        with open("list_Conj" + str(i) + ".csv", 'w', newline='', encoding='UTF8') as fich_kFold:
            # Writter
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
    dir_path = r'C:\Users\joaob\OneDrive\Ambiente de Trabalho\SCH DEV\IA\TP2'
    # Iterate directory
    for file in os.listdir(dir_path):
        # check only text files
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
            normalized_row = [(float(val) - min_value) / (max_value - min_value) if i < len(row) - 2 else val for i, val
                              in enumerate(row)]
            data.append(normalized_row)
    return data


def normalizarGeral():
    listTrainTest = train_test()
    print(listTrainTest)
    for i in range(0, len(listTrainTest)):
        train = []
        test = []
        for j in range(0, len(listTrainTest[i])):
            train.append(listTrainTest[i][j])
            if j == len(listTrainTest[i]) - 1:
                test.append(listTrainTest[i][j])
                train.pop()
        # Itera sobre a lista de nomes de ficheiros
        print(train)
        print(test)
        global_min = float('inf')
        global_max = float('-inf')
        normalized_dataTrain = []
        for t in train:
            min_val, max_val = find_min_max(t)
            global_min = min(global_min, min_val)
            global_max = max(global_max, max_val)
            normalized_dataTrain.extend(normalize(t, global_min, global_max))
        print(f'O mínimo global é {global_min} e o máximo global é {global_max}')
        with open('ficheiroTreino_' + str(i) + ".csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(normalized_dataTrain)
        normalized_dataTest = []
        normalized_dataTest.extend(normalize(test[0], global_min, global_max))
        print(f'Ficheiro a dar extend: {test[0]}')
        with open('ficheiroTeste_' + str(i) + ".csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(normalized_dataTest)


# Passo 5 — Rede Neuronal
def redeneuronal():
    k = count_csv_files("C:/Users/joaob/OneDrive/Ambiente de Trabalho/SCH DEV/IA/TP2")
    # Cria uma lista de rótulos categóricos
    categorias = [0, 1, 2, 3, 4]

    # Cria um objeto LabelEncoder
    label_encoder = LabelEncoder()
    print(label_encoder)

    # Transforma as categorias em valores numéricos
    numericos = label_encoder.fit_transform(categorias)

    # Cria um objeto OneHotEncoder
    one_hot_encoder = OneHotEncoder()

    # Transforma os valores numéricos em vetores binários
    binarios = one_hot_encoder.fit_transform(numericos.reshape(-1, 1))
    binarios = binarios.toarray()
    inteiros = binarios[:, 0].astype(int)
    print(inteiros)
    for i in range(0, k):
        # Cria o classificador MLP
        mlp = MLPClassifier(hidden_layer_sizes=(5, 5), max_iter=200)
        Xt = []
        X = []
        Yt = []
        Y = []
        with open(
                'C:/Users/joaob/OneDrive/Ambiente de Trabalho/SCH DEV/CSV TP2 PYTHON/ficheiroTreino_' + str(i) + ".csv",
                'r') as f:
            X = []
            Y = []
            # Create a CSV reader object
            reader = csv.reader(f)
            # Iterate over the rows of the file
            for row in reader:
                # Add the row to the data list
                X.append(row)
            for x in X:
                Y.append(x[-1])
            """
            with open('ficheiro_sem2col_Treino_' + str(i) + ".csv", 'w') as g:
                # Crie um escritor CSV a partir do novo ficheiro
                writer = csv.writer(g)
                # Para cada linha no ficheiro CSV original
                for row in reader:
                    # Selecione as colunas desejadas e escreva-as no novo ficheiro CSV
                    writer.writerow(row[:-2])
            """
        with open(
                'C:/Users/joaob/OneDrive/Ambiente de Trabalho/SCH DEV/CSV TP2 PYTHON/ficheiroTeste_' + str(i) + ".csv",
                'r') as f:
            Xt = []
            Yt = []
            # Create a CSV reader object
            reader = csv.reader(f)
            # Iterate over the rows of the file
            for row in reader:
                # Add the row to the data list
                Xt.append(row)
            for xt in Xt:
                Yt.append(xt[-1])
            """
            with open('ficheiro_sem2col_Teste_' + str(i) + ".csv", 'w') as g:
                # Cria um escritor CSV a partir do novo ficheiro
                writer = csv.writer(g)
                # Para cada linha no ficheiro CSV original
                for row in reader:
                    writer.writerow(row[:-2])
            """
        mlp.fit(X,Y)
        respostas = mlp.predict(Xt)
        print(respostas)

# Main

k = 5
# create_instances("time_series_data_human_activities.csv",1)
# create_k_fold_states(k) // K = 5, TODOS OS CONJUNTOS TÊM 5 IDS DIFERENTES, PARA ISSO CRIARAM-SE 8 FICHEIROS.
# normalizarGeral()
redeneuronal()