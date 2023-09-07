#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>

void callback(const nav_msgs::Odometry::ConstPtr& msg )
{
    ROS_INFO("msg.twist.twist.linear.x = %.2f\n,msg.twist.twist.linear.y = %.2f\n,msg.twist.twist.linear.z = %.2f",
        msg->twist.twist.linear.x,
        msg->twist.twist.linear.y,
        msg->twist.twist.linear.z

    );

    ROS_INFO("msg->pose.pose.position.x = %.2f\n,msg->pose.pose.position.y = %.2f\n.msg->pose.pose.position.z = %.2f",
        msg->pose.pose.position.x,
        msg->pose.pose.position.y,
        msg->pose.pose.position.z
    );

}

int main(int argc,char* argv[])
{
    ros::init(argc,argv,"odom_sub");
    ros::NodeHandle nh;
    ros::Subscriber osom_sub = nh.subscribe<nav_msgs::Odometry>("odom",10,&callback);

    ros::spin(); 
   
    return 0;
    
}