import numpy as np
from scipy.stats import chisquare
from piperabm.tools.linear_algebra import refine


def chi_square(observed_frequencies, expected_probabilities):
    observed_frequencies = refine(observed_frequencies)
    expected_probabilities = refine(expected_probabilities)

    # The expected frequencies
    expected_frequencies = np.sum(observed_frequencies) * expected_probabilities

    # Perform the Chi-square test
    chi2_stat, p_value = chisquare(f_obs=observed_frequencies, f_exp=expected_frequencies)

    return chi2_stat, p_value


if __name__ == '__main__':
    #observed_frequencies = [4, 3, 2, 1]
    observed_frequencies = [4, 3, 4, 4]
    expected_probabilities = [0.25, 0.25, 0.25, 0.25]
    chi2_stat, p_value = chi_square(observed_frequencies, expected_probabilities)
    print(chi2_stat, p_value)

