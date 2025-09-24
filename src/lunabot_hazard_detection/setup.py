from setuptools import setup

package_name = 'lunabot_hazard_detection'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/hazard.launch.py', 'launch/hazard_with_alerts.launch.py']),
        ('share/' + package_name + '/config', ['config/hazard.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'hazard_inference = lunabot_hazard_detection.hazard_inference:main',
            'hazard_alert_bridge = lunabot_hazard_detection.hazard_alert_bridge:main',
            'hazard_demo_pub = lunabot_hazard_detection.hazard_demo_pub:main',
            'hazard_onnx_node = lunabot_hazard_detection.hazard_onnx_node:main',
        ],
    },
)
from setuptools import setup

package_name = lunabot_hazard_detection

setup(
    name=package_name,
    version=0.1.0,
    packages=[package_name],
    data_files=[
        (share/ament_index/resource_index/packages, [resource/ + package_name]),
        (share/ + package_name, [package.xml]),
        (share/ + package_name + /launch, [launch/hazard.launch.py, launch/hazard_with_alerts.launch.py]),
        (share/ + package_name + /config, [config/hazard.yaml]),
    ],
    install_requires=[setuptools],
    zip_safe=True,
    entry_points={
        console_scripts: [
            hazard_inference
