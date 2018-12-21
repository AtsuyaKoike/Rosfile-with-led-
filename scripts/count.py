#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

if __name__ == '__main__':
    rospy.init_node('count')
    pub = rospy.Publisher('count_up', Int32, queue_size=1)
    rate = rospy.Rate(5)
    n = 0
    while not rospy.is_shutdown():
        if ( n  > 8 ):
            n = 0
        pub.publish(n)
        n += 1
        rate.sleep()
