import os
from glob import glob
from setuptools import setup

package_name = 'my_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Lukas Miller',
    maintainer_email='lukas.miller.95@5outlook.de',
    description='This is a simple example package with three nodes.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = my_pkg.my_node:main',
            'publisher = my_pkg.publisher:main',
            'transformer = my_pkg.transformer:main',
            'subscriber = my_pkg.subscriber:main'
        ],
    },
)
