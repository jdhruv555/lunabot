from setuptools import setup

package_name = lunabot_base

setup(
    name=package_name,
    version=0.1.0,
    packages=[package_name],
    data_files=[
        (share/ament_index/resource_index/packages, [resource/ + package_name]),
        (share/ + package_name, [package.xml]),
        (share/ + package_name + /launch, [launch/base.launch.py]),
    ],
    install_requires=[setuptools],
    zip_safe=True,
    maintainer=LunaBot,
    maintainer_email=you@example.com,
    description=Base
