from behave import *
from src import calc


@given('we add two numbers "{x}" and "{y}"')
def we_add_two_numbers_x_and_y(context, x, y):
    print("we add two numbers strings", x, "and", y)
    context.result = calc.add(int(x), int(y))


@then('result should be "{z}"')
def result_should_be_z(context, z):
    print("result should be string", z)
    assert context.result == int(z)
