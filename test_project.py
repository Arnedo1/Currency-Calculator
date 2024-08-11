import pytest
from unittest.mock import patch

import project


API_KEY = 'test_key'

@pytest.fixture
def valid_currencies():
    return ['USD', 'BRL', 'EUR', 'CAD', 'AUD', 'DKK', 'CHF']

@pytest.fixture
def mock_valid_currencies(valid_currencies):
    with patch('project.get_valid_currencies', return_value=valid_currencies) as mock_get:
        yield mock_get

@pytest.fixture
def mock_conversion_rate():
    with patch('project.get_conversion_rate', return_value=1.0) as mock_get_rate:
        yield mock_get_rate

def test_get_valid_currencies(mock_valid_currencies):
    result = project.get_valid_currencies(API_KEY)
    assert result == ['USD', 'BRL', 'EUR', 'CAD', 'AUD', 'DKK', 'CHF']
    mock_valid_currencies.assert_called_once_with(API_KEY)

def test_update_conversion_rates(mock_conversion_rate):
    project.base_currency = 'USD'
    project.base_amount = 1
    project.update_conversion_rates(project.base_currency, project.base_amount)

    assert project.conversion_rates['EUR'] == 1.0
    assert project.conversion_rates['BRL'] == 1.0

    assert mock_conversion_rate.call_count == len(project.target_currencies) - 1

def test_remove_currency_from_favorites():
    project.target_currencies = ['USD', 'EUR', 'BRL']
    project.conversion_rates = {'USD': 1.0, 'EUR': 1.0, 'BRL': 1.0}
    project.base_currency = 'USD'
