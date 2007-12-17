%define name aoetools
%define version 16
%define release %mkrel 1

Summary: Programs to setup ATA over Ethernet device
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: GPL 
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
rm -rf $RPM_BUILD_ROOT

mkdir -p %buildroot
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc HACKING NEWS README TODO
%_sbindir/*
%_mandir/*/*
