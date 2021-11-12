# Copyright (c) 2019, Andreas Klintberg
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription, LaunchIntrospector, LaunchService
from launch_ros import actions


def generate_launch_description():
    """
    Launch file for publishing Razor IMU data
    """
    config_path = os.path.join(get_package_share_directory("ros2_razor_imu"), "config",
                               "razor.yaml")

    imu_node = actions.Node(
        package='ros2_razor_imu', 
        executable='imu_node', 
        output='screen',
        parameters=[
            config_path
        ]
    )

    return LaunchDescription([imu_node])