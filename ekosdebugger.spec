Name: ekosdebugger
Version: 0.0.1.git
Release: 1%{?dist}
Summary: Ekos Debugger

License: LGPLv2
# See COPYRIGHT file for a description of the licenses and files covered

URL: https://indilib.org
Source0: https://github.com/knro/ekosdebugger/archive/master.tar.gz

BuildRequires: cmake
BuildRequires: systemd
BuildRequires: indi-libs
BuildRequires: indi-devel

BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(zlib)


%description
Ekos Debugger is a helper application to KStars, Ekos, and INDI debugging. It can be used to troubleshoot KStars, INDI, or both.

The generated log files can be shared with developers in order to investigate any issues with the software and help to improve it.

%prep
%setup -n ekosdebugger-master

%build
%define _lto_cflags %{nil}

%cmake .
make VERBOSE=1 %{?_smp_mflags} -j4

%install
make DESTDIR=%{buildroot} install

%files
%license COPYING
%doc README.md
%{_bindir}/*


%changelog
* Wed Jul 29 2020 Jim Howard <jh.xsnrg+fedora@gmail.com> 0.0.1.git-1
- added spec for copr

