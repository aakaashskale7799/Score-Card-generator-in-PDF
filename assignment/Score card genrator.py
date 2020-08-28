# -*- coding: utf-8 -*-
"""
percentile pending
"""
from fpdf import FPDF
import pandas as pd
import random
import csv
import numpy as np 
import matplotlib.pyplot as plt 
#If your data is in xlsx format yoou can convert it to csv for future use other wise its ok 
data_xls = pd.read_excel('Assignment.xlsx', 'Raw data', index_col=None)

#converted and saved i csv format
data_xls.to_csv('test1.csv', encoding='utf-8', index=False)
data=pd.read_csv("test1.csv")

#Title of the report card you can write it here or esle inside the method
title = 'Test Report'

#These are the name of columns used to show case details of the student as shown in the sample pdf
details=["Name of Candidate","Grade ","Name of school ",
             "City of Residence","Country of Residence","Registration",
             "Gender","Date of Birth ","Date and time of test", "Extra time assistance" ]

#lets start
class PDF(FPDF):
    #This is for header of the pdf . Displayed on all pages
     def header(self):
        #This is kind of shortcut I have used instead of coloring background
        #image(name, width , height  , size)
        self.image('bg.png', 0.01, 0.01, 900)
        self.image('logo_pb.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        #self.set_draw_color(109, 189, 78)
        self.set_draw_color(0, 0, 0)
        self.set_fill_color(5, 109, 170)
        self.set_text_color(1, 0, 6)
        # Thickness of frame (1 mm)
        self.set_line_width(0.3)
        # Title
        #cell(width , height, text, border(0,1),nextline or not, align, bg paint )
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Line break
        self.ln(10)
        
        
     #Body of the pdf
     def chapter_body(self, name,i,P_image):
        # Read text file
        # Times 12
        #self.set_text_color(7, 165, 228)# light blue
        self.set_text_color(147,193,61)# light green
        #to add new page
        self.add_page()
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, name)
        # Line break
        self.ln()
        #self.line(Abscissa of first point, Ordinate of first point, 
        #Abscissa of second point,Ordinate of second point)
        self.line(10, 42, 203, 42)
        self.line(10, 50, 203, 50)
        self.line(10, 92, 203, 92)
        self.line(10, 100, 203, 100)
        # Mention in Bold
        self.set_font('', 'B')
        data=pd.read_csv("test1.csv")
        #here i is registration number of the student
        student1=data.loc[data["Registration"]==i]
        #image of the student given in the profile folder
        self.image(P_image+".jpg",150,8,33)
        #==========================================================================================
        #dtails table
        k=new[["Name of Candidate","Grade ","Name of school ","City of Residence", "Country of Residence",
               "Registration","Gender","Date of Birth ","Date and time of test", "Extra time assistance"]]
        #this is to create data to list of list in order to generate table out of it
        xyz=k.values.tolist()
        xyz=xyz[0]
        detail_table=[['Name of Candidate', xyz[0], 'Registration No', xyz[5]],
                       ['Grade',xyz[1],'Gender',xyz[6]],
                       ['School Name ',xyz[2],'Date of birth',xyz[7]],
                       ['City of Residence',xyz[3],'Date of Test ',xyz[8]],
                       ["Country of Residence",xyz[4],"Extra Time assistance",xyz[9]]]
        self.set_font('Times','',9.9)
        epw = self.w - 1.7*self.l_margin
        col_width = epw/4
        self.set_font('Times','B',14.0) 
        self.ln(7)
        self.cell(epw, 0.0, 'Student Details', align='C')
        self.set_font('Times','',10.0) 
        self.ln(7)
        th = pdf.font_size
        #Table creation and printing into the pdf directly
        for row in detail_table:
            for datum in row:
                self.cell(col_width, 2*th, str(datum), border=1, align='C')
            self.ln(2*th)            
        #=======================================================================================
        #marks_table
        table=student1
        table["What you marked"].fillna("None", inplace = True)
        table=table[["Question No.","Time Spent on question (sec)","Score if correct",
                      "Score if incorrect", "Attempt status ","What you marked","Correct Answer",
                      "Outcome (Correct/Incorrect/Not Attempted)","Your score"]]
        heading=["Question No.","Time (sec)","If correct",
                      "If incorrect", "Attempt status","Your Answer","Correct Answer",
                      "Outcome","Score"]
        xyz=table.values.tolist()
        xyz.insert(0,heading)
        self.set_font('Times','',9.9)
        epw = self.w - 1.7*self.l_margin
        col_width = epw/9
        self.set_font('Times','B',14.0) 
        self.ln(7)
        self.cell(epw, 0.0, 'Student Performance', align='C')
        self.set_font('Times','',10.0) 
        self.ln(7)
        th = pdf.font_size
        for row in xyz:
            for datum in row:
                self.cell(col_width, 2*th, str(datum), border=1, align='C')
            self.ln(2*th)
        #================================================================================================
        marks=data.loc[data["Registration"]==i]
        total_marks=marks["Your score"].sum()
        display_marks=("Total Score : "+ str(total_marks))
        #display_marks=("Your over all percentile : "+str(display_marks))
        self.set_font('Times','B',14.0)
        #===================================================================
        self.cell(100,10,display_marks)
        self.ln(7)
     #Footer of the pdf   
     def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'B', 8)
        # Text color in gray
        self.set_text_color(147,193,61)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')
     #lets start with figures 
     #5 figures are designed and displayed into the pdf
     def fig1(self,img1,percentile):
         epw = self.w - 1.7*self.l_margin
         self.set_font('Times','B',14.0)
         display_percentile="Your overall percentile "+ str(percentile)
         self.set_font('Times','B',14.0)
         self.cell(100,10, display_percentile, align='L')
         self.ln()
         self.line(10, 161, 203, 161)
         self.line(10, 169, 203, 169)
         self.cell(epw, 8, 'Let\'s visualize the report in detail', align='C')
         self.ln(1)
         self.image(img1, 10 ,173,90)
     def fig2(self,img2):
         self.image(img2, 110 ,173,90)
     def fig3(self, img3):
         self.image(img3,10,35,90)
     def fig4(self, img4):
         self.image(img4,110,35,90)
     def fig5(self, img5):
         self.image(img5,10,135,90)
#P_image=str(P_image)
P_image=0
dho=[]
rai=[]
all_ranks=[]
counter=0
for i in data["Registration"].unique():
    dho.append(i)
    row=data.loc[data["Registration"]==i]
    total=row["Your score"].sum()
    rai.append(total)
df=pd.DataFrame(list(zip(dho,rai)),columns=["a","b"]).sort_values(by="b", ascending=False)
df.reset_index(drop=True, inplace=True)
for l in data["Registration"].unique():
    rank=df[df['a']==l].index.item()+1
    below=len(df['a'])-rank
    #print(str(l) + "persentage "+ str(rank)+" below "+ str(below))
    perc=(below/len(df["a"]))*100
    all_ranks.append(perc)
df=pd.DataFrame(list(zip(dho,rai,all_ranks)),columns=["a","b","rank"]).sort_values(by="b", ascending=False)
df.reset_index(drop=True, inplace=True) 
       
for i in data["Registration"].unique():
    P_image=P_image+1
    P_image=str(P_image)
    print(i)
    new=data.loc[data["Registration"]==i]
    #i=90991233
    per=df[df["a"]==i].index.item()
    percentile=df.at[per, "rank"]
    print(percentile)
    #===========================================================================================
    #===========================================================================================
    #===========================================================================================
    #bar graph
    ques=new["Question No."]
    secs=new["Time Spent on question (sec)"]
    fig,ax = plt.subplots(figsize =(4, 4))
    plt.grid(b = True, color ='red', linestyle ='-.', linewidth = 1,alpha = 0.2)
    plt.ylabel('Seconds you took')
    plt.xlabel('Question number')
    plt.title("Time taken for each question in seconds")
    ax.legend(new["Question No."])
    ques_sec=ax.bar(ques,secs)
    plt.savefig(r"C:\Users\User\Desktop\assignment\fig\."+str(i)+"_bar")
    plt.close()
    #Question vs seconds done here saved as registration number
    #===========================================================================================
    #===========================================================================================
    #===========================================================================================
    #pie chart 1
    #now time spend as a function of total time
    labels=new["Question No."]
    sizes=new["Time Spent on question (sec)"]
    fig1, ax1 = plt.subplots(figsize =(4, 4))
    wedges,texts, autotexts=ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.legend(new["Question No."])
    plt.title("Time spent as a funtion of a total time")
    plt.savefig(r"C:\Users\User\Desktop\assignment\fig\."+str(i)+"_pie1")
    plt.close()
    #===========================================================================================
    #===========================================================================================
    #===========================================================================================
    #3rd 
    att=0
    unatt=0
    for a in new["Attempt status "]:
        if a=="Attempted":
            att=att+1
        if a=="Unattempted":
            unatt=unatt+1   
    size=[att,unatt]
    labels=["Attempted","Unattempted"]      
    fig2, ax2 = plt.subplots(figsize =(4, 4))
    wedges,texts, autotexts=ax2.pie(size, autopct='%1.1f%%',shadow=True,startangle=90)
    ax2.axis('equal')
    ax2.legend(new["Attempt status "].sort_values().unique())
    plt.title("Attempts",loc="left")
    plt.savefig(r"C:\Users\User\Desktop\assignment\fig\."+str(i)+"_pie2")
    plt.close()
    #===========================================================================================
    #4th    
    correct=0
    incorrect=0
    atmp=0
    for a in new["Outcome (Correct/Incorrect/Not Attempted)"]:
        if a =="Correct":
            correct=correct+1
        if a =="Incorrect":
            incorrect=incorrect+1
        if a=="Unattempted":
            atmp=atmp+1
    size=[correct,incorrect]
    labels=["Correct","Incorrect"]
    fig3, ax3 = plt.subplots(figsize =(4, 4))
    wedges,texts, autotexts=ax3.pie(size,  autopct='%1.1f%%',shadow=True,startangle=90)
    ax3.axis('equal')
    plt.title("Accuracy from attemped Questions",loc="left")
    new["legend"] = new["Outcome (Correct/Incorrect/Not Attempted)"].map({'Correct': 'Correct', 'Incorrect': "Incorrect","Unattempted":"Incorrect"})
    ax3.legend(new["legend"].sort_values().unique())
    plt.savefig(r"C:\Users\User\Desktop\assignment\fig\."+str(i)+"_pie3")
    plt.close()
    #====================================================================================================
    #5th
    correct=0
    incorrect=0
    atmp=0
    for a in new["Outcome (Correct/Incorrect/Not Attempted)"]:
        if a =="Correct":
            correct=correct+1
        if a =="Incorrect":
            incorrect=incorrect+1
        if a=="Unattempted":
            atmp=atmp+1
    size=[correct,atmp,incorrect]
    labels=["Correct","Unattempted","Incorrect"]
    fig3, ax3 = plt.subplots(figsize =(4, 4))
    wedges,texts, autotexts=ax3.pie(size,  autopct='%1.1f%%',shadow=True,startangle=90)
    ax3.axis('equal')
    ax3.legend(["Correct","Unattempted", "incorrect"])
    plt.title("Overall performace against the test",loc="left")
    plt.savefig(r"C:\Users\User\Desktop\assignment\fig\."+str(i)+"_pie4")
    plt.close()
    #==========================================================================================
    #percentile

    
    pdf = PDF()
    pdf.chapter_body(" ",i,P_image)
    #pdf.perct(i)
    i=str(i)
    pdf.fig1(r"C:\Users\User\Desktop\assignment\fig\."+i+"_bar.png",percentile)
    pdf.fig2(r"C:\Users\User\Desktop\assignment\fig\."+i+"_pie1.png")
    pdf.add_page()
    pdf.fig3(r"C:\Users\User\Desktop\assignment\fig\."+i+"_pie2.png")
    pdf.fig4(r"C:\Users\User\Desktop\assignment\fig\."+i+"_pie3.png")
    pdf.fig5(r"C:\Users\User\Desktop\assignment\fig\."+i+"_pie4.png")
    P_image=int(P_image)    
    pdf.output(r"C:\Users\User\Desktop\assignment\product\."+i+".pdf", "F")
    plt.close()