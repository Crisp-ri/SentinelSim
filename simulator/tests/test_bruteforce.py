from unittest.mock import patch, call

from simulator.scenarios.bruteforce import bruteforce


def test_bruteforce_calls_send_event_correct_number_of_times():
    with patch("simulator.scenarios.bruteforce.send_event") as mock_send, \
         patch("simulator.scenarios.bruteforce.time.sleep"):

        bruteforce(attempts=5, delay=0.1, target_ip="1.2.3.4")

    assert mock_send.call_count == 5


def test_bruteforce_payload_is_correct():
    with patch("simulator.scenarios.bruteforce.send_event") as mock_send, \
         patch("simulator.scenarios.bruteforce.time.sleep"):

        bruteforce(attempts=1, delay=0.1, target_ip="9.9.9.9")

    args, _ = mock_send.call_args
    payload = args[0]

    assert payload["target"] == "9.9.9.9"
    assert "source_ip" in payload
    assert "payload" in payload
    assert "port" in payload


def test_bruteforce_calls_sleep_between_attempts():
    with patch("simulator.scenarios.bruteforce.send_event"), \
         patch("simulator.scenarios.bruteforce.time.sleep") as mock_sleep:

        bruteforce(attempts=3, delay=0.5, target_ip="1.1.1.1")

    assert mock_sleep.call_count == 3
    mock_sleep.assert_has_calls([call(0.5), call(0.5), call(0.5)])


def test_bruteforce_zero_attempts():
    with patch("simulator.scenarios.bruteforce.send_event") as mock_send, \
         patch("simulator.scenarios.bruteforce.time.sleep") as mock_sleep:

        bruteforce(attempts=0, delay=0.1, target_ip="1.1.1.1")

    mock_send.assert_not_called()
    