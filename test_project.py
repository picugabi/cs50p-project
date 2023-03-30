from project import sorted_dict,average,below_avg,above_avg


def test_sorted_dict():
    assert sorted_dict({1:2, 3:5, 2:1}) == {1:2 , 2:1 , 3:5}
    assert sorted_dict({1:1, 2:1, 4:1, 3:1}) == {1:1, 2:1, 3:1, 4:1}


def test_average():
    assert average({1:1, 2:1, 3:1, 4:1}) == ({}, {1:25.0 , 2:25.0, 3:25.0, 4:25.0})

def test_below_avg():
    assert below_avg({1:1 , 2:1 , 3:1}, 1) == [1] or [2] or [3]
    assert below_avg({1:1 , 2:1 , 3:1}, 2) == [1,2] or [1,3] or [2,1] or [2,3] or [3,1] or [3,2]

def test_above_avg():
    assert above_avg({1:1 , 2:1 , 3:1}, 1) == [1] or [2] or [3]
    assert above_avg({1:1 , 2:1 , 3:1}, 2) == [1,2] or [1,3] or [2,1] or [2,3] or [3,1] or [3,2]
