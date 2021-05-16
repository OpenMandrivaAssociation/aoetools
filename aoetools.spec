Summary: Programs to setup ATA over Ethernet device
Name: aoetools
Version: 37
Release: 1
Source0: https://github.com/OpenAoE/aoetools/archive/refs/tags/aoetools-%{version}.tar.gz
License: GPLv2+ 
Group: System/Kernel and hardware
Url: https://github.com/OpenAoE/aoetools

%description
The aoetools are programs for users of the ATA over Ethernet (AoE)
network storage protocol, a simple protocol for using storage over
an ethernet LAN.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

%build
%make_build CFLAGS="%optflags"

%install
mkdir -p %buildroot
%make_install

%files
%doc HACKING NEWS README
%_sbindir/*
%_mandir/*/*
