import numpy as np


class LaplaceDistribution:
    @staticmethod
    def mean_abs_deviation_from_median(x: np.ndarray):
        """Compute mean absolute deviation from the median for each feature.

        Args:
            x: numpy array of shape (n_objects, n_features)

        Returns:
            1D numpy array of shape (n_features,) with MAD from median.
        """
        x = np.asarray(x)
        if x.ndim == 1:
            x2 = x.reshape(-1, 1)
        elif x.ndim == 2:
            x2 = x
        else:
            raise ValueError("x must be a 1D or 2D numpy array")

        med = np.median(x2, axis=0)
        mad = np.mean(np.abs(x2 - med), axis=0)
        return mad

    def init(self, features):
        """Initialize Laplace distribution parameters using MLE.

        Args:
            features: numpy array of shape (n_objects, n_features)
        """
        features = np.asarray(features)
        if features.ndim == 1:
            features2 = features.reshape(-1, 1)
        elif features.ndim == 2:
            features2 = features
        else:
            raise ValueError("features must be a 1D or 2D numpy array")

        self.loc = np.median(features2, axis=0)
        self.scale = self.mean_abs_deviation_from_median(features2)
        # Avoid division by zero for constant features
        self.scale = np.maximum(self.scale, 1e-9)

    def logpdf(self, values):
        """Return log density for each object assuming independent features.

        Args:
            values: numpy array of shape (n_objects, n_features)

        Returns:
            1D numpy array of shape (n_objects,) with log pdf values.
        """
        values = np.asarray(values)
        if values.ndim == 1:
            values2 = values.reshape(-1, 1)
        elif values.ndim == 2:
            values2 = values
        else:
            raise ValueError("values must be a 1D or 2D numpy array")

        # Broadcasting: (n_objects, n_features)
        per_feature = -np.log(2.0 * self.scale) - np.abs(values2 - self.loc) / self.scale
        return np.sum(per_feature, axis=1)

    def pdf(self, values):
        """Return density for each object (exp of logpdf)."""
        return np.exp(self.logpdf(values))
