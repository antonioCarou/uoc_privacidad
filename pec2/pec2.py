# importing the module
import json
import pandas as pd
import matplotlib.pyplot as plt

# Opening JSON file
with open('ThunderbeamData.json', encoding="utf8") as json_file:
    data = json.load(json_file)

    # Generamos un dataframe con los datos que hemos descargado del Lightbeam.
    df = pd.read_json('ThunderbeamData.json')
    df = df.transpose()
    print(df)

    # # Restringimos los registros a las páginas que hemos visitado.
    pagina = df[df.firstParty == True]
    # Imprimimos las columnas del dataframe que hemos cargado.
    print(pagina.columns.values)

    # Imprimimos la lista de páginas que hemos visitado.

    print(pagina.thirdParties.values)
    listaTerceros = []
    for listTerceros in pagina.thirdParties.values:
        listaTerceros.extend(listTerceros)


    setTerceros = set(listaTerceros)
    print('El cómputo total de terceros conectados son: ' + str(len(listaTerceros)))
    print('De los terceros conectados hay ' + str(len(setTerceros)) + ' únicos')
    print('Página con más terceros es: ' + pagina['thirdParties'].apply(len).idxmax())
    print('Tiene ' + str(len(list(pagina.loc[pagina['hostname'] == 'www.genbeta.com'].thirdParties.values[0]))) + ' terceros')

    # Generamos las parejas de páginas, la lista de terceros en común, y cuántos son.
    PaginesTercers = [[pagina.hostname[u],
                       pagina.hostname[v],
                       list(set(pagina.thirdParties[u]) & set(pagina.thirdParties[v])),
                       len(list(set(pagina.thirdParties[u]) & set(pagina.thirdParties[v])))]
                      for u in pagina.index
                      for v in pagina.index
                      if u != v]


    setTerceros = set(listaTerceros)
    maxCount = 0
    maxValue = ''
    for tercero in setTerceros:
        cuentaTercero = listaTerceros.count(tercero)
        if cuentaTercero > maxCount:
            maxCount = cuentaTercero
            maxValue = tercero

    print('Tercero que mas aparece: ' + maxValue)
    print('Aparece ' + str(maxCount) + ' veces')

    # Convertimos los datos que hemos calculado en un dataframe.
    PaginesTercers = pd.DataFrame(PaginesTercers,
                                  columns=['Pagina1',
                                           'Pagina2',
                                           'TercersEnComu',
                                           'Interseccio'])

    # Calculamos cuáles son las páginas que tienen más terceros en común.
    paginasTercerosComunMax = PaginesTercers.iloc[PaginesTercers['Interseccio'].idxmax()]
    print('Las páginas con más terceros en común son: ' + paginasTercerosComunMax.Pagina2 +
          ' y ' + paginasTercerosComunMax.Pagina1)
    print('El número de terceros en común es: ' + str() + str(paginasTercerosComunMax.Interseccio))