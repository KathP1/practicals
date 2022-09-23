"""
A program that simulates a population of gophers
over a ten-year period
and displays each year's population size
"""
import random

NUMBER_OF_YEARS = 10


def main():
    population = 1000
    births = 0
    deaths = 0
    print("Welcome to the Gopher Population Simulator! "
          "\nStarting population:", population,
          "\nYear 1\n")
    for i in range(1, NUMBER_OF_YEARS, 1):
        proportion_of_births = random.randint(10, 20) / 100
        births = births + (population * proportion_of_births)
        proportion_of_deaths = random.randint(5, 25) / 100
        deaths = deaths + (population * proportion_of_deaths)
        population = population + births - deaths
        print("{:.0f}".format(births), "gophers were born.", "{:.0f}".format(deaths), "died."
              "\nPopulation: {:.0f}".format(population),
              "\nYear", i + 1, "\n")


main()
