#!/usr/bin/env python
import sys
from std_msgs.msg import Int32
import rospy

def cb(message):
    rospy.loginfo(message.data)
    num = message.data
    string = str(num) + "\n"
    print(string)
    with open("/dev/myled0", mode = 'w' ) as dev:
        dev.write(string)   

if __name__ == '__main__':
    rospy.init_node('led')
    sub = rospy.Subscriber('count_up', Int32, cb)
    rospy.spin()
