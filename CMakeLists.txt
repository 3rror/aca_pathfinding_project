cmake_minimum_required(VERSION 3.0.0)
project(aca_pathfinding VERSION 0.1.0)
# set(CMAKE_CXX_STANDARD 20)

# include(CTest)
# enable_testing()

add_executable(aca_pathfinding main.cpp graph.hpp)

target_compile_features(aca_pathfinding PUBLIC cxx_std_20)
set_target_properties(aca_pathfinding PROPERTIES CXX_EXTENSIONS OFF)

# set(CPACK_PROJECT_NAME ${PROJECT_NAME})
# set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
# include(CPack)

find_package(OpenMP)
if(OpenMP_CXX_FOUND)
    target_link_libraries(aca_pathfinding PUBLIC OpenMP::OpenMP_CXX)
endif()
