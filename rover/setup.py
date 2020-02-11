import os
from glob import glob
from setuptools import setup

package_name = 'rover'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        (os.path.join('share', package_name), glob('launch/*.yml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Michael Jalloh',
    maintainer_email='michaeljalloh19@gmail.com',
    description='ROS2 package for the rover',
    license='MIT License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "controller = rover.controller:main"
        ],
    },
)
