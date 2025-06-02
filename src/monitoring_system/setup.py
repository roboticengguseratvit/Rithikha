from setuptools import find_packages, setup

package_name = 'monitoring_system'

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
    maintainer='rithikha',
    maintainer_email='roboticengguseratvit@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'cpu_temp_publisher = monitoring_system.cpu_temp_publisher:main',
        	'cpu_temp_monitor = monitoring_system.cpu_temp_monitor:main',
        	'utility_node = monitoring_system.utility_node:main',
        ],
    },
)
