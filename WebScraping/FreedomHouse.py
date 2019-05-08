import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("https://freedomhouse.org/report/countries-world-freedom-2019")

# Create a BeautifulSoup object asdf
soup = BeautifulSoup(page.text, "html.parser")

# get the country list
country = soup.find(class_="views-table cols-7")

# find all instances (should be over 200)
country_list_e = country.find_all(class_="even")
# country_list_o = country.find_all(class_="odd")

# print(len(country_list_e))
print(len(country_list_e))

# open writer with name
file_name = "FreedomHouse2019_E.csv"
# set newline to be ' ' so that new rows are appended without skipping any
f = csv.writer(open(file_name, "w", encoding="utf-8", newline=""))

# write a new row as a headder
f.writerow(["CountryName", "PR_Score", "CL_Score", "FreedomRating", "Aggrigrate_Score"])

for country in country_list_e:
    # find the first <a> tag and get the text
    name = country.find(class_="views-field views-field-title").text.strip()
    pr_score = country.find(
        class_="views-field views-field-field-fiw-pr-rating"
    ).text.strip()
    cl_score = country.find(
        class_="views-field views-field-field-fiw-cl-rating"
    ).text.strip()
    free_rating = country.find(
        class_="views-field views-field-field-fiw-combined-score"
    ).text.strip()
    agg_score = country.find(
        class_="views-field views-field-field-fiw-aggregate-score"
    ).text.strip()
    print("name")
    print("pr_score")
    print("cl_score")
    print("free_rating")
    print("agg_score")
    print("Writing rows")
    # add the information as a row into the csv table
    f.writerow([name, pr_score, cl_score, free_rating, agg_score])

# for country in country_list_o:
# find the first <a> tag and get the text
#   name = country.find(class_="views-field views-field-title").text.strip()
#  pr_score = country.find(
#     class_="views-field views-field-field-fiw-pr-rating"
# ).text.strip()
# cl_score = country.find(
#   class_="views-field views-field-field-fiw-cl-rating"
# ).text.strip()
# free_rating = country.find(
#   class_="views-field views-field-field-fiw-combined-score"
# ).text.strip()
# agg_score = country.find(
#   class_="views-field views-field-field-fiw-aggregate-score"
# ).text.strip()
# print("name", name)
# print("pr", pr_score)
# print("cl", cl_score)
# print("free", free_rating)
# print("agg", agg_score)
# print("Writing rows")
# add the information as a row into the csv table
# f.writerow([name, pr_score, cl_score, free_rating, agg_score])
