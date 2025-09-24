#!/usr/bin/env bash
set -euo pipefail
. /opt/ros/humble/setup.sh
. "./../install/setup.sh"
ros2 launch lunabot_sim spawn_in_world.launch.py
