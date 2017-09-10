Summary: phpPgAdmin for Nethserver
Name: nethserver-phppgadmin
Version: 0.0.3
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
perl createlinks

%install
/bin/rm -rf $RPM_BUILD_ROOT
(cd root   ; /usr/bin/find . -depth -print | /bin/cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} %{buildroot}   \
   $RPM_BUILD_ROOT > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING

%clean 
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Sep 10 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.3-1.ns6
- Restart httpd service on trusted-network

* Wed Mar 29 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.2-1.ns6
- Template expansion on trusted-network

* Sun Mar 12 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.1-2.ns6
- GPL license

* Thu Dec 22 2016 stephane de labrusse <stephdl@de-labrusse.fr> - 0.0.1-1.ns6
- NS6 version
