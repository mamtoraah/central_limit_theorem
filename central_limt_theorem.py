"""Code to simulate the Central Limit Theorem"""
import random
from typing import List
import matplotlib.pyplot as plt
import statistics


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


def generate_sample_mean_list(population: List[int], sample_size: int, sample_count: int) -> List[int]:
    """From the population generate samples of size: sample_size and sample_count number of times

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


def plot_hist(population, ax):
    plt.hist(population, 100)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Histogram of Population of Random Numbers")
    plt.text(0.8, 0.8, f"population_size={len(population)}", horizontalalignment='center',
             verticalalignment='center', transform=ax.transAxes)
    plt.grid(True)
    plt.show()


def main():
    """Driver function"""
    fig, ax = plt.subplots()
    population_size = int(1E5)
    population = create_population(population_size)
    plot_hist(population, ax)
    plt.hist(population, 100)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Histogram of Population of Random Numbers")
    plt.text(0.8, 0.8, f"population_size={population_size}", horizontalalignment='center',
             verticalalignment='center', transform=ax.transAxes)
    plt.grid(True)
    plt.show()

    sample_size_list = [10, 20]
    sample_count_list = [1000, 5000]

    for sample_size in sample_size_list:
        for sample_count in sample_count_list:
            sample_mean_list = generate_sample_mean_list(
                population, sample_size, sample_count)

            # also called as mean of sample distribution of sample means
            mean_of_sample_means = statistics.mean(sample_mean_list)

            # also called standard deviation of sample distribution of sample means
            std_error = statistics.stdev(sample_mean_list)

            plt.hist(sample_mean_list, 100)
            plt.xlabel("Mean Value")
            plt.ylabel("Frequency")
            plt.title("Histogram of Sample Means")
            plt.text(0.8, 0.9, f"sample_count={sample_count}", horizontalalignment='center',
                     verticalalignment='center', transform=ax.transAxes)
            plt.text(0.8, 0.85, f"sample_size={sample_size}", horizontalalignment='center',
                     verticalalignment='center', transform=ax.transAxes)
            plt.text(0.8, 0.8, f"mean_of_sample_means={mean_of_sample_means}", horizontalalignment='center',
                     verticalalignment='center', transform=ax.transAxes)
            plt.text(0.8, 0.75, f"std_error={std_error}", horizontalalignment='center',
                     verticalalignment='center', transform=ax.transAxes)
            plt.grid(True)
            plt.show()


if __name__ == "__main__":
    main()
