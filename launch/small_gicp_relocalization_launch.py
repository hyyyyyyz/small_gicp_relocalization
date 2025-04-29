# Copyright 2025 Jackson Huang
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

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    remappings = [("/tf", "tf"), ("/tf_static", "tf_static")]

    node = Node(
        package="small_gicp_relocalization",
        executable="small_gicp_relocalization_node",
        namespace="",
        output="screen",
        remappings=remappings,
        parameters=[
            {
                "num_threads": 12,
                "num_neighbors": 10,
                "global_leaf_size": 0.75,
                "registered_leaf_size": 0.75,
                "max_dist_sq": 5.0,
                "map_frame": "map",
                "odom_frame": "odom",
                "base_frame": "base_link",
                "lidar_frame": "base_link",
                "prior_pcd_file": "/home/hyz/project/quadruped_lidar_relocalization_ws/src/small_gicp_relocalization/pcd/work_station.pcd",
            }
        ],
    )

    return LaunchDescription([node])
