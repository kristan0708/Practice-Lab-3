import employee_info as em


#def test_employees_by_age_range():


def test_calculate_average_salary():
    expected_result = 60166.67
    result = em.calculate_average_salary()

    assert(expected_result == result)

#def test_get_employees_by_dept():