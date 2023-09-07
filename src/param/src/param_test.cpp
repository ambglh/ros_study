#include <ros/ros.h>

int main(int argc,char* argv[])
{
    setlocale(LC_ALL,"");
    ros::init(argc,argv,"param_tset");
    // 全局命令空间
    ros::NodeHandle nh;
    // 局部命名空间
    ros::NodeHandle nh_("~");
    int serial_number = -1;
    ROS_INFO("全局命名空间");
    // 提取全局空间的参数
    nh.getParam("serial",serial_number);
    ROS_INFO("全局命名空间的serial is %d",serial_number);
    // 局部命名空间
    nh.getParam("param_node/serial",serial_number);
    ROS_INFO("global_to_local_Serial was %d", serial_number);

    ROS_INFO("局部命名空间");
    nh_.getParam("serial",serial_number);
    ROS_INFO("局部命名空间下的serial is %d",serial_number);
    // 提取全局命名空间
    nh_.getParam("/serial",serial_number);
    ROS_INFO("local_to_global_Serial was %d",serial_number);
    ros::spin();

    return 0;



}