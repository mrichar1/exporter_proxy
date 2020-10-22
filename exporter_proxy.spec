
Summary: A simple TLS reverse proxy for use with Prometheus exporters
Name: exporter_proxy
Version: 1.0
Release: 1
Group: Applications/System
License: AGPL-3
BuildArch: noarch
Source0: %{name}
Requires: python(abi) >= 3.6

%description
A simple TLS reverse proxy for use with Prometheus exporters.

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{_bindir}
install -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/

%clean
%{__rm} -rf %{buildroot}

%files
%{_bindir}/%{name}

%changelog
* Thu Oct 22 2020 <m.richardson@ed.ac.uk>
- Initial RPM creation.
