Name:           hyprlock
Version:        0.2.0
Release:        %autorelease
Summary:        Hyprland's simple screen locking utility

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  mesa-libgbm-devel

BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(hyprlang) >= 0.4

BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)


%description
Hyprland's simple, yet multi-threaded and GPU-accelerated screen locking
utility.


%prep
%autosetup


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/%{name}


%changelog
%autochangelog

