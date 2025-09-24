#!/usr/bin/env bash
set -e
export AMENT_TRACE_SETUP_FILES=0
safe_source(){ set +u; . "$1"; set -u; }
if [ -f /opt/ros/humble/setup.bash ]; then safe_source /opt/ros/humble/setup.bash; else safe_source /opt/ros/humble/setup.sh; fi
if [ -f /ws/install/setup.bash ]; then safe_source /ws/install/setup.bash; elif [ -f /ws/install/setup.sh ]; then safe_source /ws/install/setup.sh; fi
screen -S nav2 -X quit >/dev/null 2>&1 || true
screen -dmS nav2 bash -lc "export AMENT_TRACE_SETUP_FILES=0; source /opt/ros/humble/setup.bash; [ -f /ws/install/setup.bash ] && source /ws/install/setup.bash || true; ros2 launch lunabot_navigation navigation.launch.py use_sim_time:=true"
