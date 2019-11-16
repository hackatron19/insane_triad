# @author : grvkmrpandit
#actual program for ml
import numpy as np
import pandas as pd
import sys, json
from itertools import chain 


l2=[]
#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    #get our data as an array from read in()
    lines = read in().split('.\n')

    # Sum  of all the items in the providen array
    l2.append(lines)
l1 = list(chain.from_iterable(l2))































l1=['back pain','constipation','abdominal pain','diarrhoea','mild fever','yellow urine',
'yellowing of eyes','acute liver failure','fluid overload','swelling of stomach',
'swelled lymph nodes','malaise','blurred and distorted vision','phlegm','throat irritation',
'redness of eyes','sinus pressure','runny nose','congestion','chest pain','weakness in limbs',
'fast heart rate','pain during bowel movements','pain in anal region','bloody stool',
'irritation in anus','neck pain','dizziness','cramps','bruising','obesity','swollen legs',
'swollen blood vessels','puffy face and eyes','enlarged thyroid','brittle nails',
'swollen extremeties','excessive hunger','extra marital contacts','drying and tingling lips',
'slurred speech','knee pain','hip joint pain','muscle weakness','stiff neck','swelling joints',
'movement stiffness','spinning movements','loss of balance','unsteadiness',
'weakness of one body side','loss of smell','bladder discomfort','foul smell of urine',
'continuous feel of urine','passage of gases','internal itching','toxic look (typhos)',
'depression','irritability','muscle pain','altered sensorium','red spots over body','belly pain',
'abnormal menstruation','dischromic  patches','watering from eyes','increased appetite','polyuria','family history','mucoid sputum',
'rusty sputum','lack of concentration','visual disturbances','receiving blood transfusion',
'receiving unsterile injections','coma','stomach bleeding','distention of abdomen',
'history of alcohol consumption','fluid overload','blood in sputum','prominent veins on calf',
'palpitations','painful walking','pus filled pimples','blackheads','scurring','skin peeling',
'silver like dusting','small dents in nails','inflammatory nails','blister','red sore around nose',
'yellow crust ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# TESTING DATA df -------------------------------------------------------------------------------------
df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

# print(df.head())

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)
# print(y)

# TRAINING DATA tr --------------------------------------------------------------------------------
tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)
# --------------------------------------------decision tree ----------------------------------------------------------

def DecisionTree():

    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
    clf3 = clf3.fit(X,y)

    # calculating accuracy-------------------------------------------------------------------
    #from sklearn.metrics import accuracy score
    #y pred=clf3.predict(X test)
    #print(accuracy score(y test, y pred))
    #print(accuracy score(y test, y pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = l1  #[Symptom1,Symptom2,Symptom3,Symptom4,Symptom5]

    for k in range(0,len(l1)):
        # print (k,)
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    #ans='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            print(disease[a])
            #ans='yes'
            break
DecisionTree()
