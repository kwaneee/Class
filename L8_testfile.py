from L8 import traffic_light

def test_traffic_light():
    """Test traffic_light."""
    assert traffic_light("red") == "green", "test failed for input red"
    assert traffic_light("green") == "yellow", "test failed for input green"
    assert traffic_light("yellow") == "red", "test failed for input yellow"

    print("All tests passed")

test_traffic_light()