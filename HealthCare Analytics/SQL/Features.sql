-- 1. Operational & Bed Utilization View
CREATE OR REPLACE VIEW vw_hospital_operations AS
SELECT 
    admission_type,
    los_tier,
    insurance_type,
    COUNT(*) AS total_admissions,
    ROUND(AVG(length_of_stay)::numeric, 2) AS avg_los_days,
    SUM(is_high_risk) AS high_risk_readmissions,
    ROUND((100.0 * SUM(is_high_risk) / COUNT(*))::numeric, 2) AS high_risk_pct,
    ROUND(AVG(procedures_count)::numeric, 2) AS avg_procedures
FROM patient_encounters
GROUP BY admission_type, los_tier, insurance_type;

-- 2. Clinical Risk & Lab Biomarkers View
CREATE OR REPLACE VIEW vw_clinical_risk_stratification AS
SELECT 
    age_group,
    glycemic_status,
    chronic_conditions,
    clinical_risk_score,
    COUNT(*) AS patient_volume,
    SUM(is_high_risk) AS high_risk_count,
    ROUND((100.0 * SUM(is_high_risk) / COUNT(*))::numeric, 2) AS readmission_rate_pct,
    ROUND(AVG(bmi)::numeric, 2) AS avg_bmi,
    ROUND(AVG(last_hemoglobin)::numeric, 2) AS avg_hemoglobin,
    ROUND(AVG(last_glucose)::numeric, 2) AS avg_glucose,
    ROUND(AVG(last_creatinine)::numeric, 2) AS avg_creatinine
FROM patient_encounters
GROUP BY age_group, glycemic_status, chronic_conditions, clinical_risk_score;

-- 3. Social Determinants of Health (SDoH) & Compliance View
CREATE OR REPLACE VIEW vw_sdoh_compliance AS
SELECT 
    social_support,
    followup_compliance,
    mental_health_issue,
    smoking_status,
    alcohol_use,
    COUNT(*) AS total_patients,
    SUM(is_high_risk) AS high_risk_patients,
    ROUND((100.0 * SUM(is_high_risk) / COUNT(*))::numeric, 2) AS high_risk_rate_pct
FROM patient_encounters
GROUP BY social_support, followup_compliance, mental_health_issue, smoking_status, alcohol_use;

SELECT * FROM vw_hospital_operations LIMIT 5;