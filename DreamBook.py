import matplotlib.pylab as plt
import pandas as pd

from abc import ABC, abstractmethod
class Analysis(ABC):
    @abstractmethod
    def  performAnalysis():
        pass
    
#1- Publications trends over time
class PublicationTrend(Analysis):  # Count of books published per year
    def performAnalysis(self):
        df = pd.read_csv('DataBook.csv') #load dataset
        df.columns = df.columns.str.strip().str.lower()
        # Extract year from publication date
        df['year'] = df['publication date'].astype(str).str[:4]
        # Group by year and count
        df2 = df.groupby('year').size().reset_index(name='Book Count')
        print(df2)
        # Plot bar chart
        plt.bar(df2['year'], df2['Book Count'], color='Purple')
        plt.title('Books Published Per Year')
        plt.xlabel('Year')
        plt.ylabel('Book Count')
        plt.show()




#2- Top most Prolific Authors
class TopFiveAnalysis(Analysis):  # Top 5 Most Prolific Authors (Authors with the highest number of books)
    def performAnalysis(self):
        # Load the dataset
        df1 = pd.read_csv('DataBook.csv')
        # Group by author and count the number of books
        df2 = df1.groupby(['author']).size().reset_index(name='Top 5 authors')
        print(df2)
        # Get the top 5 authors with the most books
        df3 = df2.nlargest(5, 'Top 5 authors')
        print(df3)
        # Draw bar chart: Authors on X-axis, Count on Y-axis
        plt.bar(df3['author'], df3['Top 5 authors'], color=['pink', 'orange', 'green', 'blue', 'yellow'])
        plt.title('Top 5 Most Prolific Authors')
        plt.xlabel('Authors')
        plt.ylabel('Count')
        plt.tight_layout()  # Ensures labels and title fit well
        plt.show()


#3 - Language distribution of books
class LanguageDistribution(Analysis):  # Distribution of books by language
    def performAnalysis(self):
        df = pd.read_csv('DataBook.csv')
        df.columns = df.columns.str.strip().str.lower()
        # Group by language and count
        df2 = df.groupby('language').size().reset_index(name='Book Count')
        print(df2)
        # Plot bar chart
        plt.bar(df2['language'], df2['Book Count'], color=['lightblue','pink','yellow','orange','red','lightgreen'])
        plt.title('Language Distribution of Books')
        plt.xlabel('Language')
        plt.ylabel('Book Count')
        plt.show()


#4 - Number of books published by each publisher
class PublisherDistribution(Analysis):
    def performAnalysis(self):
        df = pd.read_csv('DataBook.csv')
        df.columns = df.columns.str.strip().str.lower()
        top_publishers = (df.groupby('book publisher').size().nlargest(10).reset_index(name='Number of Books'))
        print(top_publishers)
        plt.bar(top_publishers['book publisher'], top_publishers['Number of Books'], color='orange')
        plt.title('Top 10 Publishers by Number of Books')
        plt.xlabel('Publisher')
        plt.ylabel('Number of Books')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        


#5- missing ISBN analysis
class MissingISBN(Analysis):  # Missing ISBN Analysis
    def performAnalysis(self):
        df = pd.read_csv('DataBook.csv')  
        null_count = df['ISBN'].isnull().sum() # count rows where student is null
        print('Count of null values in ISBN column:', null_count)
        row_count = len(df)
        print('Number of rows:', row_count)
        per = null_count / row_count * 100
        print('Percentage of null ISBN is', per)
        non_null_count = df['ISBN'].notnull().sum()
        print('Count of non-null ISBNs:', non_null_count)
        # Values and labels
        values = [null_count, non_null_count]
        labels = ['Null ISBN', 'Not Null ISBN']
        # Plot pie chart
        plt.figure(figsize=(5, 5))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'lightblue'])
        plt.title('Percentage of Null ISBN')
        plt.axis('equal')  # Ensures the pie is a perfect circle
        plt.show()


# 6 - Number of books published per year categorized by language
class YearLanguageAnalysis(Analysis):  # Number of books per year categorized by language
    def performAnalysis(self):
        df1 = pd.read_csv('DataBook.csv')
        df1.columns = df1.columns.str.strip().str.lower()  # Normalize column names
        # Group by year and language, then count
        df2 = df1.groupby(['publication date', 'language']).size().reset_index(name='Count of Books')
        # Pivot for grouped bar chart
        df3 = df2.pivot(index='publication date', columns='language', values='Count of Books').fillna(0)
        print("Number of Books Published per Year Categorized by Language")
        print(df3)
        # Draw Bar Chart - Years on X Axis, Book Count by Language on Y Axis
        df3.plot(kind='bar', figsize=(10, 6))
        plt.title('Books Published per Year by Language')
        plt.xlabel('Publication Year')
        plt.ylabel('Count of Books')
        plt.legend(title='Language')
        plt.tight_layout()
        plt.show()




class  ProcessStrategy:
    def  executeStrategy( self, analysis_obj ):
        analysis_obj.performAnalysis()
 
            
class  StrategySelector:                                           
    def  openMenu(self):
        while (True):
            print ("Dream Book Shop - Dataset Analysis System")
            print ("1 - Books Published Per Year")
            print ("2 - Top Five Authors")
            print ("3 - Language distribution of books")
            print ("4 - Number of books published by each publisher ")
            print ("5 - Missing ISBN Analysis")
            print ("5 - Branch Enrollments Income for a Given Year")
            print ("6 - Exit")
            choice = int ( input ("Enter Choice: [1|2|3|4|5|6|7] "))
            if (choice<1  or choice>7):
                print ("Invalid Choice")
            else:
                ps = ProcessStrategy()
                if (choice==1):
                    ba_object =  PublicationTrend()
                    ps.executeStrategy(ba_object)
                if (choice ==2):
                     ta_object = TopFiveAnalysis()
                     ps.executeStrategy(ta_object) 
                if (choice ==3):
                    ld_object = LanguageDistribution()
                    ps.executeStrategy(ld_object)
                if (choice ==4):
                    pd_object = PublisherDistribution()
                    ps.executeStrategy(pd_object)
                if (choice ==5):
                    mi_object = MissingISBN()
                    ps.executeStrategy(mi_object)
                if (choice ==6):
                    yla_object = YearLanguageAnalysis()
                    ps.executeStrategy(yla_object)
                if (choice ==7):
                    print ("******** END *********")          
                    break;





class  Admin:
    count=0
    def  __init__(self, UserName, Password):
        if  (Admin.count == 0):
            self.username = UserName
            self.password = Password
            Admin.count = Admin.count + 1
        else:
            print ("Admin already exists")
    
    def  login(self):
        print('WELCOME TO DREAM BOOK SHOP')
        print ( 'DATA ANALYSIS SYSTEM')
        UserName = input ("Enter User Name: ")
        Password= input ("Enter Password: ")
        if  (UserName == self.username and Password == self.password):
            s1 = StrategySelector()
            s1.openMenu()
        else:
            print ("Incorrect User Name OR Password")
            
if __name__ == "__main__":
    a1 = Admin("Imara", "imara123")
    a1.login()
