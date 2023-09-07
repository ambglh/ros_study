#include <ghm_action/dowishAction.h>
#include <actionlib/client/simple_action_client.h>

typedef actionlib::SimpleActionClient<ghm_action::dowishAction> Client;
int main(int argc,char* argv[])
{
    ros::init(argc,argv,"do_dished_client");
    Client client("do_dishes",true);  // true -> don't need ros::spin()
    client.waitForServer();
    ghm_action::dowishGoal goal;

    client.sendGoal(goal);
    bool flag = client.waitForResult(ros::Duration(5.0));
    try
    {
       ROS_INFO("server has benn ready!!!!");
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
    }
    
    if (client.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
    {
        printf("Yay!! The dish work has finished\n");
    }
    printf("Current State is : %s\n",client.getState().toString().c_str());
    return 0;
    
}