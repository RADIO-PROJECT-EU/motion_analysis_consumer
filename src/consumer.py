#!/usr/bin/env python
import roslib, rospy
from motion_analysis.msg import AnswerWithHeader

topic = ''

def init():
    global topic
    rospy.init_node('motion_analysis_consumer')
    print "Do not forget to assign the correct image topic for motion analysis!"
    topic = rospy.get_param("~topic", "/motion_analysis/event/human_transfer")
    rospy.Subscriber(topic, AnswerWithHeader, stringCallback)
    print "Subscribed to",topic,"..."
    while not rospy.is_shutdown():  
        rospy.spin()

def stringCallback(msg):
    print 'Real message value = ',msg.event
    if msg.event == 0:
        print 'Sitting on bed'
    elif msg.event == 1:
        print 'Stood up'
    elif msg.event == 2:
        print 'Walking'



if __name__ == '__main__':
    init() 