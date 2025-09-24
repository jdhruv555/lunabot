cmake_minimum_required(VERSION 3.8)
project(lunabot_description)
find_package(ament_cmake REQUIRED)
ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/env-hooks/lunabot_description.dsv")
install(DIRECTORY urdf meshes launch
  DESTINATION share/${PROJECT_NAME}
)
ament_package()
