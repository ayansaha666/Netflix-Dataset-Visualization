## Netflix Dataset Analysis and Visualization

## Project Overview

This project performs **Exploratory Data Analysis (EDA)** on the Netflix titles dataset using Python.
The goal is to analyze different aspects of Netflix content such as:

* Number of **Movies vs TV Shows**
* **Content rating distribution**
* **Movie duration distribution**
* **Release year vs number of shows**
* **Top countries producing Netflix content**

The analysis is done using **data cleaning, aggregation, and visualization techniques**.

---

## Dataset

The dataset used is the **Netflix Titles Dataset**, which contains information about movies and TV shows available on Netflix.

Important columns used in this project:

* `type` – Movie or TV Show
* `title` – Title of the content
* `release_year` – Year the content was released
* `rating` – Content rating (PG, TV-MA, etc.)
* `country` – Country of production
* `duration` – Duration of movie or TV show

Dataset file used:

```
netflix_titles.csv.zip
```

---

## Libraries Used

The following Python libraries are used in this project:

* pandas
* matplotlib

Install them using:

```
pip install pandas matplotlib
```

---

## Project Workflow

### 1. Data Loading

The dataset is loaded using pandas.

```
df = pd.read_csv("netflix_titles.csv.zip")
```

---

### 2. Data Cleaning

Missing values are removed from important columns to ensure accurate analysis.

```
df = df.dropna(subset=['type','title','release_year','rating','country','duration'])
```

---

## Visualizations Generated

### 1. Movies vs TV Shows

A **bar chart** showing the number of movies and TV shows available on Netflix.

Output file:

```
movies_vs_tv_shows.png
```

---

### 2. Content Rating Distribution

A **pie chart** showing the percentage distribution of different content ratings.

Output file:

```
content-rating-pie.png
```

---

### 3. Movie Duration Distribution

A **histogram** showing the distribution of movie durations.

Output file:

```
movie-duration-histogram.png
```

---

### 4. Release Year vs Number of Shows

A **scatter plot** showing how many shows were released each year.

Output file:

```
Release_year_shows_scatterplot.png
```

---

### 5. Top 10 Countries with Most Shows

A **horizontal bar chart** showing the top 10 countries producing Netflix content.

Output file:

```
Top10_countries.png
```

---

## Project Structure

```
Netflix-Data-Analysis
│
├── netflix_titles.csv.zip
├── netflix_analysis.py
├── README.md
│
├── movies_vs_tv_shows.png
├── content-rating-pie.png
├── movie-duration-histogram.png
├── Release_year_shows_scatterplot.png
└── Top10_countries.png
```

---

## How to Run the Project

1. Clone the repository

```
git clone <your-repository-link>
```

2. Navigate to the project folder

```
cd Netflix-Data-Analysis
```

3. Run the Python script

```
python netflix_analysis.py
```

The script will generate and save all visualizations.

---

## Key Learning Outcomes

* Data cleaning using **pandas**
* Exploratory Data Analysis (EDA)
* Data aggregation using `value_counts()`
* Data visualization using **matplotlib**
* Saving plots as image files

---

## Author

**Ayan Saha**
BS Data Science – IIT Madras
Interested in **Artificial Intelligence, Machine Learning, and Natural Language Processing research**
