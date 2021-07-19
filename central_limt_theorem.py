"""Code to simulate the Central Limit Theorem"""
import random
from typing import List
import matplotlib.pyplot as plt
import matplotlib
import statistics
import pandas as pd
import math


def create_population(sample_size: int) -> List[int]:
    """Generate a population of sample_size

    Args:
        sample_size (int): The size of the population

    Returns:
        List[int]: a list of randomly generated integers
    """
    population = []
    for _ in range(sample_size):
        random_number = (random.randint(0, random.randint(1, 1000)))
        population.append(random_number)
    return population


def generate_sample_mean_list(population: List[int],
                              sample_size: int,
                              sample_count: int) -> List[int]:
    """From the population generate samples of sample_size, sample_count times

    Args:
        population (List[int]): List of random numbers
        sample_size (int): Number of elements in each sample
        sample_count (int): Number of sample means in sample_mean_list

    Returns:
        List[int]: a list of sample means
    """
    sample_mean_list = []
    for _ in range(sample_count):
        sample = random.sample(population, sample_size)
        sample_mean = statistics.mean(sample)
        sample_mean_list.append(sample_mean)
    return sample_mean_list


def plot_hist(data: List[int],
              ax: matplotlib.axes.Axes,
              xlabel: str,
              ylabel: str,
              title: str,
              texts: List[str]) -> None:
    """Plot a histogram with labels and additional texts

    Args:
        data (List[int]): the list of data points to be plotted
        ax (matplotlib.axes.Axes): Axes object for text plotting
        xlabel (str): label on x axis
        ylabel (str): label on y axis
        title (str): title of the plot
        texts (List[str]): Additional texts to be plotted
    """
    plt.hist(data, 100)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    i = 0.0
    for text in texts:
        plt.text(0.8,
                 0.8 - i,
                 text,
                 horizontalalignment="center",
                 verticalalignment="center",
                 transform=ax.transAxes)
        i += 0.05
    plt.grid(True)
    plt.show()


def main(plot=True):
    """Driver Function

    Args:
        plot (bool, optional): Decide whether to plot or not. Defaults to True.
    """
    fig, ax = plt.subplots()
    population_size = int(1E5)
    population = create_population(population_size)
    if plot:
        plot_hist(population,
                  ax,
                  "Value",
                  "Frequency",
                  "Histogram of Population of Random Numbers",
                  [f"population_size={population_size}"])

    population_mean = statistics.mean(population)
    population_stdev = statistics.stdev(population)

    sample_size_list = [50, 500]
    sample_count_list = [500, 5000]

    records = []
    for sample_size in sample_size_list:
        for sample_count in sample_count_list:
            sample_mean_list = generate_sample_mean_list(
                population, sample_size, sample_count)

            # also called as mean of sample distribution of sample means
            mean_of_sample_means = round(statistics.mean(sample_mean_list), 2)

            # also called standard dev of sample distribution of sample means
            std_error = round(statistics.stdev(sample_mean_list), 2)
            if plot:
                plot_hist(sample_mean_list,
                          ax,
                          "Mean Value",
                          "Frequency",
                          "Sampling Distribution of Sample Means",
                          [
                              f"sample_count={sample_count}",
                              f"sample_size={sample_size}",
                              f"mean_of_sample_means={mean_of_sample_means}",
                              f"std_error={std_error}"])

            record = {
                "sample_size": sample_size,
                "sample_count": sample_count,
                "population_mean": population_mean,
                "sample_mean": mean_of_sample_means,
                "population_stdev": population_stdev,
                "population_stdev_using_formula": std_error*math.sqrt(sample_size),
                "sample_stdev": std_error,
            }

            records.append(record)

    df = pd.DataFrame(records)
    print(df)


if __name__ == "__main__":
    main(plot=False)
