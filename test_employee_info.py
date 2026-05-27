import employee_info as em


def test_employees_by_age_range():
    expected_result = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
                       {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
                       {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    result = em.get_employees_by_age_range(25,38)

    assert(expected_result == result)


def test_calculate_average_salary():
    expected_result = 60166.67
    result = em.calculate_average_salary()

    assert(expected_result == result)

def test_get_employees_by_dept():
    expected_result = ["John","Peter"]
    result = em.get_employees_by_dept("Sales")

    assert(expected_result == result)