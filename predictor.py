import pandas as pd
import numpy as np

def predict():
    #Importing datasets
    train_variants = pd.read_csv("training_variants.csv")
    train_text = pd.read_csv("train_csv.csv")
    test_variants = pd.read_csv("test_variants.csv")
    test_text = pd.read_csv("test_csv.csv")
    
    #Pre-processing train_data
    Text_train = train_text.loc[:,["Text"]]
    a = []
    for i in Text_train.iterrows():
      index, data = i
      a.append(list(data))
    
    corpus_train=[]
    for i in range(3316):
      corpus_train.extend(a[i])
    
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(max_features = 1200)
    X = cv.fit_transform(corpus_train).toarray()
    X = pd.DataFrame(X)
    
    #Transforming data
    train_variants = train_variants.drop(columns=["ID"])
    y_train = train_variants["Class"]
    del train_variants["Class"]
    train_variants = pd.get_dummies(train_variants,drop_first=True)
    train_variants2 = train_variants.join(X,how='outer')
    
    #Transforming test_data
    Text_test = test_text.loc[:,["Text"]]
    a1 = []
    for i in Text_test.iterrows():
        index, data = i
        a1.append(list(data))
      
    corpus_test=[]
    for i in range(367):
        corpus_test.extend(a1[i])
    
    X_test = cv.transform(corpus_test).toarray()
    
    test_variants = test_variants.drop(columns=["ID"])
    y_test = test_variants["Class"]
    del test_variants["Class"]
    test_variants = pd.get_dummies(test_variants,drop_first=True)
    X_test=pd.DataFrame(X_test)
    test_variants2 = test_variants.join(X_test,how='outer')
    
    #Gettinng common columns so as to keep number of features same
    common_columns = train_variants2.columns.intersection(test_variants2.columns)
    
    #Changing train_variants2
    train_columns_remove = train_variants2.columns.difference(common_columns)
    train_variants2 = train_variants2.drop(columns=train_columns_remove)
    
    #Changing test_variants2
    test_columns_remove = test_variants2.columns.difference(common_columns)
    test_variants2 = test_variants2.drop(columns=test_columns_remove)
    
    from keras.models import load_model
    classification = load_model("model3.h5")
    
    #Getting user input
    sample = pd.read_csv("sample1.csv")
    sampleA = sample.loc[:,["Gene","Variation"]]
    sampleB = sample.loc[:,["Text"]]
    
    #Transforming input_data
    input_test = sampleB
    a2 = []
    for i in input_test.iterrows():
        index, data = i
        a2.append(list(data))
      
    corpus_input=[]
    for i in range(1):
        corpus_input.extend(a2[i])
    
    input_test_transform = cv.transform(corpus_input).toarray()
    
    sampleA = pd.get_dummies(sampleA,drop_first=True)
    input_test_transform=pd.DataFrame(input_test_transform)
    input_variants = sampleA.join(input_test_transform,how='outer')
    
    #Changing input_variants
    input_columns_remove = input_variants.columns.difference(common_columns)
    input_variants = input_variants.drop(columns=input_columns_remove)
    x = 1348-len(input_variants.columns)
    y = input_variants.shape[0]
    matrix = np.zeros(x*y)
    matrix = matrix.reshape(y,x)
    matrix = pd.DataFrame(matrix)
    input_variants = pd.concat([input_variants, matrix], axis=1, sort=False)
    
    result = classification.predict(input_variants)
    result = pd.DataFrame(result)
    result = result.idxmax(axis=1)
    print(result.values)
    
    return result.values