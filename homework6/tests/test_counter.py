from homework6.counter.counter import instances_counter


def test_get_created_instances():
    @instances_counter
    class User:
        pass

    assert User.get_created_instances() == 0
    _ = User(), User(), User()
    assert User.get_created_instances() == 3


def test_reset_instances_counter():
    @instances_counter
    class User:
        pass

    assert User.reset_instances_counter() == 0
    _ = User(), User(), User()
    assert User.reset_instances_counter() == 3
    assert User.reset_instances_counter() == 0
