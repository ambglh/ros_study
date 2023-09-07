#include <ghm_action/dowishAction.h>
#include <actionlib/server/simple_action_server.h>

typedef actionlib::SimpleActionServer<ghm_action::dowishAction> Server;
void execute(const ghm_action::dowishGoalConstPtr& goal,Server* as)
{
    as->publishFeedback(ghm_action::dowishFeedbackConstPtr& gg);
}


int main(int argc,char** argv)
{
    ros::init(argc,argv,"dowish_server");
    ros::NodeHandle nh;
    Server server(nh,"do_dishes",boost::bind(&execute,_1,&server),false); //_1表示占位符
    server.start();
    ros::spin();
    return 0;
}