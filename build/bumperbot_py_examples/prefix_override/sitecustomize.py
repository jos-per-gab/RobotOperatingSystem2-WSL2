import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/lazywsl/RobotOperatingSystem2-WSL2/ROS2/bumpberbot_ws/install/bumperbot_py_examples'
