import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from lab_6 import check_distribution 

class TestGasDistribution(unittest.TestCase):
    
    def test_all_cities_reachable(self):
        cities = ['Львів', 'Стрий']
        storages = ['Сховище_1']
        pipelines = [['Сховище_1', 'Львів'], ['Львів', 'Стрий']]
        result = check_distribution(cities, storages, pipelines)
        self.assertEqual(result, [])

    def test_some_cities_unreachable(self):
        cities = ['Львів', 'Стрий', 'Долина']
        storages = ['Сховище_1']
        pipelines = [['Сховище_1', 'Львів']]
        result = check_distribution(cities, storages, pipelines)
        self.assertEqual(result, [['Сховище_1', ['Стрий', 'Долина']]])

    def test_multiple_storages(self):
        cities = ['Львів', 'Стрий', 'Долина']
        storages = ['Сховище_1', 'Сховище_2']
        pipelines = [['Сховище_1', 'Долина'], ['Долина', 'Львів'], ['Львів', 'Стрий']]
        result = check_distribution(cities, storages, pipelines)
        self.assertEqual(result, [['Сховище_2', ['Львів', 'Стрий', 'Долина']]])

    def test_no_pipelines(self):
        cities = ['Львів', 'Стрий']
        storages = ['Сховище_1']
        pipelines = []
        result = check_distribution(cities, storages, pipelines)
        self.assertEqual(result, [['Сховище_1', ['Львів', 'Стрий']]])

    def test_empty_input(self):
        cities = []
        storages = []
        pipelines = []
        result = check_distribution(cities, storages, pipelines)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
