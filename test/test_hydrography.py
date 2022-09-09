import pytest

from application import rest
from . import TestConfig as config

API_PREFIX = rest.server.API_PREFIX


def mock_kafka():
    from application import kafka
    result = kafka.start_consumer(config)
    return result


def mock_gunicorn():
    from application import rest
    result = rest.start_gunicorn_server(config)
    return result


def mock_rest():
    from application import rest
    result = rest.start_flask_server(config)
    return result


@pytest.fixture
def clientinstance():
    return rest.create_server(config).test_client()


def _test_kafka_consumer(mocker):
    mocker.patch('application.kafka.start_consumer', return_value=1)
    assert mock_kafka() == 1


def _test_gunicorn_consumer(mocker):
    mocker.patch('application.rest.start_gunicorn_server', return_value=1)
    assert mock_gunicorn() == 1


def _test_server_consumer(mocker):
    mocker.patch('application.rest.start_flask_server', return_value=1)
    assert mock_rest() == 1


def test_aquifer_route(clientinstance):
    url = API_PREFIX + '/aquifers'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def test_basin_route(clientinstance):
    url = API_PREFIX + '/basins'
    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def test_flow_rate_route(clientinstance):
    url = API_PREFIX + '/flow_rates'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def test_hydrography_route(clientinstance):
    url = API_PREFIX + '/hydrography/geojson'

    payload = {'ids': ['dea95839-7f6b-4aa4-ab4a-9bce6a12fd10']}
    response = clientinstance.post(url, json=payload)
    assert response.get_data() != b''
    assert response.status_code == 200


def test_hydrography_summary_route(clientinstance):
    url = API_PREFIX + '/hydrography/summary'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def test_contribs_route(clientinstance):
    url = API_PREFIX + '/contribs'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def test_water_security_route(clientinstance):
    url = API_PREFIX + '/water_security'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def test_water_availability_route(clientinstance):
    url = API_PREFIX + '/water_availability'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def test_waterbodies_route(clientinstance):
    url = API_PREFIX + '/waterbodies'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def test_limitslvl1_route(clientinstance):
    url = API_PREFIX + '/limits_lvl_1'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def test_limitslvl2_route(clientinstance):
    url = API_PREFIX + '/limits_lvl_2'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200
