SELECT 
    COUNT(*) AS total_records,
    SUM(is_high_risk) AS total_high_risk,
    ROUND(AVG(length_of_stay), 2) AS avg_los_days,
    ROUND(AVG(clinical_risk_score), 2) AS avg_clinical_score
FROM patient_encounters;