from unittest.mock import patch, MagicMock
from functions.api_mocking import get_only_numbers, API


def test_get_only_numbers():
    test_data = ["1,3,4,5,32,ab,c21,v32,v323v,v32", "521,532,633,c2c"]
    expected = "1|3|4|5|32|21|32|323|32|521|532|633"

    fake_api = MagicMock()
    fake_api.get_data.return_value = test_data
    with patch("functions.api_mocking.API", fake_api):
        result = get_only_numbers()
        assert result == expected
