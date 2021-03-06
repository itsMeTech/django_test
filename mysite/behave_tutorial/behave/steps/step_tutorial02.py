# ----------------------------------------------------------------------------
# STEPS:
# http://jenisys.github.io/behave.example/tutorials/tutorial03.html
# ----------------------------------------------------------------------------
from behave   import given, when, then
from hamcrest import assert_that, equal_to, is_not
from behave_tutorial.classes.NinjaFight import NinjaFight

@given('the ninja has a {achievement_level}')
def step_the_ninja_has_a(context, achievement_level):
    context.ninja_fight = NinjaFight(achievement_level)

@when('attacked by a {opponent_role}')
def step_attacked_by_a(context, opponent_role):
    context.ninja_fight.opponent = opponent_role

@when('attacked by {opponent}')
def step_attacked_by(context, opponent):
    context.ninja_fight.opponent = opponent

@when('not attacked')
def step_attacked_by(context):
    context.ninja_fight.opponent = None

@then('the ninja should {reaction}')
def step_the_ninja_should(context, reaction):
    assert_that(reaction, equal_to(context.ninja_fight.decision()))