from homework6.counter.counter import instances_counter


def test_get_created_instances():
    @instances_counter
    class Test:
        pass

    assert Test.get_created_instances() == 0
    instance, _, _ = Test(), Test(), Test()
    assert Test.get_created_instances() == 3


def test_reset_instances_counter():
    @instances_counter
    class Test:
        pass

    assert Test.reset_instances_counter() == 0
    instance, _, _ = Test(), Test(), Test()
    assert Test.reset_instances_counter() == 3
    assert Test.reset_instances_counter() == 0
