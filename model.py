# Import libraries
import mysql.connector
from decimal import Decimal

# ทำโมเดล+เขียนคำสั่ง SQL
class DataModel:
    def __init__(self, BMI, Smoking, PhysicalHealth, MentalHealth, DiffWalking,Sex,AgeCategory,Diabetic,PhysicalActivity,GenHealth,SleepTime,Asthma,SkinCancer):
        self.BMI = BMI
        self.Smoking = Smoking
        self.PhysicalHealth = PhysicalHealth
        self.MentalHealth = MentalHealth
        self.DiffWalking = DiffWalking
        self.Sex = Sex
        self.AgeCategory = AgeCategory
        self.Diabetic = Diabetic
        self.PhysicalActivity = PhysicalActivity
        self.GenHealth = GenHealth
        self.SleepTime = SleepTime
        self.Asthma = Asthma
        self.SkinCancer = SkinCancer

    @staticmethod
    def connector():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ppgdmild",
            database="heartdb"
        )
        return connection

    # insertแถวลงในDatabase
    def insert(self, result, percentage):
        # เชื่อมต่อฐานข้อมูล
        connection = DataModel.connector()
        cursor = connection.cursor()
        query = "INSERT INTO hearttable (BMI, Smoking, PhysicalHealth, MentalHealth, DiffWalking, Sex, AgeCategory, Diabetic, PhysicalActivity, GenHealth, SleepTime, Asthma, SkinCancer, result, percentage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try: 
            values = (self.BMI, self.Smoking, self.PhysicalHealth, self.MentalHealth, self.DiffWalking, self.Sex, self.AgeCategory, self.Diabetic, self.PhysicalActivity, self.GenHealth, self.SleepTime, self.Asthma, self.SkinCancer, result, percentage)
            cursor.execute(query, values)
            connection.commit()
            return cursor.lastrowid
        except Exception as e: #กรณีที่ insert แล้วเกิด error
            print(f"Error: {e}")
            return None