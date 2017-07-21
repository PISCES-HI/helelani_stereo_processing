cmake_minimum_required(VERSION 2.8.3)
project(helelani_stereo_processing)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS rospy)

###################################
## catkin specific configuration ##
###################################

catkin_package(
  INCLUDE_DIRS src
  LIBRARIES helelani_client
  CATKIN_DEPENDS rospy std_msgs helelani_common
)

#############
## Install ##
#############

catkin_python_setup()

install(PROGRAMS scripts/stereo_anaglyph scripts/stereo_calibration
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
