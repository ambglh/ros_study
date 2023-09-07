#include <ros/ros.h>

int main(int argc,char* argv[])
{
    ros::init(argc,argv,"ghm_param");
    ros::NodeHandle nh;
    int param1,param2,param3,param4,param5;
    bool ifget1 = ros::param::get("param_1",param1);
    bool ifget2 = nh.getParam("param_2",param2);
    nh.param("param_3",param3,3);
    ROS_INFO("param3 is %d",param3);
    if (ifget1)
    {
        ROS_INFO("param_1 got successfully");
    }
    else
    {
        ROS_WARN("param1 has got value byyourself");
        param1 = 1;

    }
    param4 = 4;
    ros::param::set("param_4",param4);
    param5 = 5;
    nh.setParam("param_5",param5);
    bool ifparam4 = nh.hasParam("param4");
    bool ifparam5 = ros::param::has("param5");
    
    return 0;
}