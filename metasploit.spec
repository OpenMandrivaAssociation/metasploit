%define	name	metasploit
%define	version	3.6.0
%define	release	%mkrel 1

# prevent rpm to create debug files for binary content
%define _enable_debug_packages    %{nil}
%define debug_package     %{nil}
# disable automatic dependencies, because of shipped exploits
%define __find_provides %{nil}
%define __find_requires %{nil}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Penetration Testing Resources
License:	GPLv2
Group:		Monitoring
URL:		http://www.metasploit.com/
Source0:	http://www.metasploit.com/releases/framework-%{version}.tar.bz2
Patch:      msf3-3.5.0-fhs.patch
BuildArch:	noarch
# To avoid automatic dependency on file
BuildRequires:	ruby
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Metasploit provides useful information and tools for penetration
testers, security researchers, and IDS signature developers. This
project was created to provide information on exploit techniques
and to create a functional knowledgebase for exploit developers and
security professionals. The tools and information on this site are
provided for legal security research and testing purposes only.
Metasploit is an open source project managed by Rapid7.

%package gui
Summary:	GUI for %{name}
Group:		Monitoring
Requires:   %{name} = %{version}-%{release}
Requires:   ruby-gtk2
Requires:   ruby-libglade2

%description gui
This package contains a GUI for %{name}.

%prep
%setup -q -n msf3
%patch -p 1
find . -name .svn | xargs rm -rf

%build

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_bindir}
install -m 755 msf* %{buildroot}%{_bindir}

install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -r data %{buildroot}%{_datadir}/%{name}
cp -r external %{buildroot}%{_datadir}/%{name}
cp -r lib %{buildroot}%{_datadir}/%{name}
cp -r modules %{buildroot}%{_datadir}/%{name}
cp -r plugins %{buildroot}%{_datadir}/%{name}
cp -r scripts %{buildroot}%{_datadir}/%{name}
cp -r tools %{buildroot}%{_datadir}/%{name}

rm -rf %{buildroot}%{_datadir}/%{name}/external/source

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{_datadir}/metasploit
%exclude %{_bindir}/msfgui

%files gui
%defattr(-,root,root)
%doc README
%{_bindir}/msfgui

