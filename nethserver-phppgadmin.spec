Summary: phpPgAdmin for Nethserver
Name: nethserver-phppgadmin
Version: 0.0.4
Release: 2%{?dist}
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
sed -i 's/_RELEASE_/%{version}/' %{name}.json

%install
/bin/rm -rf $RPM_BUILD_ROOT
(cd root   ; /usr/bin/find . -depth -print | /bin/cpio -dump $RPM_BUILD_ROOT)

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
cp -a manifest.json %{buildroot}/usr/share/cockpit/%{name}/
cp -a logo.png %{buildroot}/usr/share/cockpit/%{name}/
cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/

%{genfilelist} %{buildroot}   \
   $RPM_BUILD_ROOT > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%clean 
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Oct 14 2019 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.4-1.ns7
- cockpit. added to legacy apps

* Sun Sep 10 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.3-1.ns7
- Restart httpd service on trusted-network

* Wed Mar 29 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.2-1.ns7
- Template expansion on trusted-network

* Sun Mar 12 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.1-2.ns7
- GPL license

* Thu Dec 22 2016 stephane de labrusse <stephdl@de-labrusse.fr> - 0.0.1-1.ns7
- NS7 version
