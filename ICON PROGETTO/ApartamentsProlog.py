import pandas as pd
from pyswip import Prolog


def initialize_kb_file(kb_path):
    """Inizializza il file della knowledge base (KB) Prolog."""
    with open(kb_path, "w", encoding="utf-8") as file:
        file.write("")  # Sovrascrive il file o crea un nuovo file vuoto

def write_fact_to_file(fact, file_path):
    """Scrive un fatto Prolog nel file specificato."""
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(fact + ".\n")

def write_prolog_rule(file_path, rule):
    """Scrive una regola Prolog nel file specificato."""
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(rule + "\n")

def create_prolog_fact(row):
    """Crea un fatto Prolog basato su una riga del DataFrame."""
    id = row['id']
    source = row['source'] if pd.notna(row['source']) else "no_source"
    name = row['name'].replace("'", "") if pd.notna(row['name']) else "no_name"
    host_id = row['host_id'] if pd.notna(row['host_id']) else -1
    host_since = row['host_since'] if pd.notna(row['host_since']) else "no_host_since"
    host_location = row['host_location'].replace("'", "") if pd.notna(row['host_location']) else "no_location"
    host_response_time = row['host_response_time'].replace("'", "") if pd.notna(row['host_response_time']) else "no_response_time"
    host_response_rate = int(row['host_response_rate'].replace("%", "")) if pd.notna(row['host_response_rate']) else -1
    host_acceptance_rate = int(row['host_acceptance_rate'].replace("%", "")) if pd.notna(row['host_acceptance_rate']) else -1
    host_is_superhost = row['host_is_superhost'] if pd.notna(row['host_is_superhost']) else "no"
    host_listings_count = int(row['host_listings_count']) if pd.notna(row['host_listings_count']) else -1
    host_total_listings_count = int(row['host_total_listings_count']) if pd.notna(row['host_total_listings_count']) else -1
    host_verifications = row['host_verifications'].replace("'", "") if pd.notna(row['host_verifications']) else "no_verifications"
    host_has_profile_pic = row['host_has_profile_pic'] if pd.notna(row['host_has_profile_pic']) else "no"
    host_identity_verified = row['host_identity_verified'] if pd.notna(row['host_identity_verified']) else "no"
    neighbourhood_cleansed = row['neighbourhood_cleansed'].replace("'", "") if pd.notna(row['neighbourhood_cleansed']) else "no_neighbourhood"
    neighbourhood_group_cleansed = row['neighbourhood_group_cleansed'].replace("'", "") if pd.notna(row['neighbourhood_group_cleansed']) else "no_neighbourhood_group"
    latitude = int(row['latitude']) if pd.notna(row['latitude']) else -1.0
    longitude = int(row['longitude']) if pd.notna(row['longitude']) else -1.0
    property_type = row['property_type'].replace("'", "") if pd.notna(row['property_type']) else "no_property_type"
    room_type = row['room_type'].replace("'", "") if pd.notna(row['room_type']) else "no_room_type"
    accommodates = int(row['accommodates']) if pd.notna(row['accommodates']) else -1
    bedrooms = int(row['bedrooms']) if pd.notna(row['bedrooms']) else -1
    beds = int(row['beds']) if pd.notna(row['beds']) else -1
    price = int(row['price']) if pd.notna(row['price']) else -1.0
    minimum_nights = int(row['minimum_nights']) if pd.notna(row['minimum_nights']) else -1
    maximum_nights = int(row['maximum_nights']) if pd.notna(row['maximum_nights']) else -1
    has_availability = row['has_availability'].replace("'", "") if pd.notna(row['has_availability']) else "no_availability"
    availability_90 = int(row['availability_90']) if pd.notna(row['availability_90']) else -1
    number_of_reviews = int(row['number_of_reviews']) if pd.notna(row['number_of_reviews']) else -1
    number_of_reviews_ltm = int(row['number_of_reviews_ltm']) if pd.notna(row['number_of_reviews_ltm']) else -1
    first_review = row['first_review'] if pd.notna(row['first_review']) else "no_first_review"
    last_review = row['last_review'] if pd.notna(row['last_review']) else "no_last_review"
    review_scores_rating = row['review_scores_rating'] if pd.notna(row['review_scores_rating']) else -1.0
    review_scores_accuracy = row['review_scores_accuracy'] if pd.notna(row['review_scores_accuracy']) else -1.0
    review_scores_cleanliness = row['review_scores_cleanliness'] if pd.notna(row['review_scores_cleanliness']) else -1.0
    review_scores_checkin = row['review_scores_checkin'] if pd.notna(row['review_scores_checkin']) else -1.0
    review_scores_communication = row['review_scores_communication'] if pd.notna(row['review_scores_communication']) else -1.0
    review_scores_location = row['review_scores_location'] if pd.notna(row['review_scores_location']) else -1.0
    review_scores_value = row['review_scores_value'] if pd.notna(row['review_scores_value']) else -1.0
    instant_bookable = row['instant_bookable'].replace("'", "") if pd.notna(row['instant_bookable']) else "no"
    calculated_host_listings_count = int(row['calculated_host_listings_count']) if pd.notna(row['calculated_host_listings_count']) else -1
    calculated_host_listings_count_entire_homes = int(row['calculated_host_listings_count_entire_homes']) if pd.notna(row['calculated_host_listings_count_entire_homes']) else -1
    reviews_per_month = float(row['reviews_per_month']) if pd.notna(row['reviews_per_month']) else -1.0
    amenites = row['amenities'].replace("'", "") if pd.notna(row['amenities']) else "no_amenities"

    # Restituisce il fatto Prolog come stringa
    return (
        f"property({id}, '{source}', '{name}', "
        f"{host_id}, '{host_since}', '{host_location}', '{host_response_time}', "
        f"{host_response_rate}, {host_acceptance_rate}, '{host_is_superhost}', {host_listings_count}, "
        f"{host_total_listings_count}, '{host_verifications}', '{host_has_profile_pic}', "
        f"'{host_identity_verified}', '{neighbourhood_cleansed}', '{neighbourhood_group_cleansed}', {latitude}, {longitude}, "
        f"'{property_type}', '{room_type}', {accommodates},"
        f"{bedrooms}, {beds}, {price}, {minimum_nights}, {maximum_nights}, "
        f"'{has_availability}', {availability_90}, {number_of_reviews}, {number_of_reviews_ltm}, "
        f"'{first_review}', '{last_review}', {review_scores_rating}, {review_scores_accuracy}, "
        f"{review_scores_cleanliness}, {review_scores_checkin}, {review_scores_communication}, "
        f"{review_scores_location}, {review_scores_value}, '{instant_bookable}', "
        f"{calculated_host_listings_count}, {calculated_host_listings_count_entire_homes}, "
        f"{reviews_per_month}, '{amenites}')"
    )

def populate_prolog_kb(dataset, kb_path):
    """Popola la knowledge base di Prolog con i fatti derivati dal dataset."""
    for index, row in dataset.iterrows():
        prolog_fact = create_prolog_fact(row)
        write_fact_to_file(prolog_fact, kb_path)

def query_prolog(kb_path):
    """Esegue una query al motore Prolog e restituisce un dizionario con i risultati."""
    prolog = Prolog()
    prolog.consult(kb_path)

    results_dict = {}
    query = "host_indicator_value(HostScore, ID)"
    res = prolog.query(query)
    for result in res:
        ID = result["ID"]
        HostScore = result["HostScore"]
        results_dict[ID] = HostScore
    
    return results_dict

def update_dataset_with_prolog_results(dataset, results_dict):
    """Aggiorna il dataset con i risultati ottenuti dalla query Prolog."""
    dataset['host_valutation'] = -1
    for index, row in dataset.iterrows():
        id_value = row['id']
        if id_value in results_dict:
            dataset.at[index, 'host_valutation'] = results_dict[id_value]
    
    return dataset

def execute_prolog_module(dataset, kb_path):
    """Esegue l'intero processo di integrazione tra il dataset e Prolog."""
    # Stampa le informazioni sul dataset
    print(dataset.info())

    # Inizializza il file della knowledge base
    initialize_kb_file(kb_path)

    # Popola la KB Prolog con i fatti dal dataset
    populate_prolog_kb(dataset, kb_path)

    # Scrivi la regola nel file Prolog
    regola = """
    (host_indicator_value(HostScore,ID) :- property(ID,_,_,_,HostSince,_,HostResponceTime,HostResponceRate,HostAcceptanceRate,HostIsSuperHost,_,_,_,HostHasProfilePicture,HostIdentifyVerified,_,_,_,_,_,_,Accomodates,NumberOfBedRooms,NumberOfBeds,_,_,_,_,_,NumberOfReviews,NumberOfReviewsLastYear,_,LastReview,ReviewScoreRating,ReviewScoreAccuracy,_,_,_,_,_,IstantBookable,_,_,ReviewsPerMonth,_), 
        
        % 1. Calcola il punteggio HostSinceScore : 10 punti
        (HostSince = "no_host_since" ->
            HostSinceScore = 0
        ;
            % Estrai l'anno da HostSince
            sub_string(HostSince, 0, 4, _, YearString),
            atom_number(YearString, YearHostSince),
            YearDiff is 2022 - YearHostSince,
            HostSinceScore is min(YearDiff, 10)
        ),

        % 2. Calcola il punteggio HostResponseTimeScore : 5 punti
        (HostResponceTime = 'within an hour' -> HostResponseTimeScore = 5;
        HostResponceTime = 'within a few hours' -> HostResponseTimeScore = 4;
        HostResponceTime = 'within a day' -> HostResponseTimeScore = 3;
        HostResponceTime = 'a few days or more' -> HostResponseTimeScore = 1;
        HostResponceTime = 'no_response_time' -> HostResponseTimeScore = 0),

        % 3. Calcola il punteggio HostResponseRateScore : 10 punti
        (HostResponceRate = -1 -> HostResponseRateScore = 0;
        HostResponceRate = 100 -> HostResponseRateScore = 10;
        HostResponceRate >= 90, HostResponceRate < 100 -> HostResponseRateScore = 9;
        HostResponceRate >= 80, HostResponceRate < 90 -> HostResponseRateScore = 8;
        HostResponceRate >= 70, HostResponceRate < 80 -> HostResponseRateScore = 7;
        HostResponceRate >= 60, HostResponceRate < 70 -> HostResponseRateScore = 6;
        HostResponceRate >= 50, HostResponceRate < 60 -> HostResponseRateScore = 5;
        HostResponceRate >= 40, HostResponceRate < 50 -> HostResponseRateScore = 4;
        HostResponceRate >= 30, HostResponceRate < 40 -> HostResponseRateScore = 3;
        HostResponceRate >= 20, HostResponceRate < 30 -> HostResponseRateScore = 2;
        HostResponceRate >= 10, HostResponceRate < 20 -> HostResponseRateScore = 1;
        HostResponceRate < 10 -> HostResponseRateScore = 0),

        % 4. Calcola il punteggio HostAcceptanceRateScore : 10 punti
        (HostAcceptanceRate = -1 -> HostAcceptanceRateScore = 0;
        HostAcceptanceRate = 100 -> HostAcceptanceRateScore = 10;
        HostAcceptanceRate >= 90, HostAcceptanceRate <100 -> HostAcceptanceRateScore = 9;
        HostAcceptanceRate >= 80, HostAcceptanceRate <90 -> HostAcceptanceRateScore = 8;
        HostAcceptanceRate >= 70, HostAcceptanceRate <80 -> HostAcceptanceRateScore = 7;
        HostAcceptanceRate >= 60, HostAcceptanceRate <70 -> HostAcceptanceRateScore = 6;
        HostAcceptanceRate >= 50, HostAcceptanceRate <60 -> HostAcceptanceRateScore = 5;
        HostAcceptanceRate >= 40, HostAcceptanceRate <50 -> HostAcceptanceRateScore = 4;
        HostAcceptanceRate >= 30, HostAcceptanceRate <40 -> HostAcceptanceRateScore = 3;
        HostAcceptanceRate >= 20, HostAcceptanceRate <30 -> HostAcceptanceRateScore = 2;
        HostAcceptanceRate >= 10, HostAcceptanceRate <20 -> HostAcceptanceRateScore = 1;
        HostAcceptanceRate >= 0, HostAcceptanceRate <10 -> HostAcceptanceRateScore = 0),

        % 5. Calcola il punteggio HostIsSuperHostScore : 5 punti
        (HostIsSuperHost = 't' -> HostIsSuperHostScore = 5;
        HostIsSuperHost = 'f' -> HostIsSuperHostScore = 0;
        HostIsSuperHost = 'no' -> HostIsSuperHostScore = 0),

        % 6. Calcola il punteggio HostHasProfilePictureScore : 5 punti
        (HostHasProfilePicture = 't' -> HostHasProfilePictureScore = 5;
        HostHasProfilePicture = 'f' -> HostHasProfilePictureScore = 0;
        HostHasProfilePicture = 'no' -> HostHasProfilePictureScore = 0),

        % 7- Calcola il punteggio HostIdentifyVerifiedScore : 5 punti
        (HostIdentifyVerified = 't' -> HostIdentifyVerifiedScore = 5;
        HostIdentifyVerified = 'f' -> HostIdentifyVerifiedScore = 0;
        HostIdentifyVerified = 'no' -> HostIdentifyVerifiedScore = 0),

        % 8. Calcola il punteggio LastReviewScore : 5 punti
        % Controlla se LastReview è 'no_last_review'
        (LastReview = 'no_last_review' -> LastReviewScore = 0;
        % Altrimenti, estrai l'anno da LastReview
        sub_string(LastReview, 0, 4, _, YearStringLR),
        atom_number(YearStringLR, YearLastReview),
        % Calcola la differenza di anni
        YearDiffLR is 2022 - YearLastReview,
        % Assegna il punteggio in base alla differenza di anni
        (YearDiffLR = 0 -> LastReviewScore = 5;
        YearDiffLR = 1 -> LastReviewScore = 4;
        YearDiffLR = 2 -> LastReviewScore = 3;
        YearDiffLR = 3 -> LastReviewScore = 2;
        YearDiffLR = 4 -> LastReviewScore = 1;
        YearDiffLR >= 5 -> LastReviewScore = 0)),

        % 9. Calcola il punteggio ReviewScoreRatingScore : 10 punti
        (ReviewScoreRating = -1.0 -> ReviewScoreRatingScore = 0;
        ReviewScoreRating = 5.0 -> ReviewScoreRatingScore = 10;
        ReviewScoreRating >= 4.0, ReviewScoreRating <5 -> ReviewScoreRatingScore = 8;
        ReviewScoreRating >= 3.0, ReviewScoreRating <4 -> ReviewScoreRatingScore = 6;
        ReviewScoreRating >= 2.0, ReviewScoreRating <3 -> ReviewScoreRatingScore = 4;
        ReviewScoreRating >= 1.0, ReviewScoreRating <2 -> ReviewScoreRatingScore = 2;
        ReviewScoreRating = 0.0 -> ReviewScoreRatingScore = 0),

        % 10. Calcola il punteggio ReviewsPerMonthScore : 5 punti
        (ReviewsPerMonth = -1.0 -> ReviewsPerMonthScore = 0;
        ReviewsPerMonth >= 10.0 -> ReviewsPerMonthScore = 5;
        ReviewsPerMonth >= 8.0, ReviewsPerMonth <10 -> ReviewsPerMonthScore = 4;
        ReviewsPerMonth >= 6.0, ReviewsPerMonth <8 -> ReviewsPerMonthScore = 3;
        ReviewsPerMonth >= 4.0, ReviewsPerMonth <6 -> ReviewsPerMonthScore = 2;
        ReviewsPerMonth >= 1.0, ReviewsPerMonth <4 -> ReviewsPerMonthScore = 1;
        ReviewsPerMonth >= 0.0, ReviewsPerMonth <1 -> ReviewsPerMonthScore = 0),

        % 11. Calcola il punteggio IsntantBookableScore : 5 punti
        (IstantBookable = 't' -> IsntantBookableScore = 5;
        IstantBookable = 'f' -> IsntantBookableScore = 0;
        IstantBookable = 'no' -> IsntantBookableScore = 0),

        % 12. Calcola il punteggio di ReviewScoreAccuracyScore : 5 punti
        (ReviewScoreAccuracy = -1.0 -> ReviewScoreAccuracyScore = 0;
        ReviewScoreAccuracy = 5.0 -> ReviewScoreAccuracyScore = 5;
        ReviewScoreAccuracy >= 4.0, ReviewScoreAccuracy <5.0 -> ReviewScoreAccuracyScore = 4;
        ReviewScoreAccuracy >= 3.0, ReviewScoreAccuracy <4.0 -> ReviewScoreAccuracyScore = 3;
        ReviewScoreAccuracy >= 2.0, ReviewScoreAccuracy <3.0 -> ReviewScoreAccuracyScore = 2;
        ReviewScoreAccuracy >= 1.0, ReviewScoreAccuracy <2.0 -> ReviewScoreAccuracyScore = 1;
        ReviewScoreAccuracy = 0.0 -> ReviewScoreAccuracyScore = 0),
        
        % 13. Calcola il punteggio di NumbeOfReviewsScore : 5 punti
        (NumberOfReviews = -1 -> NumbeOfReviewsScore = 0;
        NumberOfReviews >= 500 -> NumbeOfReviewsScore = 5;
        NumberOfReviews >= 400, NumberOfReviews <500 -> NumbeOfReviewsScore = 4;
        NumberOfReviews >= 300, NumberOfReviews <400 -> NumbeOfReviewsScore = 3;
        NumberOfReviews >= 200, NumberOfReviews <300 -> NumbeOfReviewsScore = 2;
        NumberOfReviews >= 50, NumberOfReviews <200 -> NumbeOfReviewsScore = 1;
        NumberOfReviews < 50 -> NumbeOfReviewsScore = 0),

        % 14. Calcola il punteggio di NumbeOfReviewsLastYearScore : 5 punti
        (NumberOfReviewsLastYear = -1 -> NumbeOfReviewsLastYearScore = 0;
        NumberOfReviewsLastYear >= 50 -> NumbeOfReviewsLastYearScore = 5;
        NumberOfReviewsLastYear >= 40, NumberOfReviewsLastYear <50 -> NumbeOfReviewsLastYearScore = 4;
        NumberOfReviewsLastYear >= 30, NumberOfReviewsLastYear <40 -> NumbeOfReviewsLastYearScore = 3;
        NumberOfReviewsLastYear >= 20, NumberOfReviewsLastYear <30 -> NumbeOfReviewsLastYearScore = 2;
        NumberOfReviewsLastYear >= 10, NumberOfReviewsLastYear <20 -> NumbeOfReviewsLastYearScore = 1;
        NumberOfReviewsLastYear < 10 -> NumbeOfReviewsLastYearScore = 0),

        % 15. Calcola il punteggio di BedScore : 5 punti
        HalfAccomodates is Accomodates / 2,
        (NumberOfBeds >= HalfAccomodates -> BedScore = 5;
        NumberOfBeds < HalfAccomodates -> BedScore = 2),

        % 16. Calcola il punteggio di BedRoomsScore : 5 punti
        (Accomodates > 0 ->
        RatioBedRooms is float(NumberOfBedRooms) / float(Accomodates),
        (RatioBedRooms >= 0.333 -> BedRoomsScore = 5;
        RatioBedRooms >= 0.25, RatioBedRooms < 0.333 -> BedRoomsScore = 4;
        RatioBedRooms >= 0.2, RatioBedRooms < 0.25 -> BedRoomsScore = 3;
        RatioBedRooms >= 0.167, RatioBedRooms < 0.2 -> BedRoomsScore = 2;
        RatioBedRooms >= 0.143, RatioBedRooms < 0.167 -> BedRoomsScore = 1;
        RatioBedRooms < 0.143 -> BedRoomsScore = 0);
        BedRoomsScore = 0  % Se Accomodates è 0, assegna 0 punti
    ),

        HostScore is HostSinceScore + HostResponseTimeScore + HostResponseRateScore + HostAcceptanceRateScore + HostIsSuperHostScore + HostHasProfilePictureScore + HostIdentifyVerifiedScore + LastReviewScore + ReviewScoreRatingScore + ReviewsPerMonthScore + IsntantBookableScore + ReviewScoreAccuracyScore + NumbeOfReviewsScore + NumbeOfReviewsLastYearScore + BedScore + BedRoomsScore
    ).
    """
    # Scrivi la regola nel file Prolog
    write_prolog_rule(kb_path, regola)

    # Esegui la query Prolog e ottieni i risultati
    results_dict = query_prolog(kb_path)

    # Aggiorna il dataset con i risultati della query Prolog
    updated_dataset = update_dataset_with_prolog_results(dataset, results_dict)
    
    # Restituisci il dataset aggiornato
    return updated_dataset











































