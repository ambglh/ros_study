#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>

int main(int argc,char* argv[])
{
    ros::init(argc,argv,"odom_pub");
    ros::NodeHandle nh;
    ros::Publisher odom_pub = nh.advertise<nav_msgs::Odometry>("odom",50);
    tf::TransformBroadcaster odom_broadcaster;
    double x = 0;
    double y = 0;
    double th = 0;

    double vx = 0.1;
    double vy = -0.1;
    double vth = 0.1;

    ros::Time current_time,last_time;
    current_time = ros::Time::now();
    last_time = ros::Time::now();

    ros::Rate r(10);
    while ( nh.ok())
    {
        ros::spinOnce();
        current_time = ros::Time::now();

        double dt = (current_time - last_time).toSec();
        double delta_x = (vx * cos(th) - vy * sin(th)) * dt;
        double delta_y = (vx * sin(th) - vy * cos(th)) * dt;
        double delta_th = vth * dt;

        x += delta_x;
        y += delta_y;
        th +=delta_th;
        ROS_INFO("x = %.2f,y = %.2f,th = %.2f",
                x,y,th);

        geometry_msgs::Quaternion odom_quat = tf::createQuaternionMsgFromYaw(th);
        geometry_msgs::TransformStamped odom_trans;
        odom_trans.header.stamp = current_time;
        odom_trans.header.frame_id = "odom";
        odom_trans.child_frame_id = "base_link";
        odom_trans.transform.translation.x = x;
        odom_trans.transform.translation.y = y;
        odom_trans.transform.translation.z = 0.0;
        odom_trans.transform.rotation = odom_quat;

        odom_broadcaster.sendTransform(odom_trans);
        nav_msgs::Odometry odom;
        odom.pose.pose.position.x = x;
        odom.pose.pose.position.y = y;
        odom.pose.pose.position.z = 0;
        odom.pose.pose.orientation = odom_quat;

        odom.child_frame_id = "base_link";
        odom.twist.twist.linear.x = vx;
        odom.twist.twist.linear.y = vy;
        odom.twist.twist.angular.z = vth;
        odom_pub.publish(odom);

        last_time = current_time;
        r.sleep();

    }
    
}