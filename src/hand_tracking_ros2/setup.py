from setuptools import find_packages, setup

package_name = 'hand_tracking_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='asrahina',
    maintainer_email='asrahina649@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
              'hand_tracking_node = hand_tracking_ros2.hand_tracking_node:main'
        ],
    },
)
