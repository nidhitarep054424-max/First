#print("Hello World")
#with open("sample.txt","r") as file:
    #print(file.read())
#with open("sample.txt","w")as file:
    #file.write("Hello Python")
#with open("sample.txt","a") as file:
    #file.write("\nHello!")
import pandas as pd
df = pd.read_csv("product-translation-ai-1000.csv")
print(df)
