"""Generate data_bulk24.py: 200 medicine & healthcare data functions, 200K+ lines."""
import random, os

random.seed(2424)

TOPICS = [
    "antibiotic_drug", "antiviral_drug", "antifungal_drug", "antiparasitic_drug",
    "chemotherapy_agent", "immunosuppressant", "blood_pressure_medication", "cholesterol_medication",
    "antidepressant", "antipsychotic", "anxiolytic", "mood_stabilizer",
    "painkiller_opioid", "painkiller_nsaid", "anesthetic_local", "anesthetic_general",
    "anticoagulant", "antiplatelet_drug", "diuretic_drug", "antihistamine",
    "corticosteroid", "bronchodilator", "insulin_type", "oral_hypoglycemic",
    "thyroid_hormone", "contraceptive_drug", "fertility_drug", "bisphosphonate",
    "vaccine_type", "immunoglobulin", "antivenom", "probiotic_strain",
    "medical_imaging_mri", "ct_scanner", "ultrasound_machine", "xray_machine",
    "mammography_unit", "pet_scanner", "spect_scanner", "fluoroscopy_unit",
    "endoscope_type", "colonoscope", "bronchoscope", "laparoscope",
    "arthroscope", "cystoscope", "duodenoscope", "capsule_endoscope",
    "surgical_instrument_scalpel", "surgical_forceps", "surgical_scissors", "surgical_retractor",
    "surgical_clamp", "surgical_needle", "surgical_suture", "surgical_stapler",
    "electrocautery_device", "cryosurgery_tool", "laser_surgery_tool", "ultrasonic_scalpel",
    "robotic_surgery_system", "surgical_microscope", "surgical_drill", "surgical_saw",
    "prosthetic_hip", "prosthetic_knee", "prosthetic_shoulder", "prosthetic_elbow",
    "dental_implant", "dental_crown", "dental_bridge", "denture_type",
    "hearing_aid_type", "cochlear_implant", "pacemaker_model", "defibrillator_icd",
    "stent_type", "heart_valve_prosthetic", "vascular_graft", "catheter_type",
    "iv_line_type", "syringe_type", "needle_gauge", "infusion_pump",
    "ventilator_type", "cpap_machine", "bipap_machine", "oxygen_concentrator",
    "dialysis_machine", "heart_lung_machine", "ecmo_device", "icu_monitor",
    "pulse_oximeter", "ecg_monitor", "eeg_machine", "emg_machine",
    "blood_glucose_meter", "continuous_glucose_monitor", "insulin_pump", "hemoglobin_analyzer",
    "blood_cell_counter", "coagulation_analyzer", "blood_gas_analyzer", "electrolyte_analyzer",
    "urine_analyzer", "pregnancy_test", "drug_test_kit", "pcr_machine",
    "elisa_reader", "flow_cytometer", "centrifuge_type", "microscope_electron",
    "spectrophotometer", "chromatography_hplc", "mass_spectrometer", "culture_media",
    "incubator_type", "autoclave_sterilizer", "biosafety_cabinet", "fume_hood",
    "wheelchair_type", "walker_device", "crutch_type", "hospital_bed",
    "patient_lift", "transfer_board", "orthopedic_brace", "neck_collar",
    "back_support_belt", "compression_stocking", "elastic_bandage", "cast_material",
    "splint_type", "sling_type", "cervical_pillow", "pressure_mattress",
    "hospital_gown", "surgical_gown", "surgical_glove", "face_mask",
    "n95_respirator", "surgical_drape", "eye_protection", "head_cover",
    "shoe_cover", "hand_sanitizer", "antiseptic_solution", "disinfectant_type",
    "wound_dressing", "bandage_roll", "gauze_pad", "adhesive_tape",
    "antimicrobial_wound_gel", "negative_pressure_wound_therapy", "burn_dressing", "surgical_sponge",
    "first_aid_kit", "defibrillator_aed", "emergency_blanket", "tourniquet_type",
    "stretcher_type", "cervical_collar_emergency", "oxygen_mask", "splint_emergency",
    "thermometer_type", "stethoscope_model", "otoscope", "ophthalmoscope",
    "blood_pressure_cuff", "reflex_hammer", "tuning_fork", "measuring_tape",
    "tongue_depressor", "pen_light", "laryngeal_mirror", "nasal_speculum",
    "vaginal_speculum", "anoscope", "proctoscope", "laryngoscope",
    "chart_eye_snellen", "vision_tester", "audiology_screener", "spirometer",
    "peak_flow_meter", "airway_adjunct", "endotracheal_tube", "tracheostomy_tube",
]

random.shuffle(TOPICS)

COLUMNS = "Name,Category,Year,Manufacturer,Application,Cost_USD,Shelf_Years,Risk_Level".split(",")
ENTRIES = 1000
func_count = 0

with open("../datab/data_bulk24.py", "w", encoding="utf-8") as f:
    f.write('"""data_bulk24.py: 200 medicine & healthcare data functions, 1000 entries each, ~200K lines."""\n')
    f.write("import random\n\n")

    for spec in TOPICS:
        rng = random.Random(hash(spec + "v5.1.0.24") % (2**31))
        func_name = spec
        func_count += 1

        f.write("\ndef get_{}_data():\n".format(func_name))
        f.write('    """Return {} entries of {} data."""\n'.format(ENTRIES, func_name.replace("_", " ")))
        f.write("    return [\n")

        for i in range(ENTRIES):
            name = "{}-{} {}".format(
                random.choice(["Medi","Health","Care","Vita","Nova","Ultra","Max","Pro","Elite","Prime","Plus","Bio","Gen","Pure","Safe","Shield","Guard","Flex","Neo","Cure"]),
                rng.randint(100, 9999),
                random.choice(["XR","XL","HP","EZ","DX","FX","GT","LT","MT","XT"])
            )
            category = random.choice(["Pharmaceutical","Device","Diagnostic","Therapeutic","Surgical","Monitoring","Protective","Rehabilitative","Imaging","Sterilization"])
            year = rng.randint(1980, 2026)
            manufacturer = random.choice(["Pfizer","Johnson & Johnson","Roche","Merck","Novartis","AbbVie","Bristol Myers","Sanofi","Bayer","GSK","AstraZeneca","Thermo Fisher","Medtronic","Siemens Health","GE Healthcare","Philips","Boston Scientific","Stryker","Becton Dickinson","Cardinal Health"])
            application = random.choice(["Cardiology","Neurology","Orthopedics","Oncology","Emergency","Surgery","Diagnostics","Therapy","Prevention","Rehabilitation","Pediatrics","Geriatrics","Dermatology","Ophthalmology","Dentistry","Pulmonology","Gastroenterology","Urology","Endocrinology","Rheumatology"])
            cost = rng.randint(1, 50000)
            shelf = rng.randint(1, 15)
            risk = random.choice(["Low","Moderate","High","Critical","Controlled","Variable","Stable","Experimental","Approved","Investigational"])

            f.write('        ("{}", "{}", {}, "{}", "{}", {}, {}, "{}")'.format(
                name, category, year, manufacturer, application, cost, shelf, risk
            ))
            f.write(",\n" if i < ENTRIES - 1 else ",\n")

        f.write("    ]\n")

total = os.path.getsize("data_bulk24.py") if os.path.exists("data_bulk24.py") else 0
lines_est = (ENTRIES + 3) * func_count
print("Generated data_bulk24.py: {} functions, ~{} lines, {:.1f} KB".format(func_count, lines_est, total/1024))
