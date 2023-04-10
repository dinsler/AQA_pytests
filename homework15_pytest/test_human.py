import pytest


@pytest.mark.positive
def test_valid_name(human_with_params):
    name = 'John Smith'
    human = human_with_params(name, 34, 'male')
    assert human._Human__name == name, f'{name} was not added'


@pytest.mark.negative
@pytest.mark.xfail
def test_invalid_name(human_with_params):
    name = 'Nancy2345'
    with pytest.raises(Exception):
        human_with_params(name, 22, 'female')


@pytest.mark.negative
@pytest.mark.xfail
def test_name_as_integer(human_with_params):
    name = 12345
    with pytest.raises(Exception):
        human_with_params(name, 22, 'female')


@pytest.mark.negative
@pytest.mark.xfail
def test_age_as_string(human_with_params):
    age = 'Stasik'
    with pytest.raises(Exception):
        human_with_params('Lucy', age, 'female')


@pytest.mark.positive
def test_change_to_opposite_gender(average_human):
    human = average_human
    new_gender = 'female' if human.gender == 'male' else 'male'
    human.change_gender(new_gender)
    assert human.gender == new_gender, 'Gender was not changed'


@pytest.mark.negative
def test_exception_on_the_same_gender(average_human):
    human = average_human
    new_gender = 'male' if human.gender == 'male' else 'female'
    with pytest.raises(Exception):
        human.change_gender(new_gender)


@pytest.mark.negative
def test_invalid_gender_input(average_human):
    human = average_human
    new_gender = 'non binary'
    with pytest.raises(Exception):
        human.change_gender(new_gender)
    assert human.gender != new_gender, 'Gender changed despite exception'


@pytest.mark.negative
@pytest.mark.xfail
def test_wrong_gender_human(human_with_params):
    gender = 'spaceship'
    with pytest.raises(Exception):
        human = human_with_params('Karl', 34, gender)
    assert human.gender in ["male", "female"], 'Validation should work on object creation also'


@pytest.mark.negative
@pytest.mark.xfail
def test_change_gender_to_dead_human(human_with_params):
    age = 102
    human = human_with_params('Liza', age, 'female')
    new_gender = 'male'
    human.change_gender(new_gender)
    assert human.gender != new_gender, 'Gender should not be changed for dead human'


@pytest.mark.positive
def test_is_alive(average_human):
    human = average_human
    assert average_human._Human__is_alive(), f"{human._Human__name} is already dead..."


@pytest.mark.negative
@pytest.mark.xfail
def test_old_is_alive(dead_human):
    assert not dead_human._Human__is_alive(), 'Human with age over 100 should have status "dead"'


@pytest.mark.positive
def test_grow(average_human):
    expected_age = average_human.age
    average_human.grow()
    assert average_human.age == expected_age + 1, 'Age was not increase'


@pytest.mark.negative
@pytest.mark.xfail
def test_dead_human_grow_not_validated(dead_human):
    with pytest.raises(Exception):  # raises comment
        dead_human.grow()


@pytest.mark.negative
def test_dead_human_not_grow(dead_human):
    expected_age = dead_human.age
    dead_human.grow()
    assert dead_human.age == expected_age, 'Dead human should not grow'
    assert dead_human._Human__status == 'dead', 'Dead human should have correct status'


@pytest.mark.negative
@pytest.mark.xfail
def test_unborn_human(human_with_params):
    age = - 10
    with pytest.raises(Exception):
        human = human_with_params('Michael', age, 'male')
    # human.grow()
    # assert human.age != age + 1, 'Human should not grow, if it does not exist'


@pytest.mark.positive
def test_change_status_by_grow(old_human):
    current_age = old_human.age
    old_human.grow()
    assert old_human._Human__status == 'dead', 'Status was not change, human is dead'
    assert old_human.age == current_age, 'Age should not change for a dead human'
