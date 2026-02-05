from fastapi import FastAPI
import pandas as pd
from sqlalchemy import create_engine
import os

app = FastAPI()
engine = create_engine(os.getenv("DATABASE_URL"))

@app.get("/api/metrics")
def get_metrics():
    df = pd.read_sql("SELECT * FROM admissions", engine)
    
    # Calculate ALOS (Average Length of Stay)
    df['stay_duration'] = (pd.to_datetime(df['discharge_date']) - pd.to_datetime(df['admit_date'])).dt.days
    alos = df['stay_duration'].mean()
    
    # Calculate Readmission Rate
    readmission_rate = (df['readmission_30d'].sum() / len(df)) * 100
    
    return {
        "Average_Length_of_Stay": round(alos, 2),
        "Readmission_Rate": f"{round(readmission_rate, 2)}%",
        "Total_Records": len(df)
    }
