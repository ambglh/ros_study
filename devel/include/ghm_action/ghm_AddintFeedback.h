// Generated by gencpp from file ghm_action/ghm_AddintFeedback.msg
// DO NOT EDIT!


#ifndef GHM_ACTION_MESSAGE_GHM_ADDINTFEEDBACK_H
#define GHM_ACTION_MESSAGE_GHM_ADDINTFEEDBACK_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ghm_action
{
template <class ContainerAllocator>
struct ghm_AddintFeedback_
{
  typedef ghm_AddintFeedback_<ContainerAllocator> Type;

  ghm_AddintFeedback_()
    : progress_bar(0.0)  {
    }
  ghm_AddintFeedback_(const ContainerAllocator& _alloc)
    : progress_bar(0.0)  {
  (void)_alloc;
    }



   typedef double _progress_bar_type;
  _progress_bar_type progress_bar;





  typedef boost::shared_ptr< ::ghm_action::ghm_AddintFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ghm_action::ghm_AddintFeedback_<ContainerAllocator> const> ConstPtr;

}; // struct ghm_AddintFeedback_

typedef ::ghm_action::ghm_AddintFeedback_<std::allocator<void> > ghm_AddintFeedback;

typedef boost::shared_ptr< ::ghm_action::ghm_AddintFeedback > ghm_AddintFeedbackPtr;
typedef boost::shared_ptr< ::ghm_action::ghm_AddintFeedback const> ghm_AddintFeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ghm_action::ghm_AddintFeedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ghm_action::ghm_AddintFeedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ghm_action::ghm_AddintFeedback_<ContainerAllocator1> & lhs, const ::ghm_action::ghm_AddintFeedback_<ContainerAllocator2> & rhs)
{
  return lhs.progress_bar == rhs.progress_bar;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ghm_action::ghm_AddintFeedback_<ContainerAllocator1> & lhs, const ::ghm_action::ghm_AddintFeedback_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ghm_action

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::ghm_action::ghm_AddintFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ghm_action::ghm_AddintFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ghm_action::ghm_AddintFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ghm_action::ghm_AddintFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ghm_action::ghm_AddintFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ghm_action::ghm_AddintFeedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ghm_action::ghm_AddintFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ac7532a8a8f0d2be4f5284d94fee2d59";
  }

  static const char* value(const ::ghm_action::ghm_AddintFeedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xac7532a8a8f0d2beULL;
  static const uint64_t static_value2 = 0x4f5284d94fee2d59ULL;
};

template<class ContainerAllocator>
struct DataType< ::ghm_action::ghm_AddintFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ghm_action/ghm_AddintFeedback";
  }

  static const char* value(const ::ghm_action::ghm_AddintFeedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ghm_action::ghm_AddintFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#连续反馈\n"
"float64 progress_bar\n"
"\n"
;
  }

  static const char* value(const ::ghm_action::ghm_AddintFeedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ghm_action::ghm_AddintFeedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.progress_bar);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ghm_AddintFeedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ghm_action::ghm_AddintFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ghm_action::ghm_AddintFeedback_<ContainerAllocator>& v)
  {
    s << indent << "progress_bar: ";
    Printer<double>::stream(s, indent + "  ", v.progress_bar);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GHM_ACTION_MESSAGE_GHM_ADDINTFEEDBACK_H
