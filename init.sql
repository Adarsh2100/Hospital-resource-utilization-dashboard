CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    age INT,
    gender VARCHAR(10),
    insurance_type VARCHAR(50)
);

CREATE TABLE admissions (
    admission_id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(patient_id),
    department VARCHAR(50), -- Cardiology, Oncology, Pediatrics, etc.
    branch VARCHAR(50),
    admit_date TIMESTAMP,
    discharge_date TIMESTAMP,
    outcome VARCHAR(20), -- Recovered, Improved, Deceased
    total_cost DECIMAL(10, 2),
    readmission_30d BOOLEAN DEFAULT FALSE
);
