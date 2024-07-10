# Copyright 2021-2024 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

"""
A page of the application.
Page content is imported from the Predictions.md file.

Please refer to https://docs.taipy.io/en/latest/manuals/gui/pages for more details.
"""

from taipy.gui import Markdown, notify
import pandas as pd


dn_holiday = None
dn_result = None

selected_scenario = None
selected_holiday = None
selected_level = 100

# TODO: Complete the `on_submission_change` function
def on_submission_change(state, submitable, details):
    """
    This function triggers some actions once the current selected scenario changes.
    in our case we want to redefine the variable `dn_result` and print that the operation was a success within the app with
    the use of the `notify` function. 
    """
    pass

# TODO: Complete the `on_change_params` function
def on_change_params(state):
    """
    This function triggers some actions once the parameters of a scenario are modified
    In our case we want to redefine
    - the holiday level of importance in the scenario
    - redefine the selected_scenario holiday
    - redefine dn_holiday
    - print that the parameters were changed successfully with the notify function
    - refresh the state with `state.refresh()`
    """
    pass
# TODO: Complete the `on_change` function
def on_change(state, var_name, var_value):
    """
    This function triggers some actions once a state variable is modified.
    We want this function to make actions only if the variable `selected_scenario` has been changed:
    In this case, we want to redefine:
    - the scenario selected level of importance for holidays
    - redefine dn_holiday
    - redefine dn_result
    """
    pass


Predictions = Markdown("pages/Predictions/Predictions.md")