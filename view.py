from flask import Flask, render_template, request, redirect, url_for
from model import DataModel
from logic import calculate_result

# ทำให้เว็บสามารถเรนเดอร์ไฟล์รูปภาพ และcssได้
app = Flask(__name__, template_folder='pages', static_url_path='/static')

# แสดงหน้าแรก
@app.route('/')
def home():
    # ดึงผลลัพธ์Result
    result = request.args.get('result', '') 
    # ดึงผลลัพธ์Percentage
    percentage = request.args.get('percentage', '')
    # ถ้าพบค่า Percentage
    if percentage:
        # แปลงPercentageให้เป็นทศนิยม
        percentage = float(percentage)

    # ตรวจสอบว่าผลลัพธ์และเปอร์เซ็นต์ว่างเปล่าหรือไม่ ให้แสดง home.html ก่อน
    if not result and not percentage:
        return render_template('home.html')

    # ถ้าpercentage และ result ไม่ Null ให้แสดงผลไปที่หน้า page1.html
    return render_template('result.html', result=result, percentage=percentage)

# สร้างแถว
@app.route('/create', methods=['POST'])
def create():
    # รับค่าจากหน้าเว็บมาเก็บในตัวแปร
    if request.method == 'POST':
        BMI = request.form['BMI']
        Smoking = request.form['Smoking']
        PhysicalHealth = request.form['PhysicalHealth']
        MentalHealth = request.form['MentalHealth']
        DiffWalking = request.form['DiffWalking']
        Sex = request.form['Sex']
        AgeCategory = request.form['AgeCategory']
        Diabetic = request.form['Diabetic']
        PhysicalActivity = request.form['PhysicalActivity']
        GenHealth = request.form['GenHealth']
        SleepTime = request.form['SleepTime']
        Asthma = request.form['Asthma']
        SkinCancer = request.form['SkinCancer']
        
        result, percentage = calculate_result(BMI, Smoking, PhysicalHealth, MentalHealth, DiffWalking,Sex,AgeCategory,Diabetic,PhysicalActivity,GenHealth,SleepTime,Asthma,SkinCancer)
        # Redirect to the home endpoint with the result and percentage as query parameters
        return redirect(url_for('home', result=result, percentage=percentage))
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
