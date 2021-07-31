%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-plotjuggler-ros
Version:        1.5.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS plotjuggler_ros package

License:        AGPLv3
URL:            https://github.com/facontidavide/PlotJuggler
Source0:        %{name}-%{version}.tar.gz

Requires:       binutils-devel
Requires:       boost-devel
Requires:       boost-python%{python3_pkgversion}-devel
Requires:       qt5-qtbase-devel
Requires:       qt5-qtsvg-devel
Requires:       qt5-qtwebsockets-devel
Requires:       ros-galactic-diagnostic-msgs
Requires:       ros-galactic-fastcdr
Requires:       ros-galactic-geometry-msgs
Requires:       ros-galactic-nav-msgs
Requires:       ros-galactic-plotjuggler
Requires:       ros-galactic-plotjuggler-msgs
Requires:       ros-galactic-rclcpp
Requires:       ros-galactic-rcpputils
Requires:       ros-galactic-rosbag2
Requires:       ros-galactic-rosbag2-transport
Requires:       ros-galactic-sensor-msgs
Requires:       ros-galactic-tf2-msgs
Requires:       ros-galactic-tf2-ros
Requires:       ros-galactic-ros-workspace
BuildRequires:  binutils-devel
BuildRequires:  boost-devel
BuildRequires:  boost-python%{python3_pkgversion}-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtwebsockets-devel
BuildRequires:  ros-galactic-ament-cmake
BuildRequires:  ros-galactic-diagnostic-msgs
BuildRequires:  ros-galactic-fastcdr
BuildRequires:  ros-galactic-geometry-msgs
BuildRequires:  ros-galactic-nav-msgs
BuildRequires:  ros-galactic-plotjuggler
BuildRequires:  ros-galactic-plotjuggler-msgs
BuildRequires:  ros-galactic-rclcpp
BuildRequires:  ros-galactic-rcpputils
BuildRequires:  ros-galactic-rosbag2
BuildRequires:  ros-galactic-rosbag2-transport
BuildRequires:  ros-galactic-sensor-msgs
BuildRequires:  ros-galactic-tf2-msgs
BuildRequires:  ros-galactic-tf2-ros
BuildRequires:  ros-galactic-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
PlotJuggler plugin for ROS

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/galactic" \
    -DAMENT_PREFIX_PATH="/opt/ros/galactic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/galactic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Sat Jul 31 2021 Davide Faconti <davide.faconti@gmail.com> - 1.5.1-1
- Autogenerated by Bloom

