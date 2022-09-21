import tkinter as tk
import boto3
dinesh=tk.Tk()
dinesh.geometry("400x240")
dinesh.title("Sentiment Analysis")
textExample=tk.Text(dinesh,height=10)
textExample.pack()
def getText():
    aws_mag_con=boto3.session.Session(profile_name="demo_user")
    client=aws_mag_con.client(service_name='comprehend',region_name="us-east-1")
    result=textExample.get("1.0","end")#Reading from first line to end
    print(result)
    response = client.detect_sentiment(Text=result,LanguageCode='en')
    #print('The prominent sentiment is:',response['Sentiment'])
    #print('The SentimentScore is:',response['SentimentScore'])
    print(response)
b1=tk.Button(dinesh,height=1,width=10,text="Read",command=getText)#Created button Read
b1.pack()
dinesh.mainloop()