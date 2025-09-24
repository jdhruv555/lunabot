#!/usr/bin/env bash
set -euo pipefail
: ${BAG_DIR:="./demo_bags"}
mkdir -p ""
. /opt/ros/humble/setup.sh
. ./install/setup.sh
ros2 bag record -o "/demo_20250924_131544" \
/odom /cmd_vel /scan /scan/filtered /scan_from_depth /map /amcl_pose /diagnostics /alerts &
BAG_PID=
ros2 launch lunabot_bringup full_with_hazards.launch.py || true
kill  || true
