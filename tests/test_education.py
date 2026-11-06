import unittest
from sightings_analysis.synthetic_data import generate_rows
from sightings_analysis.stats import mean, pearson_r, simple_linear_regression

class SyntheticReportingTests(unittest.TestCase):
    def test_reproducible_sample(self):
        self.assertEqual(generate_rows(rows=20,seed=42),generate_rows(rows=20,seed=42))
        self.assertEqual(len(generate_rows(rows=20,seed=42)),20)
        self.assertTrue(all(row["report_id"].startswith("SYN-") for row in generate_rows(rows=20)))
    def test_elementary_statistics(self):
        self.assertEqual(mean([2,4,6]),4.0)
        self.assertAlmostEqual(pearson_r([1,2,3],[2,4,6]),1.0)
        slope,intercept,r2=simple_linear_regression([1,2,3],[2,4,6])
        self.assertAlmostEqual(slope,2.0)
        self.assertAlmostEqual(r2,1.0)
