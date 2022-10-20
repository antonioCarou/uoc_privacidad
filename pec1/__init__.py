# importing the module
import json
import pandas as pd
import matplotlib.pyplot as plt

# Opening JSON file
with open('Takeout/reproducciones.json', encoding="utf8") as json_file:
    data = json.load(json_file)
    # Generamos el dataframe
    df = pd.DataFrame(data, columns=['title', 'titleUrl', 'time'])
    # Nueva columna con las horas spliteando el timestamp ("T" separa entre fecha y hora y la hora spliteamos por ":"
    # y el primer elemento del array es la hora).
    df['hour'] = df['time'].str.split('T').str[1].str.split(':').str[0]
    # Contamos el numero de reproducciones de cada hora
    data = df.groupby(['hour'])['hour'].count().reset_index(name='count')
    plt.hist(sorted(df['hour'].tolist()), bins=24, label='Distribución de reproducciones')
    plt.xlabel('Hora')
    plt.ylabel('Reproducciones')
    plt.title('Distribución reproducciones',
              fontweight="bold")
    plt.show()

    # df.groupby(['hour'])['hour'].count().hist(bins=24).plot()
