from behave import *


def before_all(context):
    print("This before of all")


def before_feature(context, feature):
    print("This is before feature call")


def after_scenario(context, scenario):
    print("This is after scenario call")
