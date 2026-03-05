# import the libraries
import pandas as pd
import matplotlib.pyplot as plt

#import the data 
df=pd.read_csv(r"C:\Users\ayans\Downloads\netflix_titles.csv.zip")
print(df.head())

#cleaning data
df=df.dropna(subset=['type','title','release_year','rating','country','duration'])

type_counts=df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index,type_counts.values,color=['skyblue','orange'])
plt.title('NUMBERS OF MOVIE VS  TV SHOWS')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('movies_vs_tv_shows.png')
plt.show()


rating_counts=df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts,labels=rating_counts.index,autopct='%1.1f%%',startangle=90)
plt.title('PERCENTAGE OF CONTENT RATING ')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('content-rating-pie.png')
plt.show()

#DISTRIBUTION OF MOVIE DURATION USING HISTOGRAM

 
movie_df=df[df['type']=='Movie'].copy()
movie_df['duration_int']=movie_df['duration'].str.replace('min','').astype(int)
plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'],bins=30,color='purple',edgecolor='black')
plt.title('Distributions of Movie Duration')
plt.xlabel('Duration(minutes)')
plt.ylabel('No. of minutes')
plt.tight_layout()
plt.savefig('movie-duration-histogram.png')
plt.show()

#RELEASE YEAR VS NUMBER OF SHOWS USING SCATTERPLOT


release_counts=df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index,release_counts.values,color='red')
plt.title('RELEASE YEAR VS NUMBER OF SHOWS')
plt.xlabel('Release year')
plt.ylabel('Number of Shows')
plt.tight_layout()
plt.savefig('Release_year_shows_scatterplot.png')
plt.show()


#TOP 10 COUNTRIES WITH HIGHEST NUMBER OF SHOWS 


country_counts=df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index,country_counts.values,color='teal')
plt.title('TOP 10 COUNTRY WITH HIGHEST NUMBER OF SHOWS')
plt.xlabel('number of shows')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('Top10_countries.png')
plt.show()
