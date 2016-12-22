Summary: phpPgAdmin for Nethserver
Name: nethserver-phppgadmin
Version: 0.0.1
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
URL: http://dev.nethserver.org/projects/nethforge/wiki/%{name}
BuildArch: noarch

Requires: nethserver-postgresql
Requires: nethserver-httpd
Requires: phpPgAdmin
Requires: php-pgsql
BuildRequires: perl
BuildRequires: nethserver-devtools 

%description
Implementation of phpPgAdmin for Nethserver

%prep
%setup

%build
#mkdir  -p root/var/lib/phpMyAdmin/tmp
perl createlinks

%install
/bin/rm -rf $RPM_BUILD_ROOT
(cd root   ; /usr/bin/find . -depth -print | /bin/cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} %{buildroot}   \
   $RPM_BUILD_ROOT > %{name}-%{version}-filelist
#echo "%doc phpmyadmin.sql" >> %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%dir %{_nseventsdir}/%{name}-update

%clean 
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Dec 22 2016 stephane de labrusse <stephdl@de-labrusse.fr> - 0.0.1-1.ns7
- NS7 version
