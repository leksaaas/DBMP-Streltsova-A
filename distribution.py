import numpy as np

class LaplaceDistribution:
    @staticmethod
    def mean_abs_deviation_from_median(x: np.ndarray):
        ####
        # Do not change the class outside of this block
        median = np.median(x, axis=0)
        return np.mean(np.abs(x - median), axis=0)
        ####

    def __init__(self, features):
        ####
        # Do not change the class outside of this block
        features = np.asarray(features)
        if features.ndim == 1:
            features = features[:, None]

        self.loc = np.median(features, axis=0)
        self.scale = self.mean_abs_deviation_from_median(features)
        ####

    def logpdf(self, values):
        ####
        # Do not change the class outside of this block
        values = np.asarray(values)
        if values.ndim == 1:
            values = values[:, None]

        return -np.log(2 * self.scale) - np.abs(values - self.loc) / self.scale
        ####

    def pdf(self, values):
        return np.exp(self.logpdf(values))
