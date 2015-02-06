%define name aoetools
%define version 35
%define release 2

Summary: Programs to setup ATA over Ethernet device
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://downloads.sourceforge.net/project/aoetools/aoetools/%{version}/%{name}-%{version}.tar.gz
License: GPLv2+ 
Group: System/Kernel and hardware
Url: http://sourceforge.net/projects/aoetools/

%description
The aoetools are programs for users of the ATA over Ethernet (AoE)
network storage protocol, a simple protocol for using storage over
an ethernet LAN.

%prep
%setup -q

%build
%make CFLAGS="%optflags"

%install
mkdir -p %buildroot
%makeinstall_std

%files
%doc HACKING NEWS README
%_sbindir/*
%_mandir/*/*
