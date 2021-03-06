# Copyright 2016 Ebay Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


""" CLI interface for Rally OVS. """
from __future__ import print_function


import sys

from rally.cli import cliutils
from rally.common import profile
from rally_ovs.cli.commands import deployment
from rally_ovs.cli.commands import task


profile.profile = profile.PROFILE_OVS

ovs_categories = {
    "deployment": deployment.DeploymentCommands,
    "task": task.TaskCommands,
}



def main():
    return cliutils.run(sys.argv, ovs_categories)


if __name__ == '__main__':
    sys.exit(main())
