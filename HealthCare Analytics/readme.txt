================================================================================
HOSPITAL INPATIENT FLOW & CLINICAL RISK COMMAND CENTER
================================================================================

1. PROJECT OVERVIEW
--------------------------------------------------------------------------------
An executive-level clinical analytics dashboard developed in Power BI Desktop[cite: 3], 
connecting to a PostgreSQL relational database[cite: 3]. The system tracks inpatient 
flow, bed utilization bottlenecks, 30-day high-risk readmissions, metabolic 
and renal biomarkers, and Social Determinants of Health (SDoH) across 10,000 
patient encounters[cite: 2, 3].


2. TECHNICAL ARCHITECTURE & ENVIRONMENT
--------------------------------------------------------------------------------
- Database Engine: PostgreSQL 
- Database Name: Healthcare_analytics (localhost:5432)
- Schema / Table: public.patient_encounters (9,999 rows)[cite: 1]
- Pipeline: Python (Pandas + SQLAlchemy) for data staging
- Modeling Layer: PostgreSQL analytical views
- BI Platform: Power BI Desktop[cite: 3]
- Calculation Engine: Dedicated DAX Measures table (_Measures)[cite: 1]


3. DASHBOARD VISUAL HIERARCHY
--------------------------------------------------------------------------------

[TOP SECTION: FILTERS & SLICERS]
- Admission Type Slicer: Elective, Emergency, Urgent[cite: 3]
- Age Group Slicer: 18-35, 36-50, 51-65, 65+[cite: 3]
- Insurance Type Slicer: Private, Medicare, Medicaid[cite: 3]

[ROW 1: EXECUTIVE KPI SUMMARY CARDS]
- Total Patient Inflow: 10K encounters[cite: 3]
- High Risk Readmission Rate: 33.3%[cite: 3]
- Avg Length of Stay: 15.1 Days[cite: 3]
- Total Inpatient Bed Days: 151K Days[cite: 3]
- Avg Clinical Risk Score: 2.21 Acuity Index[cite: 3]

[ROW 2: CLINICAL RISK & POPULATION STRATIFICATION]
- Top Left: Renal vs. Glycemic Acuity Profile (Scatter Chart)
  * X-axis: Average Blood Glucose (last_glucose)[cite: 2, 3]
  * Y-axis: Average Serum Creatinine (last_creatinine)[cite: 2, 3]
  * Legend / Category: chronic_conditions[cite: 2, 3]
  * Size: Total Encounters[cite: 1, 2]

- Top Middle: Readmission Risk Distribution by Chronic Comorbidity (100% Stacked Bar)[cite: 3]
  * Y-axis: Chronic Conditions (Diabetes, Hypertension, COPD, Heart Disease)[cite: 3]
  * X-axis: Total Encounters[cite: 1, 3]
  * Legend: Readmission Risk Tier (High, Medium, Low)[cite: 3]

- Top Right: High-Risk Patient Volume by Payer Mix (Donut Chart)[cite: 3]
  * Legend: insurance_type (Uninsured, Private, Public)[cite: 2, 3]
  * Values: High Risk Encounters[cite: 1, 3]

[ROW 3: INTAKE BIOMARKERS, SDoH & BED BOTTLENECK]
- Bottom Left: Clinical Biomarker Profile across Intake Types (Matrix Table)[cite: 3]
  * Rows: glycemic_status (Hyperglycemic, Normal, Pre-Diabetic)[cite: 3]
  * Columns: admission_type (Elective, Emergency, Urgent)[cite: 3]
  * Values: Total Encounters, Avg Glucose Level, Avg Hemoglobin, High Risk Readmission Rate[cite: 3]

- Bottom Middle: High-Risk Encounter Distribution by SDoH & Compliance (Clustered Bar Chart)[cite: 3]
  * Y-axis: followup_compliance (Good, Poor)[cite: 2, 3]
  * X-axis: High Risk Encounters[cite: 1, 3]
  * Legend: social_support (Strong, Weak)[cite: 2, 3]

- Bottom Right: Bed Utilization vs. 30-Day Readmission Risk by LoS Tier (Line & Column Chart)[cite: 3]
  * X-axis: los_tier (Short, Medium, Extended, Long-term)[cite: 3]
  * Column Y-axis: Total Encounters[cite: 1, 3]
  * Line Y-axis: High Risk Readmission Rate[cite: 1, 3]


4. CORE DAX MEASURES SPECIFICATION
--------------------------------------------------------------------------------

Total Encounters = 
COUNTROWS('public patient_encounters')

High Risk Encounters = 
CALCULATE(
    COUNTROWS('public patient_encounters'),
    'public patient_encounters'[is_high_risk] = 1
)

High Risk Readmission Rate = 
DIVIDE([High Risk Encounters], [Total Encounters], 0)

Avg Length of Stay = 
AVERAGE('public patient_encounters'[length_of_stay])

Total Inpatient Bed Days = 
SUM('public patient_encounters'[length_of_stay])

Avg Clinical Risk Score = 
AVERAGE('public patient_encounters'[clinical_risk_score])

Avg Glucose Level = 
AVERAGE('public patient_encounters'[last_glucose])

Avg Hemoglobin = 
AVERAGE('public patient_encounters'[last_hemoglobin])

Hyperglycemic Encounter Rate = 
DIVIDE(
    CALCULATE(
        [Total Encounters], 
        'public patient_encounters'[glycemic_status] = "Hyperglycemic (>140)"
    ),
    [Total Encounters],
    0
)

Extended Stay Patient Volume = 
CALCULATE(
    [Total Encounters],
    'public patient_encounters'[length_of_stay] > 7
)

Low Compliance Volume = 
CALCULATE(
    [Total Encounters],
    'public patient_encounters'[followup_compliance] = "Poor"
)

Low Compliance Readmission Rate = 
DIVIDE(
    CALCULATE(
        [High Risk Encounters], 
        'public patient_encounters'[followup_compliance] = "Poor"
    ),
    CALCULATE(
        [Total Encounters], 
        'public patient_encounters'[followup_compliance] = "Poor"
    ),
    0
)


5. REPRODUCTION & DEPLOYMENT STEPS
--------------------------------------------------------------------------------
1. Ensure PostgreSQL is active on port 5432 and the table
   'public.patient_encounters' is populated with 9,999 rows[cite: 1].
2. Open Power BI Desktop -> Home -> Get Data -> PostgreSQL Database[cite: 3].
3. Server: localhost:5432 | Database: Healthcare_analytics.
4. Import 'public patient_encounters'[cite: 1, 3].
5. Create a disconnected Home Table named '_Measures' and add all DAX calculations[cite: 1, 3].
6. Apply page background color #F1F5F9 (0% transparency).
7. Assemble slicers, cards, and visuals using a consistent card container style:
   - Background: #FFFFFF
   - Border: Solid #E2E8F0 (6px rounded corners)
   - Shadow: Subtle Bottom-Right
================================================================================