from setuptools import find_packages, setup

package_name = 'ros2_tutorial'

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
    maintainer='Jadiouo',
    maintainer_email='Jadiouo@users.noreply.github.com',
    description='Minimal ROS 2 Jazzy talker/listener package (ament_python)',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'talker = ros2_tutorial.talker:main',
            'listener = ros2_tutorial.listener:main',
        ],
    },
)
