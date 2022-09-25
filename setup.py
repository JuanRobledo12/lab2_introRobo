from setuptools import setup

package_name = 'team99_object_follower'

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
    maintainer='tony',
    maintainer_email='jarobledo98@hotmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'view_image_raw = team99_object_follower.view_image_raw:main',
            'detect_ball = team99_object_follower.detect_ball:main',
            'rotate_turtle = team99_object_follower.rotate_turtle:main',
            'test_detect_ball = team99_object_follower.test_detect_ball:main',
        ],
    },
)
