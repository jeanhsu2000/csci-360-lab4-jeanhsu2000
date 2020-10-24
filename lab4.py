import numpy as np

from lab4_utils import feature_names, accuracy_score


# Hint: Consider how to utilize np.unique()
def preprocess_data(training_inputs, testing_inputs, training_labels, testing_labels):
    processed_training_inputs, processed_testing_inputs = ([], [])
    processed_training_labels, processed_testing_labels = ([], [])
    # VVVVV YOUR CODE GOES HERE VVVVV $

    # ^^^^^ YOUR CODE GOES HERE ^^^^^ $
    return (
        processed_training_inputs,
        processed_testing_inputs,
        processed_training_labels,
        processed_testing_labels,
    )


# Hint: consider how to utilize np.argsort()
def naive_bayes(predict_on, reference_points, reference_labels):
    # Here you should calculate the requisite probabilities from the reference points
    # and then use them to classify each test point. Don't forget to use Laplace smoothing
    assert (
        len(predict_on) > 0
    ), f"parameter predict_on needs to be of length 0 or greater"
    assert (
        len(reference_points) > 0
    ), f"parameter reference_points needs to be of length 0 or greater"
    assert (
        len(reference_labels) > 0
    ), f"parameter reference_labels needs to be of length 0 or greater"
    assert len(reference_labels) == len(reference_points), (
        f"reference_points and reference_labels need to be the" f" same length"
    )
    predictions = []
    # VVVVV YOUR CODE GOES HERE VVVVV $

    # ^^^^^ YOUR CODE GOES HERE ^^^^^ $
    return predictions


def cross_validate(
    training_inputs, testing_inputs, training_labels, testing_labels, k=5
):
    # Here you should re-split the dataset into folds, preprocess again,
    #   run through your naive bayes, and measure the accuracy for each fold.
    # See the test script for examples of part of this process.

    kf_ete = []  # array of k-fold cross validation estimates of test error

    # VVVVV YOUR CODE GOES HERE VVVVV $

    # ^^^^^ YOUR CODE GOES HERE ^^^^^ $
    return kf_ete
