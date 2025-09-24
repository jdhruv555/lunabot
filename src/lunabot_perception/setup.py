from setuptools import setup

package_name = lunabot_perception

setup(
    name=package_name,
    version=0.1.0,
    packages=[package_name],
    data_files=[
        (share/ament_index/resource_index/packages, [resource/ + package_name]),
        (share/ + package_name, [package.xml]),
        (share/ + package_name + /launch, [launch/perception.launch.py]),
        (share/ + package_name + /config, [config/perception.yaml]),
    ],
    install_requires=[setuptools],
    zip_safe=True,
    entry_points={
        console_scripts: [
            lidar_filter
