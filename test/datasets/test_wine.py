# This code is part of Qiskit.
#
# (C) Copyright IBM 2020, 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

""" Test Wine """

import unittest
from test import QiskitMachineLearningTestCase
import json
import numpy as np
from qiskit_machine_learning.datasets import wine


class TestWine(QiskitMachineLearningTestCase):
    """Wine tests."""

    def test_wine(self):
        """Wine test."""

        input_file = self.get_resource_path("wine_ref.json", "datasets")
        with open(input_file, encoding="utf8") as file:
            ref_data = json.load(file)

        training_features, training_labels, test_features, test_labels = wine(
            training_size=20, test_size=10, n=2, plot_data=False, one_hot=False
        )

        np.testing.assert_almost_equal(ref_data["training_features"], training_features)
        np.testing.assert_almost_equal(ref_data["training_labels"], training_labels)

        np.testing.assert_almost_equal(ref_data["test_features"], test_features)
        np.testing.assert_almost_equal(ref_data["test_labels"], test_labels)


if __name__ == "__main__":
    unittest.main()
