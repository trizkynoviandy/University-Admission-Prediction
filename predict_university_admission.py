import joblib
import pandas as pd

def input_data(x1, x2, x3, x4, x5, x6, x7):
    input_data = [[x1, x2, x3, x4, x5, x6, x7]]
    new_data = pd.DataFrame(input_data, 
                            columns = ['GRE Score', 
                                       'TOEFL Score', 
                                       'University Rating', 
                                       'SOP', 
                                       'LOR ', 
                                       'CGPA', 
                                       'Research'])
    return new_data

def prediction(model, data):
    result = model.predict(data)
    return result[0]

if __name__ == "__main__" :
    model = joblib.load("model/university_admission.sav")
    print('\n----------------University Admission Prediction----------------\n')
    print("""This project aims to predict the likelihood of a student 
          being admitted to a university using linear regression\n""")
    print('Please input the variables: ')
    var_1 = input('1. GRE Score: ')
    var_2 = input('2. TOEFL Score: ')
    var_3 = input('3. University Rating: ')
    var_4 = input('4. SOP: ')
    var_5 = input('5. LOR: ')
    var_6 = input('6. CGPA: ')
    var_7 = input('7. Research: ')
    new_data = input_data(var_1, var_2, var_3, var_4, var_5, var_6, var_7)
    predict = prediction(model, new_data)
    print(f"Admission Chance: {predict:.2f}")