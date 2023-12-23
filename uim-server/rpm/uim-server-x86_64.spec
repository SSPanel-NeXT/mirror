Name:           uim-server
Version:        0.0.1
Release:        1%{?dist}
Summary:        SSPanel-UIM Server (XrayR Edition) is a fork of XrayR with full WebAPI support & bugfixes.
Group:          Unspecified
License:        MPL-2.0
URL:            https://github.com/SSPanel-UIM/UIM-Server
Packager:       SSPanel-UIM Team <package@sspanel.org>
BuildRequires:  systemd

%description
SSPanel-UIM Server (XrayR Edition) is a fork of XrayR with full WebAPI support & bugfixes.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/uim-server
mkdir -p %{buildroot}%{_sysconfdir}/uim-server
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/uim-server-amd64-linux %{buildroot}/usr/local/uim-server/uim-server
install -m 644 %{_builddir}/%{name}-%{version}/dns.json %{buildroot}/usr/local/uim-server/dns.json
install -m 644 %{_builddir}/%{name}-%{version}/route.json %{buildroot}/usr/local/uim-server/route.json
install -m 644 %{_builddir}/%{name}-%{version}/custom_outbound.json %{buildroot}/usr/local/uim-server/custom_outbound.json
install -m 644 %{_builddir}/%{name}-%{version}/custom_inbound.json %{buildroot}/usr/local/uim-server/custom_inbound.json
install -m 644 %{_builddir}/%{name}-%{version}/rulelist %{buildroot}/usr/local/uim-server/rulelist
install -m 644 %{_builddir}/%{name}-%{version}/geoip.dat %{buildroot}/usr/local/uim-server/geoip.dat
install -m 644 %{_builddir}/%{name}-%{version}/geosite.dat %{buildroot}/usr/local/uim-server/geosite.dat
install -m 644 %{_builddir}/%{name}-%{version}/README.md %{buildroot}/usr/local/uim-server/README.md
install -m 644 %{_builddir}/%{name}-%{version}/LICENSE %{buildroot}/usr/local/uim-server/LICENSE
install -m 644 %{_builddir}/%{name}-%{version}/config.yml.example %{buildroot}%{_sysconfdir}/uim-server/config.yml
install -m 644 %{_builddir}/%{name}-%{version}/uim-server.service %{buildroot}%{_sysconfdir}/systemd/system

%post
ln -s /usr/local/uim-server/uim-server %{_bindir}/uim-server

%postun
rm -f %{_bindir}/uim-server

%clean
rm -rf %{buildroot}

%files
%attr(0755, root, root) /usr/local/uim-server
%attr(0755, root, root) /usr/local/uim-server/uim-server
%attr(0644, root, root) /usr/local/uim-server/dns.json
%attr(0644, root, root) /usr/local/uim-server/route.json
%attr(0644, root, root) /usr/local/uim-server/custom_outbound.json
%attr(0644, root, root) /usr/local/uim-server/custom_inbound.json
%attr(0644, root, root) /usr/local/uim-server/rulelist
%attr(0644, root, root) /usr/local/uim-server/geoip.dat
%attr(0644, root, root) /usr/local/uim-server/geosite.dat
%attr(0644, root, root) /usr/local/uim-server/README.md
%attr(0644, root, root) /usr/local/uim-server/LICENSE
%attr(0644, root, root) %{_sysconfdir}/uim-server
%attr(0644, root, root) %{_sysconfdir}/uim-server/config.yml
%attr(0644, root, root) %{_sysconfdir}/systemd/system/uim-server.service

%changelog
* Sun Jul 24 2022 SSPanel-UIM Team <package@sspanel.org> - 0.9.1-1
 - https://github.com/sspanel-uim/XrayR/releases/tag/v0.9.1
