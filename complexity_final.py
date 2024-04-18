import ijson
import csv
import os

def complexity(filename):
    ad_count = 0
    charLen = 0.0
    numSen = 0.0
    numWords = 0.0
    senLen = 0.0

    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for text in csv_reader:
            ad_count += 1
            word_count, sentence_count = average_sentence_length(text[0])
            charLen += len(text[0])
            numSen += sentence_count
            numWords += word_count
            if sentence_count != 0:
                senLen += (word_count / sentence_count)

    charLen /= ad_count
    numSen /= ad_count
    numWords /= ad_count
    senLen /= ad_count

    return ad_count, charLen, numSen, numWords, senLen

def append_to_csv(file_path, data):
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

def average_sentence_length(text):
    sentence_endings = ['.', '!', '?']
    word_count = 0
    sentence_count = 0
    in_word = False

    for char in text:
        if char in sentence_endings:
            sentence_count += 1
            in_word = False
        elif char.isalpha():
            if not in_word:
                word_count += 1
                in_word = True
        else:
            in_word = False

    if sentence_count == 0:
        return 0, 0  # To avoid division by zero
    return word_count, sentence_count

filenames = ['ad_text/abortion_text.csv', 'ad_text/adhd_text.csv', 'ad_text/aids_text.csv', 'ad_text/alcohol consumption_text.csv', 'ad_text/animal viruses_text.csv', 'ad_text/antibiotic_text.csv', 'ad_text/antidepressants_text.csv', 'ad_text/anxiety_text.csv', 'ad_text/artificial kidney_text.csv', 'ad_text/assisted living_text.csv', 'ad_text/autoantibodies_text.csv', 'ad_text/autoimmune disease_text.csv', 'ad_text/bariatric surgery_text.csv', 
             'ad_text/barr virus_text.csv', 'ad_text/behavioral therapy_text.csv', 'ad_text/birth_text.csv', 'ad_text/blisters_text.csv', 'ad_text/blood cancer_text.csv', 'ad_text/blood_text.csv', 'ad_text/body temperature_text.csv', 'ad_text/body weight_text.csv', 'ad_text/body_text.csv', 'ad_text/brain injuries_text.csv', 'ad_text/brain_text.csv', 'ad_text/breast cancer_text.csv', 'ad_text/calories_text.csv', 'ad_text/cancer_text.csv',
             'ad_text/cannabis_text.csv', 'ad_text/cardiovascular disease_text.csv', 'ad_text/caregiver_text.csv', 'ad_text/cells_text.csv', 'ad_text/chest_text.csv', 'ad_text/child health_text.csv', 'ad_text/childhood obesity_text.csv', 'ad_text/climate anxiety_text.csv', 'ad_text/cognitive health_text.csv', 'ad_text/coma_text.csv', 'ad_text/congenital syphilis_text.csv', 'ad_text/covid_text.csv', 
             'ad_text/death_text.csv', 'ad_text/dementia_text.csv', 'ad_text/dengue_text.csv', 'ad_text/diabetes_text.csv', 'ad_text/dietary guidelines_text.csv', 'ad_text/dignified death_text.csv', 'ad_text/disease_text.csv', 'ad_text/disorder_text.csv', 'ad_text/dissociation_text.csv', 'ad_text/doctor_text.csv', 'ad_text/doxy-pep_text.csv', 'ad_text/drug companies_text.csv', 'ad_text/drug_text.csv', 'ad_text/dry skin_text.csv', 'ad_text/endometrial cancer_text.csv', 
             'ad_text/epidemic_text.csv', 'ad_text/epstein-barr virus_text.csv', 'ad_text/esophagus_text.csv', 'ad_text/extreme pain_text.csv', 'ad_text/eye care_text.csv', 'ad_text/fascia_text.csv', 'ad_text/fentanyl_text.csv', 'ad_text/fertility_text.csv', 'ad_text/fever_text.csv', 'ad_text/firearm injuries_text.csv', 'ad_text/flu_text.csv', 'ad_text/gene_text.csv', 'ad_text/genetic disease_text.csv', 'ad_text/global health_text.csv', 'ad_text/gonorrhea_text.csv', 
             'ad_text/gunshot wound_text.csv', 'ad_text/hair follicle cell_text.csv', 'ad_text/health economist_text.csv', 'ad_text/health equity_text.csv', 'ad_text/health worker_text.csv', 'ad_text/hearing loss_text.csv', 'ad_text/heart disease_text.csv', 'ad_text/heart failure_text.csv', 'ad_text/heart_text.csv', 'ad_text/heat exposure_text.csv', 'ad_text/hepatitis_text.csv', 'ad_text/hernia_text.csv', 'ad_text/high blood pressure_text.csv', 'ad_text/hiv_text.csv', 
             'ad_text/home health care_text.csv', 'ad_text/hospital_text.csv', 'ad_text/illness_text.csv', 'ad_text/immune response_text.csv', 'ad_text/immunization_text.csv', 'ad_text/indoor air quality_text.csv', 'ad_text/infant mortality_text.csv', 'ad_text/infection_text.csv', 'ad_text/influenza_text.csv', 'ad_text/injectable drug_text.csv', 'ad_text/injury_text.csv', 'ad_text/insurance_text.csv', 'ad_text/internet addiction_text.csv', 'ad_text/ketamine_text.csv', 
             'ad_text/kidney disease_text.csv', 'ad_text/life expectancy_text.csv', 'ad_text/life insurance_text.csv', 'ad_text/listeria_text.csv', 'ad_text/liver cancer_text.csv', 'ad_text/long covid_text.csv', 'ad_text/long-term care_text.csv', 'ad_text/lung cancer_text.csv', 'ad_text/major depressive disorder_text.csv', 'ad_text/malaria_text.csv', 'ad_text/marijuana_text.csv', 'ad_text/maternal deaths_text.csv', 
             'ad_text/medicaid_text.csv', 'ad_text/medical evacuation_text.csv', 'ad_text/medical facilities_text.csv', 'ad_text/medical insurance_text.csv', 'ad_text/medical record_text.csv', 'ad_text/medical service_text.csv', 'ad_text/medical worker_text.csv', 'ad_text/medicare_text.csv', 'ad_text/medication_text.csv', 'ad_text/memory_text.csv', 'ad_text/mental health_text.csv', 'ad_text/metabolic disease_text.csv', 'ad_text/metabolites_text.csv', 'ad_text/meth_text.csv', 
             'ad_text/Mounjaro_text.csv', 'ad_text/mouth_text.csv', 'ad_text/mrna vaccine_text.csv', 'ad_text/multiple sclerosis_text.csv', 'ad_text/muscle soreness_text.csv', 'ad_text/neurodegenerative disease_text.csv', 'ad_text/neurosurgery_text.csv', 'ad_text/nurse_text.csv', 'ad_text/nursing home_text.csv', 'ad_text/obesity drug_text.csv', 'ad_text/obesity_text.csv', 'ad_text/opioid_text.csv', 'ad_text/organ transplant_text.csv', 'ad_text/organ_text.csv', 
             'ad_text/osha_text.csv', 'ad_text/ovarian cancer_text.csv', 'ad_text/ozempic_text.csv', 'ad_text/pain_text.csv', 'ad_text/parkinson_text.csv', 'ad_text/patients_text.csv', 'ad_text/pediatric cancer_text.csv', 'ad_text/pediatric obesity_text.csv', 'ad_text/pet scan_text.csv', 'ad_text/physician-assisted suicide_text.csv', 'ad_text/pill_text.csv', 'ad_text/pregnant women_text.csv', 'ad_text/premature babies_text.csv', 'ad_text/preventive medicine_text.csv', 'ad_text/private treatment_text.csv', 
             'ad_text/psilocybin_text.csv', 'ad_text/psychedelics_text.csv', 'ad_text/psychiatry_text.csv', 'ad_text/ptsd_text.csv', 'ad_text/public health_text.csv', 'ad_text/respiratory virus_text.csv', 'ad_text/serotonin_text.csv', 'ad_text/sex problems_text.csv', 'ad_text/sickle cell_text.csv', 'ad_text/side effects_text.csv', 'ad_text/skin_text.csv', 'ad_text/smoking rate_text.csv', 'ad_text/soreness_text.csv', 'ad_text/sperm_text.csv', 
             'ad_text/sti_text.csv', 'ad_text/stomach_text.csv', 'ad_text/stroke_text.csv', 'ad_text/suicide_text.csv', 'ad_text/surgery_text.csv', 'ad_text/syphilis_text.csv', 'ad_text/tb_text.csv', 'ad_text/technology addiction_text.csv', 'ad_text/teen suicide_text.csv', 'ad_text/teeth_text.csv', 'ad_text/telehealth_text.csv', 'ad_text/therapy_text.csv', 'ad_text/tirzepatide_text.csv', 'ad_text/tobacco_text.csv', 'ad_text/traumatic brain injuries_text.csv', 
             'ad_text/traumatic memory_text.csv', 'ad_text/treatment_text.csv', 'ad_text/tumor_text.csv', 'ad_text/umbilical cord_text.csv', 'ad_text/unhealthy indoor air_text.csv', 'ad_text/unvaccinated children_text.csv', 'ad_text/uterine cancer_text.csv', 'ad_text/vaccine_text.csv', 'ad_text/virus_text.csv', 'ad_text/wegovy_text.csv', 'ad_text/weight gain_text.csv', 'ad_text/weight loss_text.csv', 'ad_text/weight-loss drug_text.csv', 'ad_text/workout_text.csv', 
             'ad_text/wound_text.csv', 'ad_text/Zepbound_text.csv']

for filename in filenames:
    keyword = os.path.basename(filename).split('_')[0]
    count, charLen, numSen, numWords, senLen = complexity(filename)

    csv_file_path = 'complexityFinal.csv'
    new_line = [keyword] + [count] + [charLen] + [numWords] + [numSen] + [senLen]
    append_to_csv(csv_file_path, new_line)
    print(new_line)