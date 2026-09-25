DROP TABLE IF EXISTS patient_encounters;

CREATE TABLE patient_encounters (
    patient_id VARCHAR(100),
    age INT,
    gender VARCHAR(20),
    weight_kg INT,
    height_cm INT,
    bmi NUMERIC(5,2),
    num_previous_admissions INT,
    chronic_conditions VARCHAR(100),
    medications_count INT,
    last_hemoglobin NUMERIC(5,2),
    last_glucose NUMERIC(6,2),
    last_creatinine NUMERIC(5,2),
    admission_type VARCHAR(50),
    length_of_stay INT,
    procedures_count INT,
    smoking_status VARCHAR(50),
    alcohol_use VARCHAR(50),
    physical_activity VARCHAR(50),
    insurance_type VARCHAR(50),
    followup_compliance VARCHAR(50),
    social_support VARCHAR(50),
    mental_health_issue VARCHAR(10),
    readmission_risk VARCHAR(20),
    is_high_risk INT,
    age_group VARCHAR(20),
    los_tier VARCHAR(50),
    clinical_risk_score INT,
    glycemic_status VARCHAR(50)
);

SELECT 
    COUNT(*) AS total_records,
    SUM(is_high_risk) AS total_high_risk,
    ROUND(AVG(length_of_stay), 2) AS avg_los_days,
    ROUND(AVG(clinical_risk_score), 2) AS avg_clinical_score
FROM patient_encounters;