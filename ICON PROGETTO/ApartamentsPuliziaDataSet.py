import pandas as pd

# Funzione per pulire le stringhe
def clean_string(value):
    if isinstance(value, str):
        # Sostituisce le lettere accentate con quelle non accentate
        replacements = {
            'à': 'a', 'è': 'e', 'é': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
            'À': 'A', 'È': 'E', 'É': 'E', 'Ì': 'I', 'Ò': 'O', 'Ù': 'U'
        }
        for accented_char, unaccented_char in replacements.items():
            value = value.replace(accented_char, unaccented_char)

        # Mantiene solo lettere, numeri e virgole, rimuovendo tutto il resto
        allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,. ")
        value = ''.join(char for char in value if char in allowed_chars)
        
        # Riduce gli spazi multipli a un singolo spazio
        while "  " in value:
            value = value.replace("  ", " ")

        # Rimuove spazi all'inizio e alla fine della stringa
        value = value.strip()

    return value


def clear_dataset_prolog(data):
    # Applica la pulizia delle stringhe ad alcune colonne
    data['name'] = data['name'].apply(lambda x: clean_string(x) if pd.notna(x) else x)
    data['host_location'] = data['host_location'].apply(lambda x: clean_string(x) if pd.notna(x) else x)
    data['host_verifications'] = data['host_verifications'].apply(lambda x: clean_string(x) if pd.notna(x) else x)
    #data['neighbourhood_cleansed'] = data['neighbourhood_cleansed'].apply(lambda x: clean_string(x) if pd.notna(x) else x)
    data['amenities'] = data['amenities'].apply(lambda x: clean_string(x) if pd.notna(x) else x)

    # axis=1: Si riferisce all'asse delle colonne (l'asse delle x). 
    # #Quando utilizzi axis=1, l'operazione viene eseguita sulle colonne. 
    # Ad esempio, se usi drop(columns, axis=1), Pandas rimuove le colonne specificate.
    def clean_price_string(price_str):
        # Controlla se la stringa non è vuota o nulla
        if price_str and isinstance(price_str, str):
            # Rimuovi il simbolo del dollaro
            cleaned_str = price_str.replace("$", "").replace(",", "").strip()
            # Trova la posizione del punto (se esiste) e conserva solo la parte prima del punto
            if '.' in cleaned_str:
                cleaned_str = cleaned_str.split('.')[0]
            # Ritorna la stringa pulita
            return int(cleaned_str)
        return None
    data['price'] = data['price'].apply(lambda x: clean_price_string(x) if pd.notna(x) else x)

    # Rimozione delle colonne non rilevanti
    data = data.drop('id', axis=1)
    data = data.drop('host_id', axis=1)
    data = data.drop('host_picture_url', axis=1)
    data = data.drop('host_url', axis=1)
    data = data.drop('listing_url', axis=1)
    data = data.drop('picture_url', axis=1)
    data = data.drop('host_about', axis=1)
    data = data.drop('host_thumbnail_url', axis=1)
    data = data.drop('host_neighbourhood', axis=1)
    data = data.drop('calculated_host_listings_count_private_rooms', axis=1)
    data = data.drop('calculated_host_listings_count_shared_rooms', axis=1)
    data = data.drop('bathrooms_text', axis=1)
    data = data.drop('calendar_updated', axis=1)
    data = data.drop('availability_60', axis=1)
    data = data.drop('availability_30', axis=1)
    data = data.drop('availability_365', axis=1)
    data = data.drop('calendar_last_scraped', axis=1)
    data = data.drop('number_of_reviews_l30d', axis=1)
    data = data.drop('license', axis=1)
    data = data.drop('neighbourhood', axis=1)
    data = data.drop('scrape_id', axis=1)
    data = data.drop('last_scraped', axis=1)
    data = data.drop('host_name', axis=1)
    data = data.drop('minimum_minimum_nights', axis=1)
    data = data.drop('maximum_minimum_nights', axis=1)
    data = data.drop('minimum_maximum_nights', axis=1)
    data = data.drop('maximum_maximum_nights', axis=1)
    data = data.drop('minimum_nights_avg_ntm', axis=1)
    data = data.drop('maximum_nights_avg_ntm', axis=1)
    data = data.drop('neighborhood_overview', axis=1)
    data = data.drop('description', axis=1)
    data = data.drop('bathrooms', axis=1)
    #data = data.drop('amenities', axis=1)

    # Aggiunta colonna id con ID
    data.loc[:,'id']=range(1,(data.shape[0])+1)

    # Aggiunta colonna id con ID
    data.loc[:,'host_id']=range(1,(data.shape[0])+1)

    # Rimozione delle righe con valori mancanti in 'room_type'
    data = data.dropna(subset=['room_type'])

    # Rimozione delle righe con valori mancanti in 'price'
    data = data.dropna(subset=['price'])

    # Rimozione delle righe con valori mancanti in 'neighbourhood_cleansed'
    data = data.dropna(subset=['neighbourhood_cleansed'])

    # Rimozione delle righe con valori mancanti in 'host_since'
    data = data.dropna(subset=['host_since'])

    # Rimozione delle righe con valori mancanti in 'latitude'
    data = data.dropna(subset=['latitude'])

    # Rimozione delle righe con valori mancanti in 'longitude'
    data = data.dropna(subset=['longitude'])

    # Rimozione delle righe dove 'host_since' non corrisponde al pattern 'XXXX-XX-XX'
    data = data[data['host_since'].str.match(r'^\d{4}-\d{2}-\d{2}$', na=False)]

    # Ottieni il numero di righe
    num_rows = data.shape[0]
    print(f"Il numero di righe nel file CSV è: {num_rows}")

    return data

def clear_dataset_unsupervised_learning(data):

    data = data.drop('source', axis=1)
    data = data.drop('name', axis=1)
    data = data.drop('host_since', axis=1)
    data = data.drop('host_location', axis=1)
    data = data.drop('host_response_time', axis=1)
    data = data.drop('host_listings_count', axis=1)
    data = data.drop('host_total_listings_count', axis=1)
    data = data.drop('host_verifications', axis=1)
    data = data.drop('id', axis=1)
    data = data.drop('host_id', axis=1)
    data = data.drop('calculated_host_listings_count', axis=1)
    data = data.drop('availability_90', axis=1)
    data = data.drop('calculated_host_listings_count_entire_homes', axis=1)
    data = data.drop('reviews_per_month', axis=1)

    # Elimino le righe con valore altitutidine -1 perchè non hanno contenuto informativo
    data = data[data['elevation'] != -1]

    # Inizializza un dizionario vuoto per memorizzare i servizi unici e il loro conteggio
    amenities_count = {}

    # Funzione per aggiornare il dizionario con il conteggio dei servizi
    def update_amenities_count(amenities_str):
        if pd.notna(amenities_str):  # Controlla se il valore non è NaN
            # Dividi la stringa di servizi in singoli elementi
            amenities_list = amenities_str.split(", ")
            # Aggiorna il conteggio dei servizi nel dizionario
            for amenity in amenities_list:
                if amenity in amenities_count:
                    amenities_count[amenity] += 1
                else:
                    amenities_count[amenity] = 1

    # Applica la funzione a tutte le righe della colonna 'amenities'
    data['amenities'].apply(update_amenities_count)

    # Ordina il dizionario in base ai valori (conteggi) in ordine decrescente
    sorted_amenities_count = dict(sorted(amenities_count.items(), key=lambda item: item[1], reverse=True))
    x = 320
    # Seleziona i primi x servizi
    top_amenities = list(sorted_amenities_count.keys())[:x]

    # Creare un DataFrame vuoto con colonne per ciascuna amenity
    amenities_df = pd.DataFrame(0, index=data.index, columns=top_amenities)

    # Funzione per aggiornare il DataFrame delle amenities
    def update_amenities_columns(row):
        if pd.notna(row['amenities']):
            amenities_list = row['amenities'].split(", ")
            for amenity in amenities_list:
                if amenity in top_amenities:
                    amenities_df.at[row.name, amenity] = 1

    # Applicare la funzione a ogni riga
    data.apply(update_amenities_columns, axis=1)

    # Concatenare il DataFrame delle amenities con il DataFrame originale
    data = pd.concat([data, amenities_df], axis=1)

    # Deframmentare il DataFrame
    data = data.copy()

    print("Numero di servizi unici:", len(amenities_count))
    print(len(amenities_count))
    
    def update_region_columns(data):
        # Lista delle regioni
        regions = ['Bari', 'Foggia', 'Lecce', 'Taranto', 'Brindisi', 'Barletta-Andria-Trani']
        
        # Aggiungi una colonna per ciascuna regione ed inizializzala a 0
        for region in regions:
            data[region] = 0
        
        # Funzione per aggiornare le colonne delle regioni
        def update_region(row):
            if row['neighbourhood_group_cleansed'] in regions:
                row[row['neighbourhood_group_cleansed']] = 1
            return row
        
        # Applica la funzione per aggiornare le colonne delle regioni
        data = data.apply(update_region, axis=1)
        
        return data
    
    data = update_region_columns(data)

    # Rimuove la colonna 'amenities' dal DataFrame in quanto è stata sostituita da colonne binarie per i servizi
    data = data.drop('amenities', axis=1)

    # Elimino tutte le righe con valori mancanti
    data = data.dropna()
    return data

def clean_percentage_string(percentage_str):
    # Controlla se la stringa non è vuota o nulla
    if percentage_str and isinstance(percentage_str, str):
        # Rimuovi il simbolo '%' e converti il valore a intero
        return int(percentage_str.replace('%', '').strip())
    return -1

def clear_dataset_supervised_learning(data):
    # Applicazione su una colonna specifica del DataFrame
    data['host_response_rate'] = data['host_response_rate'].apply(lambda x: clean_percentage_string(x) if pd.notna(x) else x)
    data['host_acceptance_rate'] = data['host_acceptance_rate'].apply(lambda x: clean_percentage_string(x) if pd.notna(x) else x)
    data = data[data['host_response_rate'] != -1]
    data = data[data['host_acceptance_rate'] != -1]

    # Conversione delle colonne booleane in valori binari
    data['host_is_superhost'] = data['host_is_superhost'].apply(lambda x: 1 if x == 't' else 0)
    data['host_has_profile_pic'] = data['host_has_profile_pic'].apply(lambda x: 1 if x == 't' else 0)
    data['host_identity_verified'] = data['host_identity_verified'].apply(lambda x: 1 if x == 't' else 0)
    data['has_availability'] = data['host_identity_verified'].apply(lambda x: 1 if x == 't' else 0)
    data['instant_bookable'] = data['instant_bookable'].apply(lambda x: 1 if x == 't' else 0)

    data = data.drop('first_review', axis=1)
    data = data.drop('last_review', axis=1)
    data = data.drop('neighbourhood_cleansed', axis=1)
    data = data.drop('neighbourhood_group_cleansed', axis=1)
    data = data.drop('classification', axis=1)
    # FARE FEATURE ENGINEERING SU QUESTE COLONNE
    # Crea colonne dummy per 'property_type' e 'room_type' con valori 0 e 1
    property_type_dummies = pd.get_dummies(data['property_type'], prefix='property_type').astype(int)
    room_type_dummies = pd.get_dummies(data['room_type'], prefix='room_type').astype(int)

    # Unisci le colonne dummy al dataset originale
    data = pd.concat([data, property_type_dummies, room_type_dummies], axis=1)

    # Rimuovi le colonne originali 'property_type' e 'room_type' se non sono più necessarie
    data = data.drop('property_type', axis=1)
    data = data.drop('room_type', axis=1)

    # Handle missing values
    data.fillna(data.mean(), inplace=True)
    
    return data