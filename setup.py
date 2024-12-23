from setuptools import find_packages, setup

package_name = 'pythonROSexamples'

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
    maintainer='claypool',
    maintainer_email='claypool@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ["pyTestNode = pythonROSexamples.myFirstPyNode:main",
                            "robonews_publisher_node = pythonROSexamples.robonewsStation:main",
                            "robonews_listener_node = pythonROSexamples.subscriberPhone:main",
                            "adder_server_node = pythonROSexamples.intAdderServer:main",
                            "adder_client_node_without_oop = pythonROSexamples.intAdderClientNoop:main",
                            "adder_client_node_oop = pythonROSexamples.intAdderClientOop:main",
                            "hardware_stat_publisher_node = pythonROSexamples.hwStatusPublisher:main"]

                            
    },
)
