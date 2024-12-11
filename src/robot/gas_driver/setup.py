from setuptools import setup

package_name = 'gas_driver'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='snr',
    maintainer_email='a2technuc@outlook.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gas_sensor_publisher = x3cator_sensor.gas_sensor_publisher:main',
            'gas_sensor_subscriber = x3cator_sensor.gas_sensor_subscriber:main',
        ],
    },
)
