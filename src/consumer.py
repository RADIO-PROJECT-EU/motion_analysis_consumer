#!/usr/bin/env python
import roslib, rospy
import std_msgs

publisher = None
topic = ''

def init():
    global topic
    rospy.init_node('motion_analysis_consumer')
    print "Do not forget to assign the correct image topic for motion analysis!"
    topic = rospy.get_param("~topic", "/motion_analysis/event/human_transfer")
    rospy.Subscriber(topic, std_msgs.msg.String, stringCallback)
    print "Subscribed to",topic,"..."
    while not rospy.is_shutdown():  
        rospy.spin()

def stringCallback(msg):
    print msg.data


if __name__ == '__main__':
    init() 