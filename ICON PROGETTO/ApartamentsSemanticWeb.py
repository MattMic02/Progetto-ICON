from SPARQLWrapper import SPARQLWrapper, JSON

# Funzione per eseguire query su DBpedia
def query_dbpedia(city_name):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(f"""
        SELECT ?population ?elevation ?feature
        WHERE {{
            ?city rdfs:label "{city_name}"@en ;
                  dbo:populationTotal ?population ;
                  dbo:elevation ?elevation .
            OPTIONAL {{
                ?city dbo:type ?feature .
            }}
        }}
        LIMIT 1
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    if results["results"]["bindings"]:
        result = results["results"]["bindings"][0]
        population = int(result.get("population", {}).get("value", -1))
        elevation = float(result.get("elevation", {}).get("value", -1.0))
        feature = result.get("feature", {}).get("value", "N/A")
        
        return population, elevation, feature
    else:
        return -1, -1, "Nessuna informazione"

# Funzione per eseguire query su Wikidata
def query_wikidata(city_name):
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    sparql.setQuery(f"""
        SELECT ?population ?elevation ?typeLabel
        WHERE {{
            ?city rdfs:label "{city_name}"@it ;
                  wdt:P31 wd:Q515 ;  # Identifica la città
                  wdt:P1082 ?population ;  # Popolazione
                  wdt:P2044 ?elevation .  # Elevazione
                  
            OPTIONAL {{
                ?city wdt:P206 ?location .  # P206: Luogo di ubicazione naturale
                ?location rdfs:label ?locationLabel .
                FILTER(LANG(?locationLabel) = "it")
            }}
            
            OPTIONAL {{
                ?city wdt:P279 ?type .  # Classificazione geografica
                ?type rdfs:label ?typeLabel .
                FILTER(LANG(?typeLabel) = "it")
            }}
        }}
        LIMIT 1
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    if results["results"]["bindings"]:
        result = results["results"]["bindings"][0]
        population = int(result.get("population", {}).get("value", -1))
        elevation = float(result.get("elevation", {}).get("value", -1))
        type_label = result.get("typeLabel", {}).get("value", "N/A")

        return population, elevation, type_label
    else:
        return -1, -1, "Nessuna informazione"

def inference_semantic_web(city_name):
    # Prova a ottenere i dati da DBpedia
    population, elevation, feature = query_dbpedia(city_name)
    
    # Se non trovi i dati, prova su Wikidata
    if not population or not elevation:
        population, elevation, feature = query_wikidata(city_name)
    
    classification = []  # Inizializza la variabile `classification` come lista vuota
    
    # Se ancora non ci sono risultati
    if not population or not elevation:
        return [-1, -1, "Nessuna informazione"]
    else:
        # Determina la classificazione basata sui dati ottenuti
        if feature and "costiera" in feature.lower():
            classification.append("Costiera")
        else:
            elevation_value = float(elevation)
            if elevation_value == -1:
                classification.append("Nessuna informazione")
            elif elevation_value < 100:
                classification.append("Bassa pianura")
            elif elevation_value < 200:
                classification.append("Alta pianura")
            elif elevation_value < 400:
                classification.append("Bassa collina")
            elif elevation_value < 600:
                classification.append("Alta collina")
            elif elevation_value < 1000:
                classification.append("Bassa montagna")
            elif elevation_value < 2000:
                classification.append("Media montagna")
            else:
                classification.append("Alta montagna")
                
    result = [city_name, population, elevation, classification]
    return result



def esegui_inferenza(filtered_dataset,cityes_apartament ):
    # Dizionario per memorizzare le informazioni delle città
    city_info = {}

    # Itera attraverso tutte le città uniche
    for c in cityes_apartament:
        # Recupera le informazioni dalla funzione inferenziale
        neww_data = inference_semantic_web(c)
        
        if neww_data:
            city_name, population, elevation, classification = neww_data
            city_info[city_name] = {
                'population': population,
                'elevation': elevation,
                'classification': ', '.join(classification) if classification else "N/A"
            }
        print(f"Sto salvando i dati per {c}")
        print(neww_data)
        #time.sleep(1)

    # Aggiungi nuove colonne al dataset originale
    filtered_dataset['population'] = filtered_dataset['neighbourhood_cleansed'].map(lambda x: city_info.get(x, {}).get('population', 'N/A'))
    filtered_dataset['elevation'] = filtered_dataset['neighbourhood_cleansed'].map(lambda x: city_info.get(x, {}).get('elevation', 'N/A'))
    filtered_dataset['classification'] = filtered_dataset['neighbourhood_cleansed'].map(lambda x: city_info.get(x, {}).get('classification', 'N/A'))
    return filtered_dataset